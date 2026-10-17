import asyncio
import unittest

import httpx

from openrouter.utils.retries import (
    BackoffStrategy,
    RetryConfig,
    Retries,
    _wraps_transient_inner_code,
    retry,
    retry_async,
)


def response(status_code, json_body=None):
    request = httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions")
    if json_body is None:
        return httpx.Response(status_code, request=request)
    return httpx.Response(status_code, json=json_body, request=request)


def fast_retries():
    # Jitter-free, 1ms intervals. Budget is generous so these tests terminate on
    # success / non-retryable status rather than on the elapsed-time timeout, which
    # keeps `calls` counts deterministic regardless of CI scheduling overhead.
    backoff = BackoffStrategy(
        initial_interval=1, max_interval=1, exponent=1.0, max_elapsed_time=10000, jitter_ms=0
    )
    return Retries(RetryConfig("backoff", backoff, retry_connection_errors=True), ["5XX"])


class WrapsTransientInnerCodeTests(unittest.TestCase):
    def test_400_with_transient_inner_code(self):
        self.assertTrue(_wraps_transient_inner_code(response(400, {"error": {"code": 502}})))

    def test_400_with_string_inner_code(self):
        self.assertTrue(_wraps_transient_inner_code(response(400, {"error": {"code": "529"}})))

    def test_400_invalid_request_inner_400_not_retried(self):
        self.assertFalse(_wraps_transient_inner_code(response(400, {"error": {"code": 400}})))

    def test_400_without_inner_code(self):
        self.assertFalse(_wraps_transient_inner_code(response(400, {"error": {"message": "bad"}})))

    def test_400_non_json_body(self):
        self.assertFalse(_wraps_transient_inner_code(response(400)))


class RetryIntegrationTests(unittest.TestCase):
    def test_retries_400_wrapping_transient_code_then_succeeds(self):
        calls = 0

        def func():
            nonlocal calls
            calls += 1
            if calls < 3:
                return response(400, {"error": {"message": "Provider returned error", "code": 502}})
            return response(200, {"ok": True})

        result = retry(func, fast_retries())
        self.assertEqual(result.status_code, 200)
        self.assertEqual(calls, 3)  # retried twice, then succeeded

    def test_does_not_retry_plain_400(self):
        calls = 0

        def func():
            nonlocal calls
            calls += 1
            return response(400, {"error": {"message": "logprobs must be 0-5", "code": 400}})

        result = retry(func, fast_retries())
        self.assertEqual(result.status_code, 400)
        self.assertEqual(calls, 1)  # not retried

    def test_async_retries_400_wrapping_transient_code_then_succeeds(self):
        calls = 0

        async def func():
            nonlocal calls
            calls += 1
            if calls < 3:
                return response(400, {"error": {"code": 503}})
            return response(200, {"ok": True})

        result = asyncio.run(retry_async(func, fast_retries()))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(calls, 3)


if __name__ == "__main__":
    unittest.main()

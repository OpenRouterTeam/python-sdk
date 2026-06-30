import unittest

import httpx

from openrouter.utils.retries import (
    _is_retryable_response,
    _is_retryable_response_async,
)


def response(status_code, json_body=None):
    request = httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions")
    if json_body is None:
        return httpx.Response(status_code, request=request)
    return httpx.Response(status_code, json=json_body, request=request)


class RetryResponseTests(unittest.TestCase):
    def test_retries_request_timeout_and_rate_limit_by_default(self):
        self.assertTrue(_is_retryable_response(response(408), []))
        self.assertTrue(_is_retryable_response(response(429), []))

    def test_retries_configured_status_code_patterns(self):
        self.assertTrue(_is_retryable_response(response(502), ["5XX"]))
        self.assertTrue(_is_retryable_response(response(529), ["5XX"]))
        self.assertFalse(_is_retryable_response(response(400), ["5XX"]))

    def test_retries_400_with_transient_inner_error_code(self):
        res = response(
            400,
            {
                "error": {
                    "message": "Provider returned error",
                    "code": 502,
                    "metadata": {"provider_name": "example"},
                }
            },
        )

        self.assertTrue(_is_retryable_response(res, ["5XX"]))
        self.assertEqual(res.json()["error"]["code"], 502)

    def test_does_not_retry_400_with_non_transient_inner_error_code(self):
        res = response(
            400,
            {
                "error": {
                    "message": "logprobs must be between 0 and 5",
                    "code": 400,
                }
            },
        )

        self.assertFalse(_is_retryable_response(res, ["5XX"]))


class AsyncRetryResponseTests(unittest.IsolatedAsyncioTestCase):
    async def test_retries_400_with_transient_inner_error_code_async(self):
        res = response(
            400,
            {
                "error": {
                    "message": "Provider returned error",
                    "code": 502,
                    "metadata": {"provider_name": "example"},
                }
            },
        )

        self.assertTrue(await _is_retryable_response_async(res, ["5XX"]))
        self.assertEqual(res.json()["error"]["code"], 502)


if __name__ == "__main__":
    unittest.main()

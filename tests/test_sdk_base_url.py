import unittest
from openrouter.sdk import OpenRouter

class TestOpenRouterSDKBaseURL(unittest.TestCase):
    def test_base_url_initialization(self):
        custom_url = "https://custom.openrouter.ai/api/v1"
        client = OpenRouter(api_key="test_key", base_url=custom_url)
        self.assertEqual(client.sdk_configuration.server_url, custom_url)

if __name__ == "__main__":
    unittest.main()

from openrouter import components


def test_chat_request_supports_openrouter_web_search_server_tool():
    request = components.ChatRequest(
        messages=[{"role": "user", "content": "What changed in AI today?"}],
        tools=[
            components.OpenRouterWebSearchServerTool(
                type="openrouter:web_search",
                parameters=components.WebSearchConfig(
                    max_results=5,
                    search_context_size="medium",
                ),
            )
        ],
    )

    assert request.model_dump(mode="json", exclude_unset=True)["tools"] == [
        {
            "type": "openrouter:web_search",
            "parameters": {"max_results": 5, "search_context_size": "medium"},
        }
    ]


def test_responses_request_supports_openrouter_web_search_server_tool():
    request = components.ResponsesRequest(
        input="What changed in AI today?",
        tools=[
            components.WebSearchServerToolOpenRouter(
                type="openrouter:web_search",
                parameters=components.WebSearchServerToolConfig(
                    max_results=5,
                    search_context_size="medium",
                ),
            )
        ],
    )

    assert request.model_dump(mode="json", exclude_unset=True)["tools"] == [
        {
            "type": "openrouter:web_search",
            "parameters": {"max_results": 5, "search_context_size": "medium"},
        }
    ]


def test_request_plugins_support_web_search_plugin():
    request = components.ChatRequest(
        messages=[{"role": "user", "content": "What changed in AI today?"}],
        plugins=[components.WebSearchPlugin(id="web", max_results=5)],
    )

    assert request.model_dump(mode="json", exclude_unset=True)["plugins"] == [
        {"id": "web", "max_results": 5}
    ]

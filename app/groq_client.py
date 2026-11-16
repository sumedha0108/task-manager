from groq import Groq
from . import config

_client: Groq | None = None


def _get_client() -> Groq:
    global _client
    if _client is None:
        if not config.GROQ_API_KEY:
            raise RuntimeError("GROQ_API_KEY is not set")
        _client = Groq(api_key=config.GROQ_API_KEY)
    return _client


def chat_json(messages: list[dict]) -> str:
    """One call to Groq. Returns the raw text of the reply."""
    resp = _get_client().chat.completions.create(
        model=config.GROQ_MODEL,
        messages=messages,
        response_format={"type": "json_object"},  # asks the model for valid JSON
        temperature=0.4,
        max_completion_tokens=1500,  # free tier: 8K tokens/min, so keep replies small
        reasoning_effort="low",      # gpt-oss thinks first; low burns fewer tokens
    )
    return resp.choices[0].message.content or ""
import requests


def review_code(
    prompt: str
) -> str:

    url = (
        "http://localhost:11434/api/generate"
    )

    payload = {
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        url,
        json=payload,
        timeout=120
    )

    data = response.json()

    return data.get(
        "response",
        "No review generated."
    )
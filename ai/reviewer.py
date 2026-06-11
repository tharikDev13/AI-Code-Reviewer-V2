import requests


def review_code(
    prompt: str
) -> str:

    url = (
        "http://localhost:11434/api/generate"
    )

    payload = {
        "model": "deepseek-coder:6.7b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "top_p": 0.1,
            "num_predict": 512
        }
    }

    response = requests.post(
        url,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data.get(
        "response",
        "No review generated."
    )
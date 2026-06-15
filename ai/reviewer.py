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
            "top_p": 0,
            "repeat_penalty": 1.0,
            "num_predict": 256
        }
    }

    print(
        "\n===== OLLAMA PROMPT =====\n"
    )

    print(prompt)

    print(
        "\n=========================\n"
    )

    response = requests.post(
        url,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    review = data.get(
        "response",
        "No review generated."
    )

    print(
        "\n===== RAW MODEL RESPONSE =====\n"
    )

    print(review)

    print(
        "\n==============================\n"
    )

    return review.strip()
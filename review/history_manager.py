import json
import os


HISTORY_FILE = (
    "review_history.json"
)


def load_history():

    if not os.path.exists(
        HISTORY_FILE
    ):

        return {}

    with open(
        HISTORY_FILE,
        "r"
    ) as file:

        try:

            return json.load(
                file
            )

        except Exception:

            return {}


def save_history(
    history
):

    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )


def get_pr_findings(
    pr_number
):

    history = load_history()

    pr_key = str(
        pr_number
    )

    if pr_key not in history:

        return []

    return history[
        pr_key
    ].get(
        "open_findings",
        []
    )


def update_pr_findings(
    pr_number,
    findings
):

    history = load_history()

    pr_key = str(
        pr_number
    )

    history[
        pr_key
    ] = {
        "open_findings":
        findings
    }

    save_history(
        history
    )
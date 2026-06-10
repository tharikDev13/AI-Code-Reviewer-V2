from fastapi import FastAPI, Request

from github.repository_manager import clone_repository
from github.diff_extractor import get_diff
from github.changed_files import get_changed_files
from github.pr_commenter import post_pr_comment

from ai.prompt_builder import build_review_prompt
from ai.reviewer import review_code

import json
import hmac
import hashlib

app = FastAPI()

GITHUB_SECRET = "ai-reviewer-secret-2026"


def verify_signature(
    payload_body: bytes,
    signature_header: str
):

    if not signature_header:
        return False

    try:

        sha_name, signature = (
            signature_header.split("=")
        )

        if sha_name != "sha256":
            return False

        mac = hmac.new(
            GITHUB_SECRET.encode(),
            msg=payload_body,
            digestmod=hashlib.sha256
        )

        expected_signature = (
            mac.hexdigest()
        )

        return hmac.compare_digest(
            expected_signature,
            signature
        )

    except Exception as e:

        print(
            f"Signature Error: {e}"
        )

        return False


@app.get("/")
def home():

    return {
        "message": "AI Code Reviewer V2 Running"
    }


@app.post("/github/webhook")
async def github_webhook(request: Request):

    body = await request.body()

    signature = request.headers.get(
        "X-Hub-Signature-256"
    )

    validation_result = verify_signature(
        body,
        signature
    )

    print("\n================================")
    print("Webhook Received")
    print(
        "Signature Valid:",
        validation_result
    )

    if not validation_result:

        print(
            "Webhook Signature Failed"
        )

        return {
            "status": "error",
            "message": "Invalid signature"
        }

    payload = json.loads(
        body.decode("utf-8")
    )

    event = request.headers.get(
        "X-GitHub-Event"
    )

    print("Event:", event)

    action = payload.get("action")

    print("Action:", action)

    if event == "ping":

        print(
            "GitHub App webhook verified"
        )

        return {
            "status": "success",
            "message": "pong"
        }

    if event == "pull_request":

        pr = payload.get(
            "pull_request",
            {}
        )

        repo = payload.get(
            "repository",
            {}
        )

        repo_name = repo.get(
            "full_name"
        )

        pr_number = pr.get(
            "number"
        )

        source_branch = pr.get(
            "head",
            {}
        ).get(
            "ref"
        )

        target_branch = pr.get(
            "base",
            {}
        ).get(
            "ref"
        )

        print("\n----- PR DETAILS -----")

        print(
            "Repository:",
            repo_name
        )

        print(
            "PR Number:",
            pr_number
        )

        print(
            "Source Branch:",
            source_branch
        )

        print(
            "Target Branch:",
            target_branch
        )

        if action in [
            "opened",
            "synchronize",
            "reopened"
        ]:

            print(
                "\nStarting Repository Clone..."
            )

            workspace_path = (
                f"workspace/pr_{pr_number}"
            )

            workspace_path = clone_repository(
                repo_name,
                workspace_path
            )

            print(
                "Repository Clone Completed"
            )

            print(
                "\nStarting Diff Extraction..."
            )

            diff = get_diff(
                workspace_path,
                target_branch,
                source_branch
            )

            print(
                "\n===== PR DIFF =====\n"
            )

            print(diff)

            print(
                "\n===================\n"
            )

            changed_files = get_changed_files(
                workspace_path,
                target_branch,
                source_branch
            )

            print(
                "\n===== CHANGED FILES ====="
            )

            for file in changed_files:

                print(file)

            print(
                "========================="
            )

            print(
                "\nStarting AI Review..."
            )

            prompt = build_review_prompt(
                diff,
                changed_files
            )

            review = review_code(
                prompt
            )

            print(
                "\n===== AI REVIEW =====\n"
            )

            print(review)

            print(
                "\n=====================\n"
            )

            print(
                "\nPosting Comment To GitHub..."
            )

            try:

                post_pr_comment(
                    repo_name,
                    pr_number,
                    review
                )

                print(
                    "GitHub Comment Posted"
                )

            except Exception as e:

                print(
                    f"GitHub Comment Error: {e}"
                )

        else:

            print(
                f"Skipping action: {action}"
            )

    print(
        "\n================================\n"
    )

    return {
        "status": "success"
    }
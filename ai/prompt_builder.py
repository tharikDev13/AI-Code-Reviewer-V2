def build_review_prompt(
    diff: str,
    changed_files: list
) -> str:

    files = "\n".join(
        changed_files
    )

    prompt = f"""
You are a senior mobile code reviewer.

Review this pull request.

Changed Files:

{files}

Review Checklist:

SECURITY
- Hardcoded passwords
- Hardcoded API keys
- Sensitive data in logs
- Unsafe authentication

BUGS
- Force unwraps
- Force try
- Null pointer risks
- Array index out of bounds

PERFORMANCE
- Blocking network calls
- Unnecessary object creation
- Expensive loops
- Main thread blocking

ANDROID
- GlobalScope usage
- Memory leaks
- Lifecycle issues

IOS
- Force unwraps
- Retain cycles
- UI updates from background threads

Rules:

- Do not explain the code.
- Only report findings.
- If no issues exist return:
No significant issues found.

Output Format:

SUMMARY:
...

ISSUES:
...

SUGGESTIONS:
...

DIFF:

{diff}
"""

    return prompt
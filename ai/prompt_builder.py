def build_review_prompt(
    diff: str,
    changed_files: list
) -> str:

    files = "\n".join(
        changed_files
    )

    prompt = f"""
You are a Staff Software Engineer reviewing a pull request.

Review ONLY the code changes present in the diff.

Changed Files:

{files}

Focus ONLY on real issues.

Review Categories:

SECURITY
- Hardcoded passwords
- Hardcoded API keys
- Secrets or tokens
- Sensitive data in logs
- Unsafe authentication
- Insecure credential storage

BUGS
- Force unwraps (!)
- Force try (try!)
- Null pointer risks
- Array index out of bounds
- Unhandled errors
- Crash risks
- Unsafe casts

PERFORMANCE
- Blocking network calls
- Main thread blocking
- Expensive loops
- Unnecessary allocations
- Memory leaks

IOS
- UI updates from background threads
- Retain cycles
- Strong self capture
- Threading issues

ANDROID
- GlobalScope usage
- Lifecycle issues
- Memory leaks
- Coroutine misuse

Rules:

1. Review ONLY the changed code.
2. Ignore style issues.
3. Ignore formatting issues.
4. Ignore comments.
5. Ignore naming issues.
6. Ignore code organization suggestions.
7. Ignore best-practice suggestions unless they create a real bug.
8. Report only real defects, security issues, crash risks or performance issues.
9. Do NOT explain the code.
10. Do NOT summarize the PR.
11. Do NOT provide praise.
12. Do NOT provide suggestions.
13. Do NOT invent issues.
14. If no issue exists return EXACTLY:

No significant issues found.

Output Format:

[HIGH] Description

[MEDIUM] Description

[LOW] Description

Examples:

[HIGH] Hardcoded API key detected.

[HIGH] Hardcoded password detected.

[MEDIUM] Force unwrap detected using URL(...)!.

[MEDIUM] Force try detected using try!.

[MEDIUM] Potential IndexOutOfBoundsException from users[0].

[MEDIUM] UI updated from background thread.

[LOW] Sensitive data logged.

Pull Request Diff:

{diff}
"""

    return prompt
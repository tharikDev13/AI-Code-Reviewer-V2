def build_review_prompt(
    diff: str,
    changed_files: list
) -> str:

    files = "\n".join(
        changed_files
    )

    prompt = f"""
You are a Staff Software Engineer performing a pull request review.

Review ONLY the code changes in the diff.

Changed Files:

{files}

Focus on finding REAL issues only.

Check for:

SECURITY
- Hardcoded passwords
- Hardcoded API keys
- Secrets or tokens
- Sensitive data in logs
- Unsafe authentication

BUGS
- Force unwraps (!)
- Force try (try!)
- Null pointer risks
- Index out of bounds
- Unhandled errors
- Crash risks

PERFORMANCE
- Blocking network calls
- Main thread blocking
- Expensive loops
- Unnecessary allocations

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

1. Do NOT explain the code.
2. Do NOT summarize the PR.
3. Do NOT provide praise.
4. Do NOT output SUMMARY.
5. Do NOT output ISSUES.
6. Do NOT output SUGGESTIONS.
7. Report only findings.
8. Ignore style issues.
9. Ignore formatting issues.
10. Ignore comments.

Output examples:

[HIGH] Hardcoded API key detected.

[HIGH] Hardcoded password detected.

[MEDIUM] Potential IndexOutOfBoundsException from users[0].

[MEDIUM] Force unwrap detected using URL(...)!.

[MEDIUM] Force try detected using try!.

[MEDIUM] UI updated from background thread.

If no issues exist return EXACTLY:

No significant issues found.

Pull Request Diff:

{diff}
"""

    return prompt
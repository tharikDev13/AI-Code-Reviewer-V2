def build_review_prompt(
    diff: str,
    changed_files: list
) -> str:

    files = "\n".join(
        changed_files
    )

    prompt = f"""
You are a senior code reviewer.

Review ONLY added (+) lines.

DO NOT review:
- deleted (-) lines
- unchanged context lines
- surrounding code

Only report issues introduced by the newly added lines.

Rules:

- Report only real defects.
- Report only security issues.
- Report only crash risks.
- Report only performance issues.
- Ignore style.
- Ignore formatting.
- Ignore naming.
- Ignore architecture suggestions.
- Ignore best practices unless they create a real bug.
- Do not explain findings.
- Do not provide notes.
- Do not provide recommendations.
- Do not provide examples.
- Do not provide summaries.
- Do not invent issues.

Output format:

[HIGH] Finding

[MEDIUM] Finding

[LOW] Finding

If no findings exist return exactly:

No significant issues found.

Changed Files:

{files}

Diff:

{diff}
"""

    return prompt
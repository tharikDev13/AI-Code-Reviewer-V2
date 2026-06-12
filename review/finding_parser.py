def parse_findings(
    review_text
):

    findings = []

    if (
        not review_text
        or review_text.strip()
        == "No significant issues found."
    ):

        return findings

    lines = review_text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if (
            line.startswith("[HIGH]")
            or line.startswith("[MEDIUM]")
            or line.startswith("[LOW]")
        ):

            findings.append(
                line
            )

    return findings
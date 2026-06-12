def compare_reviews(
    previous_findings,
    current_findings
):

    previous_set = set(
        previous_findings
    )

    current_set = set(
        current_findings
    )

    new_findings = list(
        current_set
        - previous_set
    )

    resolved_findings = list(
        previous_set
        - current_set
    )

    reopened_findings = []

    return {
        "new_findings":
        sorted(new_findings),

        "resolved_findings":
        sorted(resolved_findings),

        "reopened_findings":
        reopened_findings,

        "open_findings":
        sorted(current_set)
    }
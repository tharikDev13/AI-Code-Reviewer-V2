from git import Repo


def get_diff(
    repo_path,
    target_branch,
    source_branch
):

    repo = Repo(repo_path)

    origin = repo.remotes.origin

    origin.fetch()

    try:

        diff_output = repo.git.diff(
            f"origin/{target_branch}",
            f"origin/{source_branch}"
        )

        return diff_output

    except Exception as e:

        print(
            f"Diff Extraction Error: {e}"
        )

        return ""


def get_incremental_diff(
    repo_path,
    before_sha,
    after_sha
):

    repo = Repo(repo_path)

    try:

        diff_output = repo.git.diff(
            before_sha,
            after_sha
        )

        return diff_output

    except Exception as e:

        print(
            f"Incremental Diff Error: {e}"
        )

        return ""
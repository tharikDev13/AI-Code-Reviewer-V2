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
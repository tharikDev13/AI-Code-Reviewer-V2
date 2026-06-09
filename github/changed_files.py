from git import Repo


def get_changed_files(
    repo_path,
    target_branch,
    source_branch
):

    repo = Repo(repo_path)

    origin = repo.remotes.origin

    origin.fetch()

    try:

        changed_files = repo.git.diff(
            "--name-only",
            f"origin/{target_branch}",
            f"origin/{source_branch}"
        )

        return changed_files.splitlines()

    except Exception as e:

        print(
            f"Changed Files Error: {e}"
        )

        return []
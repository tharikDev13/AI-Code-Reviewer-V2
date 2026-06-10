from github.github_auth import (
    generate_installation_token
)

token = generate_installation_token()

print("\nTOKEN GENERATED\n")

print(token[:20] + "...")
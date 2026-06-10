from ai.prompt_builder import (
    build_review_prompt
)

from ai.reviewer import (
    review_code
)


diff = """
diff --git a/LoginView.swift b/LoginView.swift

+ let password = "admin123"

+ DispatchQueue.global().async {
+     self.userLabel.text = user.name
+ }

+ let user = users[0]

+ print("User token: \\(token)")
"""

prompt = build_review_prompt(
    diff
)

review = review_code(
    prompt
)

print(
    "\n===== AI REVIEW =====\n"
)

print(review)

print(
    "\n=====================\n"
)
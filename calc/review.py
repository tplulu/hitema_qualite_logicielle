import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_code_diff(diff):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Review the following code diff and provide feedback:\n{diff}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

import openai
import os

# Configurer votre clé API OpenAI à partir de l'environnement
openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_code_diff(diff):
    try:
        # Appel à l'API OpenAI pour générer des suggestions de revue de code
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Review the following code diff and provide feedback:\n{diff}",
            max_tokens=150
        )
        return response.choices[0].text.strip()  # Récupérer et retourner la suggestion de revue
    except Exception as e:
        return f"Error analyzing code diff: {str(e)}"

# Exemple d'utilisation pour tester la fonction analyze_code_diff
if __name__ == "__main__":
    diff = """
    Here you would provide the actual code diff to be analyzed.
    This is a placeholder for demonstration purposes.
    """
    review_comment = analyze_code_diff(diff)
    print("Review comment generated:")
    print(review_comment)

import anthropic
import os
import re
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API Anthropic depuis les variables d'environnement
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

# Créer une instance du client Anthropic
client = anthropic.Anthropic(api_key=anthropic_api_key)

DEFAULT_MODEL = "claude-3-haiku-20240307"

def analyze_code_diff(diff):
    try:
        # Structure du prompt pour l'IA
        prompt = f"\n\nHuman:\n\nReview the following code diff and provide feedback:\n{diff}"

        # Appel à l'API Anthropic pour générer des suggestions de revue de code
        response = client.messages.create(
            model=DEFAULT_MODEL,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        )
        
        # Extraire le contenu de la réponse de l'API
        feedback = response.content[0].text

        return feedback

    except Exception as e:
        return f"Error analyzing code diff: {str(e)}"

if __name__ == "__main__":
    # Exemple de diff de code à analyser
    diff = """
    Here you would provide the actual code diff to be analyzed.
    This is a placeholder for demonstration purposes.
    """
    review_comment = analyze_code_diff(diff)
    print("Review comment generated:")
    print(review_comment)

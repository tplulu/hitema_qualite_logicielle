import anthropic
import os
import sys
import argparse
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API Anthropic depuis les variables d'environnement
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

# Vérifier que la clé API est correctement lue
if not anthropic_api_key:
    raise ValueError("La clé API Anthropic n'a pas été trouvée. Veuillez vérifier votre fichier .env.")

# Créer une instance du client Anthropic
client = anthropic.Anthropic(api_key=anthropic_api_key)

DEFAULT_MODEL = "claude-3-haiku-20240307"

def analyze_code_diff(diff):
    try:
        # Structure du prompt pour l'IA
        prompt = "Human: Review the following code diff and provide feedback : {diff}"

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

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            diff = file.read()
        feedback = analyze_code_diff(diff)
        print(feedback)
    except Exception as e:
        print(f"Error reading file: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze code diff for review.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the file containing the code diff')
    args = parser.parse_args()
    main(args.file)


import anthropic
import os
import argparse
from dotenv import load_dotenv

def load_api_key(api_key_env):
    # Charger les variables d'environnement depuis le fichier .env
    load_dotenv()

    # Récupérer la clé API Anthropic depuis les variables d'environnement
    anthropic_api_key = os.getenv(api_key_env)

    # Vérifier que la clé API est correctement lue
    if not anthropic_api_key:
        raise ValueError(f"La clé API Anthropic n'a pas été trouvée. Veuillez vérifier votre fichier .env pour la variable {api_key_env}.")

    return anthropic_api_key

def analyze_code_diff(api_key, diff):
    try:
        # Créer une instance du client Anthropic
        client = anthropic.Anthropic(api_key=api_key)

        # Structure du prompt pour l'IA
        prompt = f"Human: Review the following code diff and provide feedback : {diff}"

        # Appel à l'API Anthropic pour générer des suggestions de revue de code
        response = client.messages.create(
            model="claude-3-haiku-20240307",
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

def main():
    parser = argparse.ArgumentParser(description='Analyze code diff for review.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the file containing the code diff')
    parser.add_argument('-k', '--api-key', type=str, required=True, help='API key for Anthropic')
    args = parser.parse_args()

    api_key = load_api_key(args.api_key)

    try:
        with open(args.file, 'r') as file:
            diff = file.read()
        feedback = analyze_code_diff(api_key, diff)
        print(feedback)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

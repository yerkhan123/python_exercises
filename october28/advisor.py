from google import genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_API_KEY = "твой_ключ"
def main():

    client = genai.Client(api_key=GEMINI_API_KEY)
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input="Привет как дела"
    )
    print(interaction.output_text)


if __name__ == "__main__":
    main()

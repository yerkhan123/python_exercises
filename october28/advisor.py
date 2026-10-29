from google import genai
import os
os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
export GEMINI_API_KEY="НОВЫЙ_КЛЮЧ"
def main():

    client = genai.Client(api_key=GEMINI_API_KEY)
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input="Привет как дела"
    )
    print(interaction.output_text)


if __name__ == "__main__":
    main()

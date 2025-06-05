from google import genai

def ask_gemini(API_KEY: str, prompt: str):
    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=prompt
    )

    return response.text
from google import genai

# client gets api key from environment variable GEMINI_API_KEY
genai_client = genai.Client()

# genai_prompt = genai.TextPrompt
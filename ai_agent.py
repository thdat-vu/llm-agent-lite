import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY in your .env file.")

genai.configure(api_key=api_key)

# Create a model instance
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate a response
response = model.generate_content("Explain how AI works in a few words")

print(response.text)
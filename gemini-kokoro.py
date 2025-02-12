import os
from dotenv import load_dotenv
import google.generativeai as genai
import soundfile as sf
from kokoro_onnx import Kokoro

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_user_input():
    """Get the user's question/prompt from terminal"""
    print("\nWhat would you like me to talk about? (Type 'quit' to exit)")
    return input("> ")

def generate_text(prompt):
    """Generate text using Gemini API"""
    response = model.generate_content(prompt)
    return response.text

def text_to_speech(text):
    """Convert text to speech using Kokoro TTS"""
    kokoro = Kokoro("kokoro-v1.0.onnx", "voices.json")
    samples, sample_rate = kokoro.create(
        text,
        voice="af_sarah",
        speed=1.0,
        lang="en-us"
    )
    sf.write("audio.wav", samples, sample_rate)
    print("Created audio.wav")

def main():
    print("Welcome to Gemini-Kokoro TTS!")
    print("This program will convert your questions into speech using Gemini AI and Kokoro TTS.")
    
    while True:
        user_prompt = get_user_input()
        if user_prompt.lower() == 'quit':
            break
            
        try:
            # Generate text using Gemini
            generated_text = generate_text(user_prompt)
            print("\nGenerated text:")
            print(generated_text)
            
            # Convert to speech
            print("\nConverting to speech...")
            text_to_speech(generated_text)
            
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            continue

if __name__ == "__main__":
    main()
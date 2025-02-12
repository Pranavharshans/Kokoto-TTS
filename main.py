import soundfile as sf
from kokoro_onnx import Kokoro

kokoro = Kokoro("kokoro-v1.0.onnx", "voices.json")
samples, sample_rate = kokoro.create(
"""
That sounds like a fantastic idea! A children's storytelling app powered by Gemini API and TTS could be a fun and engaging experience. Here's how you might structure it:

User Interaction:

Allow the user (parent or child) to input some personalized information (name, favorite animals, settings, etc.).
Optionally, you could also let the user choose a theme or genre (adventure, fantasy, etc.).
Story Generation:

Use the Gemini API to generate a personalized story based on the user’s input. You could provide a basic template or allow more creativity, such as choosing plot twists, characters, and scenarios.
"""
    , voice="af_sarah", speed=1.0, lang="en-us"
)
sf.write("audio.wav", samples, sample_rate)
print("Created audio.wav")

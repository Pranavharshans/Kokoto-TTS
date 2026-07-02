# Kokoro-TTS × Gemini

AI-powered text-to-speech pipeline that combines Google Gemini (gemini-2.0-flash) for response generation with Kokoro ONNX TTS for speech synthesis. Type a prompt and get a spoken audio response.

## How It Works

1. User enters a text prompt
2. Gemini generates a natural, speech-optimized response
3. Kokoro TTS converts the response to an audio file (`audio.wav`)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranavharshans/Kokoro-TTS-x-Gemini.git
   cd Kokoro-TTS-x-Gemini
   ```

2. Install dependencies:
   ```bash
   pip install google-generativeai kokoro-onnx soundfile python-dotenv
   ```

3. Download the Kokoro ONNX model files and place them in the project directory:
   - `kokoro-v1.0.onnx`
   - `voices.json`

4. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```

## Usage

```bash
python gemini-kokoro.py
```

Enter a prompt at the terminal. Gemini will generate a natural-sounding response optimized for speech, and Kokoro TTS will convert it to `audio.wav`. Type `quit` to exit.

### Example

```
You: Explain quantum computing in simple terms
(Response generated and saved to audio.wav)
```

## Project Structure

```
Kokoro-TTS-x-Gemini/
├── gemini-kokoro.py    # Main application: Gemini + Kokoro TTS pipeline
├── main.py             # Standalone Kokoro TTS demo script
└── .gitignore
```

## Dependencies

- `google-generativeai` — Google Gemini API SDK
- `kokoro-onnx` — Kokoro ONNX TTS runtime
- `soundfile` — WAV file writing
- `python-dotenv` — Environment variable management

## Model Files Required

- Kokoro ONNX model (`kokoro-v1.0.onnx`)
- Voice config (`voices.json`)
- Google Gemini API key (set in `.env`)

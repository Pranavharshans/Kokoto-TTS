# CLAUDE.md — Kokoro-TTS × Gemini

AI TTS pipeline combining Google Gemini with Kokoro ONNX TTS.

## Project overview

- `gemini-kokoro.py` — main application loop: accepts prompts, generates speech-optimized text via Gemini (gemini-2.0-flash), converts to audio with Kokoro TTS, saves as `audio.wav`
- `main.py` — standalone Kokoro TTS demo with hardcoded sample text

## Setup

```bash
pip install -r requirements.txt
```

Requires two external model files in the project root: `kokoro-v1.0.onnx` and `voices.json`. Set `GEMINI_API_KEY` in a `.env` file.

## Running

```bash
python gemini-kokoro.py
```

Type prompts interactively. Type `quit` to exit.

## Output

Audio saved to `audio.wav` in the project root. The `.gitignore` excludes `*.wav`, `*.onnx`, `*.json`, `env/`, and `.env`.

# 🎬 AI Video Assistant with RAG

> An AI-powered assistant that lets you **ask questions about any YouTube video** — powered by Whisper transcription, ChromaDB vector search, and Mistral AI via LangChain.

---

## ✨ Features

- 🎥 **YouTube Audio Download** — fetches the best audio stream via `yt-dlp`
- 🔊 **Audio Processing** — resamples to 16 kHz mono WAV using FFmpeg & pydub
- 📝 **Local Transcription** — runs OpenAI Whisper on-device (no API cost)
- 🌐 **Hindi / Hinglish Support** — auto-translates to English via `deep-translator`
- 🧩 **Chunking & Embedding** — splits transcript and embeds with `sentence-transformers`
- 🗃️ **Vector Store** — persists embeddings in ChromaDB for fast semantic retrieval
- 🤖 **RAG Q&A** — retrieves relevant chunks and answers via Mistral AI + LangChain LCEL
- 📋 **Auto Summarization** — generates a concise summary of the video
- ✅ **Action Item Extraction** — pulls out actionable tasks from the content
- 🔑 **Key Decision Extraction** — identifies key decisions discussed
- ❓ **Open Questions** — surfaces unresolved questions from the video
- 💬 **Interactive Chat (CLI)** — conversational loop powered by the RAG chain
- 🖥️ **Streamlit Web UI** — end-to-end browser interface with PDF export

---

## 🗂️ Project Structure

```
AI-Video-Assistant/
├── core/
│   ├── extractor.py       # Action items, key decisions & question extraction
│   ├── rag_engine.py      # RAG chain build & query logic
│   ├── summarizer.py      # Summarization & title generation
│   ├── transcriber.py     # Whisper transcription + translation
│   └── vector_store.py    # ChromaDB embedding & retrieval
├── utils/
│   └── audio_processor.py # yt-dlp download + FFmpeg audio conversion
├── app.py                 # Streamlit web application (UI)
├── main.py                # CLI entry point
├── requirements.txt
└── .env                   # API keys (not committed)
```

---

## ⚙️ How It Works

1. **Download** — `yt-dlp` pulls the best audio stream from a YouTube URL (or a local file path)
2. **Convert** — FFmpeg resamples the audio to 16 kHz mono WAV
3. **Transcribe** — Whisper transcribes the audio locally on your machine
4. **Translate** *(optional)* — Hindi/Hinglish content is translated to English via `deep-translator`
5. **Chunk & Embed** — the transcript is split into overlapping chunks and embedded using `sentence-transformers`
6. **Store** — embeddings are persisted in a local ChromaDB vector store
7. **Analyze** — Mistral AI generates a title, summary, action items, key decisions, and open questions
8. **Query** — user questions are answered by retrieving relevant chunks and passing them to Mistral AI via LangChain
9. **UI** — a Streamlit frontend provides end-to-end interaction with PDF export

---

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Amankhan0087/AI-Video-Assistant-With-RAG.git
cd AI-Video-Assistant-With-RAG
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** FFmpeg must be installed separately and available on your system PATH.
> - Windows: https://ffmpeg.org/download.html
> - macOS: `brew install ffmpeg`
> - Linux: `sudo apt install ffmpeg`

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

Get your free Mistral API key at https://console.mistral.ai

---

## ▶️ Running the App

### Streamlit Web UI

```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

### CLI Mode

```bash
python main.py
```

You will be prompted for a YouTube URL (or local file path) and the language (`english` / `hinglish`). After processing, a two-phase output is shown:

- **Phase 1** — title, summary, action items, key decisions, open questions
- **Phase 2** — interactive chat loop (type `exit` to quit)

---

## 🧰 Tech Stack

| Layer | Library |
|---|---|
| Audio download | `yt-dlp` |
| Audio processing | `FFmpeg`, `pydub` |
| Speech-to-text | `openai-whisper` + `torch` |
| Translation | `deep-translator` |
| Embeddings | `sentence-transformers` |
| Vector store | `ChromaDB` |
| LLM / RAG | `LangChain` + `Mistral AI` |
| UI | `Streamlit` |
| PDF export | `fpdf2`, `reportlab` |

---

## 📋 Requirements

```
Python >= 3.10
yt-dlp>=2024.4.9
pydub>=0.25.1
ffmpeg-python>=0.2.0
openai-whisper>=20231117
torch>=2.2.0
torchaudio>=2.2.0
deep-translator>=1.11.4
langchain>=0.2.0
langchain-community>=0.2.0
langchain-mistralai>=0.1.0
mistralai>=0.4.0
chromadb>=0.5.0
sentence-transformers>=2.7.0
streamlit>=1.35.0
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source. See the [LICENSE](LICENSE) file for details.

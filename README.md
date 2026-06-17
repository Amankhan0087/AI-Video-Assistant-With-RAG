# AI Video Assistant with RAG

Ask questions about any YouTube video. The pipeline downloads audio, transcribes it, stores chunks in a vector database, and answers queries using a RAG (Retrieval-Augmented Generation) approach powered by Mistral AI.

## How it works

1. **Download** — `yt-dlp` pulls the best audio stream from a YouTube URL
2. **Convert** — FFmpeg resamples it to 16 kHz mono WAV
3. **Transcribe** — audio is transcribed to text
4. **Chunk & embed** — text is split into chunks and embedded via `sentence-transformers`
5. **Store** — embeddings are stored in ChromaDB
6. **Query** — user questions are answered by retrieving relevant chunks and passing them to Mistral AI via LangChain
7. **UI** — Streamlit frontend for end-to-end interaction; results exportable as PDF

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Create a `.env` file:

```
MISTRAL_API_KEY=your_key_here
```

## Run

```bash
streamlit run app.py
```

## Stack

| Layer | Library |
|---|---|
| Audio download | yt-dlp |
| Audio processing | FFmpeg, pydub |
| Embeddings | sentence-transformers |
| Vector store | ChromaDB |
| LLM / RAG | LangChain + Mistral AI |
| Translation | deep-translator |
| UI | Streamlit |
| Export | fpdf2, reportlab |

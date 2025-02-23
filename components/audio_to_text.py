import streamlit as st
import whisper
import io
import soundfile as sf
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]


def convert_audio_to_text(audio_path, model="turbo"):
    # data, sr = sf.read(io.BytesIO(audio))
    try:
        model = whisper.load_model(model)
        result = model.transcribe(audio_path)
        transcription = result["text"]

        st.markdown(f"**Transcription:** {transcription}")
        return transcription
    except FileNotFoundError:
        pass

def transcribe_audio(audio_file):
    """
    Takes a BytesIO audio file and uses OpenAI's Whisper model to transcribe it.
    Returns the transcription text.
    """
    if audio_file is None:
        st.error("No audio file provided for transcription.")
        return ""
    try:
        # Ensure your OpenAI API key is set before calling this.
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript.get("text", "")
    except Exception as e:
        st.error(f"Transcription failed: {e}")
        return ""
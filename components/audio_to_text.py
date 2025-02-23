import streamlit as st
import whisper
import io
import soundfile as sf


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
import streamlit as st
from components.audio_recorder import record_audio
from components.audio_to_text import convert_audio_to_text, transcribe_audio
from components.feedback_generator import generate_feedback

def main():
    st.title("Interview Feedback Generator")
    audio = record_audio("audio.mp3")
    # text = transcribe_audio(audio)
    # text = convert_audio_to_text("audio.mp3")
    # feedback = generate_feedback(text)
    
if __name__ == "__main__":
    main()
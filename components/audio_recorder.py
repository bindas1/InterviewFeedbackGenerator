import streamlit as st
from st_audiorec import st_audiorec

def record_audio(save_file_path=None):
    # Display instructions
    st.write("Press the button to record your voice. When finished, the audio will be saved and playable below.")
    
    wav_audio_data = st_audiorec()

    if wav_audio_data and save_file_path is not None:
        with open(save_file_path, "wb") as f:
            f.write(wav_audio_data)
        st.success(f"Audio saved as {save_file_path}!")
    return wav_audio_data
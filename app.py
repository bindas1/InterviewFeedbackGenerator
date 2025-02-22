import streamlit as st
from st_audiorec import st_audiorec  # Install via pip install streamlit-audiorecorder

def main():
    st.title("Audio Recorder App")
    
    # Display instructions
    st.write("Press the button to record your voice. When finished, the audio will be saved and playable below.")
    
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')
        
        # Save the audio data to a file
        with open("output.wav", "wb") as f:
            f.write(wav_audio_data)
        st.success("Audio recorded and saved as output.wav!")
    
if __name__ == "__main__":
    main()
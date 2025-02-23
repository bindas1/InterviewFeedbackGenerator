import streamlit as st
from st_audiorec import st_audiorec

import streamlit as st
import openai
import numpy as np
import io
import soundfile as sf
import av
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase


def record_audio(save_file_path=None):
    # Display instructions
    st.write("Press the button to record your voice. When finished, the audio will be saved and playable below.")
    
    wav_audio_data = st_audiorec()

    if wav_audio_data and save_file_path is not None:
        with open(save_file_path, "wb") as f:
            f.write(wav_audio_data)
        st.success(f"Audio saved as {save_file_path}!")
    return wav_audio_data

# class AudioRecorder(AudioProcessorBase):
#     def __init__(self):
#         self.frames = []

#     def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
#         # Convert frame to a numpy array and store it.
#         pcm = frame.to_ndarray()
#         self.frames.append(pcm)
#         return frame

# def record_audio():
#     """
#     Uses streamlit-webrtc to capture audio from the user's microphone.
#     When the user clicks "Stop Recording", the captured audio is concatenated,
#     saved as a WAV file in-memory, and returned as a BytesIO object.
#     """
#     st.title("Microphone Audio Recorder")
#     st.write("Press the 'Stop Recording' button when you're done.")
    
#     # Create the audio recorder component.
#     recorder = AudioRecorder()
#     webrtc_ctx = webrtc_streamer(
#         key="audio_recorder",
#         media_stream_constraints={"audio": True, "video": False},
#         audio_processor_factory=lambda: recorder,
#     )
    
#     # Provide a button to stop recording.
#     if st.button("Stop Recording"):
#         webrtc_ctx.stop()
#         if recorder.frames:
#             # Concatenate recorded frames (each is a numpy array).
#             audio_data = np.concatenate(recorder.frames, axis=1)
#             mem_file = io.BytesIO()
#             # Assume a sample rate (adjust if needed).
#             sample_rate = 48000
#             # soundfile expects shape (samples, channels) so we transpose.
#             sf.write(mem_file, audio_data.T, sample_rate, format="WAV")
#             mem_file.seek(0)
#             st.audio(mem_file, format="audio/wav")
#             return mem_file
#         else:
#             st.error("No audio frames recorded.")
#     return None
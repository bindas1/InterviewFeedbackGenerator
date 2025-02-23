import streamlit as st
from components.audio_recorder import record_audio
# from components.audio_to_text import convert_audio_to_text, transcribe_audio
# from components.feedback_generator import generate_feedback
from components.wordware_audio_to_text import upload_to_transfersh, call_wordware_api

def main():
    st.title("Interview Feedback Generator")
    audio_path = "audio.mp3"
    _ = record_audio(audio_path)
    # text = transcribe_audio(audio)
    # text = convert_audio_to_text("audio.mp3")
    # feedback = generate_feedback(text)
    
    if st.button("Generate Feedback"):
        transcript = ""
        
        try:
            audio_url = upload_to_transfersh(audio_path)
            print("Audio file uploaded successfully. URL:", audio_url)
        except Exception as e:
            print("Error during upload:", e)
            return
        
        # print("Calling Wordware API...")
        # try:
        #     result = call_wordware_api(audio_url, transcript)
        #     st.markdown(f"**Feedback:** {result}")
        # except Exception as e:
        #     print("Error calling Wordware API:", e)
    
if __name__ == "__main__":
    main()
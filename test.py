import os
import streamlit as st
from audiorecorder import AudioRecorder

def main():
    st.set_page_config(page_title="Audio Recorder", page_icon=":microphone:", layout="wide")
    st.title("Audio Recorder Test")
    st.write("This is a test for the audio recorder.")

    audio = AudioRecorder("Click to Start Recording", "Click to Stop Recording")

    if len(audio) > 0:
        
        # play the audio
        st.audio(audio.export().read())

        # save the audio to a file
        audio.export("test.wav", format="wav")
        st.write(f"Audio saved to test.wav {len(audio) / 44100} seconds")


if __name__ == "__main__":
    main()
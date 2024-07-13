import streamlit as st
from client import Client

st.title("한국숫자 연습")


# Function to generate a random number based on a specified digit
def get_number(digit):
    response = db.get("get_number/", params={"digit": digit})
    return response["current_number"]


# Function to generate the Korean number for display
def get_display_knum(number):
    response = db.get("display_knum/", params={"input_number": number})
    return response["display_knum"]


# Function to generate audio
def get_audio_path(number):
    response = db.post("play_audios", json={"input_number": number})
    return response.strip('"')


# Initialize the client
db = Client()

# Create a text input box
digit = st.number_input("자리", min_value=1, max_value=5, value=4)

if "action1" not in st.session_state:
    st.session_state.action1 = False

# Display button for generating number, Korean word, and audio
if st.button("TRY IT"):
    st.session_state.action1 = True
    # Generate a random number based on a specified digit (e.g., for digit=2, generating 21. )
    st.session_state.number = get_number(digit)

    # Generate the Korean number for display (e.g., 이십일)
    st.session_state.display_knum = get_display_knum(st.session_state.number)

    # Generate the audio (.mp3 file)
    st.session_state.audio_path = get_audio_path(st.session_state.number)

# Check if the TRY IT button was pressed
# Keep the random number showing on the page
if st.session_state.action1:
    # Display the generated random number on UI (e.g., 21)
    st.title(f"{st.session_state.number}")
    # Allow the user to play the audio
    st.audio(st.session_state.audio_path)
    # Display the Korean word of the generated random number on UI (e.g., 21)
    if st.button("Answer"):
        st.write(f"{st.session_state.display_knum}")

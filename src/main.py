import streamlit as st
from client import Client

st.title("한국숫자 연습")


# Function to generate a random number based on a specified digit
def get_number(digit: int) -> str:
    response = db.get("get_number", params={"digit": digit})
    return response["current_number"]


# Function to generate the Korean number for display
def get_display_knum(number: int):
    response = db.get("display_knum", params={"input_number": number})
    return response["display_knum"]


# Function to fetch a random date
def get_date() -> str:
    response = db.get("get_date")
    return response["date"]


# Function to generate audio
def get_audio_path(input_text: str) -> str:
    if isinstance(input_text, int):
        input_text = str(input_text) + "원입니다"

    response = db.post("play_audios", json={"input_text": input_text})
    return response.strip('"')


# Initialize the client
db = Client()


# Page functions:
# The page for korean number:
def number_page():
    # Create a text input box
    digit = st.number_input("자리", min_value=4, max_value=6, value=4)

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


# The page for korean date:
def date_page():
    if "action2" not in st.session_state:
        st.session_state.action2 = False

    # Display button for generating number, Korean word, and audio
    if st.button("TRY IT"):
        st.session_state.action2 = True
        # Generate a random date e.g., 4월24일
        st.session_state.date = get_date()

        # Generate the audio (.mp3 file)
        st.session_state.audio_path = get_audio_path(st.session_state.date)

    if st.session_state.action2:
        # Display the generated random number on UI (e.g., 4월24일)
        st.title(f"{st.session_state.date}")

        # Allow the user to play the audio
        st.audio(st.session_state.audio_path)


# Page dictionary
pages = {"Number": number_page, "Date": date_page}

# Sidebar with a drop-down list for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()

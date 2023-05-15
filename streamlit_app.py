import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
from gpt4free import you


def get_answer(question: str) -> str:
    # Set cloudflare clearance cookie and get answer from GPT-4 model
    try:
        result = you.Completion.create(prompt=question)

        return result.text

    except Exception as e:
        # Return error message if an exception occurs
        return (
            f'An error occurred: {e}. Please make sure you are using a valid cloudflare clearance token and user agent.'
        )


# Set page configuration and add header
st.set_page_config(
    page_title="SimpleGPT",
    initial_sidebar_state="expanded",
    page_icon="",
    menu_items={
        'About': "### gptfree GUI",
    },
)
st.header('SimpleGPT')

# Add text area for user input and button to get answer
question_text_area = st.text_area('🤖 Ask Any Question :', placeholder='Explain quantum computing in 50 words')
if st.button('Chat'):
    answer = get_answer(question_text_area)
    escaped = answer.encode('utf-8').decode('unicode-escape')
    # Display answer
    st.caption("Answer :")
    st.markdown(escaped)

# Hide Streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

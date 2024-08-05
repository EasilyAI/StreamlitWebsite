import streamlit as st
import time
import re

def type_text_gpt_style(text, output_container, output_box_class, delay=0.025, type_effect=True):
    # output_container = st.empty()
    result = ""
    if type_effect:
        for letter in text:
            if letter == "\n":
                result += "<br>"
            result += letter
            output_container.markdown(f'<div class={output_box_class}>{result}</div>', unsafe_allow_html=True)
            time.sleep(delay)
    else:
        output_container.markdown(f'<div class={output_box_class}>{text}</div>', unsafe_allow_html=True)
    return result

def run_process_spinner(duration=1.5, message = 'Processing...'):
    with st.spinner(message):
        time.sleep(duration)

def wait(duration=1):
    time.sleep(duration)

def is_input_valid(user_input, placeholder):
    if user_input and user_input != placeholder:
        return True
    return False

# Find more emojis here: 
#    https://www.webfx.com/tools/emoji-cheat-sheet/
#    https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

import streamlit as st
import project_path

from Agent import process_user_input
from webUtils.emailUtils import send_email_smtp, validate_email,get_recipient_email_contacts
from webUtils.pageConfig import load_default_page_config, add_page_titles
from webUtils.textUtils import (is_input_valid, type_text_gpt_style,run_process_spinner,wait)

# -------- PAGE TEXT VARIABLES ---------
SPARKLES_EMOJI = ":sparkles:" #:spider_web:
HEAD_TITLE_TEXT = f"{SPARKLES_EMOJI} Save time, use AI"
HEAD_SUB_TITLE_TEXT = "AI solutions for businesses"
HEAD_DESCRIPTION_TEXT = """What solutions? We can do a lot of things...<br>
    <ol> 
        <li>Shoot us a couple of lines on your needs or type of business</li>
        <li>Our <b>AI will do the rest</b></li>
    <ol>"""

SEARCH_BAR_INSTRUCTION_TEXT = "Enter the kind of solution you are looking for"
SEARCH_BAR_DEFAULT_TEXT = "You can also write about your business, or just leave it empty"
SEARCH_BAR_HELPER_TEXT = "Write us what is your "

CONTACT_EMAIL_PLACEHOLDER = "Sounds intresting? leave us your email and we'll be in touch"


# -------- LOAD PAGE DEFAULT CONFIG & STYLE -------
load_default_page_config()


# -------- PAGE TITLE --------
add_page_titles(HEAD_TITLE_TEXT,HEAD_SUB_TITLE_TEXT,HEAD_DESCRIPTION_TEXT)


# -------- INITIATE SESSION STATE -----------
for state in ["user_input","result"]:
    if state not in st.session_state:
        st.session_state[state] = ""

for state in ["should_use_type_effect"]:
    if state not in st.session_state:
        st.session_state[state] = True

for state in ["result_printed","submit_clicked", "clear_form", "run_gpt_clicked"]:
    if state not in st.session_state:
        st.session_state[state] = False

if st.session_state["clear_form"]:
    st.session_state["result"] = ""  # Clear result from session state
    st.session_state["user_input"] = "" # Clear user input box
    st.session_state["result_printed"] = False  
    st.session_state["clear_form"] = False
    st.rerun()

# -------- SEARCH BAR AND BUTTONS -----------
with st.container():
    search_bar, run_gpt_button, clear_button = st.columns([6, 1, 1])
    
    with search_bar:
        user_input = st.text_input(label = SEARCH_BAR_INSTRUCTION_TEXT, 
                                   placeholder = SEARCH_BAR_DEFAULT_TEXT, 
                                   help = SEARCH_BAR_HELPER_TEXT,
                                   label_visibility="visible",
                                   key='user_input')
    
    with run_gpt_button:
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        run_gpt = st.button("Run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with clear_button:
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        clear = st.button("Clear")
        st.markdown('</div>', unsafe_allow_html=True)

    if run_gpt:
        st.session_state["run_gpt_clicked"] = True
        st.session_state["should_use_type_effect"] = True
    
    if clear:
        st.session_state['clear_form'] = True

    output_container = st.empty()
    if st.session_state["run_gpt_clicked"] or st.session_state["result_printed"]:
        if st.session_state["run_gpt_clicked"]:
            run_process_spinner(duration=1.5)

        if is_input_valid(st.session_state["user_input"], SEARCH_BAR_DEFAULT_TEXT):
            result = process_user_input(st.session_state["user_input"], test_mode= False)         
            st.session_state["result"] = result            
            
            type_text_gpt_style(text = st.session_state["result"], output_container=output_container, output_box_class = 'answer-box', type_effect=st.session_state["should_use_type_effect"])
            st.session_state["result_printed"] = True
            st.session_state["run_gpt_clicked"] = False
            st.session_state["should_use_type_effect"] = False
        
        else:
            st.write("Please enter a valid search term.")

    
    if st.session_state["result_printed"]:
        wait(1)
        col1, col2 = st.columns([3, 1])
            
        with col1:    
            st.markdown('<div class="contact-input-container">', unsafe_allow_html=True)
            email = st.text_input(label='Email',placeholder=CONTACT_EMAIL_PLACEHOLDER, key='email_input', label_visibility='hidden')
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="contact-button-container">', unsafe_allow_html=True)
            submit = st.button("Submit")
            st.markdown('</div>', unsafe_allow_html=True)

        
        if submit:
            st.session_state["submit_clicked"] = True
        
     
    if st.session_state["submit_clicked"] and "email_input" in st.session_state:
        if not st.session_state["email_input"] or not validate_email(st.session_state["email_input"]):
            st.error('Please enter a valid email address.')
        else:
            is_email_sent = send_email_smtp(subject=f"New contact request submitted - {email}", body_dict = dict(st.session_state), to_email=get_recipient_email_contacts())
            print("email sent: ",is_email_sent)

            if is_email_sent:                 
                st.success('Request submitted successfully! 🤓')
                st.session_state["submit_clicked"] = False
            else:
                st.error('Error submitting contact details')
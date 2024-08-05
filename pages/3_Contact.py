import project_path
from webUtils.pageConfig import load_default_page_config
from webUtils.emailUtils import send_email_smtp, validate_email,get_recipient_email_contacts
import streamlit as st


# -------- LOAD PAGE CONFIG & STYLE -------
load_default_page_config()


# -------- INITIATE PAGE VARIABLES -------
for user_input in ['name_input','phone_input','email_input']:
    if user_input not in st.session_state:
        st.session_state[user_input] = ''

if 'clear_form' not in st.session_state:
    st.session_state.clear_form = False

if st.session_state.clear_form:
    st.session_state.name_input = ''
    st.session_state.phone_input = ''
    st.session_state.email_input = ''


# -------- ADD CONTENT TO PAGE -------
st.title('Contact Form')
with st.form(key='contact_form'):
    name = st.text_input(label='Name',placeholder="Optional", key='name_input')
    phone = st.text_input(label = 'Phone Number', placeholder="Optional", key='phone_input')
    email = st.text_input(label ='Email', placeholder="We won't spam you 🫡", key='email_input')
    
    col1, col2 = st.columns([1, 1])  # Create two columns with equal width

    with col1:
        submit_button = st.form_submit_button('Submit', use_container_width=True)
    with col2:
        clear_button = st.form_submit_button('Clear Form', use_container_width=True)


# -------- BUTTONS FUNCTIONALITY -------
    if submit_button:
        if not email or not validate_email(email):
            st.error('Please enter a valid email address.')
        else:
            st.session_state.name = name
            st.session_state.phone = phone
            st.session_state.email = email        

            data = {
                'name': name,
                'phone': phone,
                'email': email
            }
            
            is_email_sent = send_email_smtp(subject=f"New contact request submitted - {email}", body_dict = data, to_email=get_recipient_email_contacts())
            
            if is_email_sent:                 
                st.success('Form submitted successfully! 🤓')
            else:
                st.error('Error submitting form')
        
        st.session_state.clear_form = False
            
    if clear_button:
        st.session_state.clear_form = True
        st.rerun()
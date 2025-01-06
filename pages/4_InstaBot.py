import streamlit as st

from webUtils.pageConfig import load_default_page_config

# -------- LOAD PAGE CONFIG & STYLE -------
load_default_page_config(layout="wide")

st.title("Sign up for the InstaBot service")

st.markdown(
    '<a href="https://www.instagram.com/oauth/authorize?enable_fb_login=0&force_authentication=1&client_id=1585703655622941&redirect_uri=https://rw7uq0spp4.execute-api.us-east-1.amazonaws.com/business-auth&response_type=code&scope=instagram_business_basic%2Cinstagram_business_manage_messages%2Cinstagram_business_manage_comments%2Cinstagram_business_content_publish" target="_blank" style="text-decoration:none;">'
    # '<a href="https://rw7uq0spp4.execute-api.us-east-1.amazonaws.com/business-auth">'
    '<button style="background-color:#4CAF50; color:white; border:none; padding:10px; font-size:16px; cursor:pointer;">'
    'Register'
    '</button>'
    '</a>',
    unsafe_allow_html=True
)
# st.markdown(
#     '<a href="https://rw7uq0spp4.execute-api.us-east-1.amazonaws.com/business-deauth">'
#     '<button style="background-color:#4CAF50; color:white; border:none; padding:10px; font-size:16px; cursor:pointer;">'
#     'Deauthorize'
#     '</button>'
#     '</a>',
#     unsafe_allow_html=True
# )
# st.markdown(
#     '<a href="https://rw7uq0spp4.execute-api.us-east-1.amazonaws.com/data-deletion">'
#     '<button style="background-color:#4CAF50; color:white; border:none; padding:10px; font-size:16px; cursor:pointer;">'
#     'Data Deletion'
#     '</button>'
#     '</a>',
#     unsafe_allow_html=True
# )
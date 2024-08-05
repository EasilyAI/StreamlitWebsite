import streamlit as st
from streamlitWeb.webUtils.stylingUtils import load_css
import yaml
import project_path
    
def load_default_page_config(page_title="AI solutions", 
                             page_icon=":sparkles:", 
                             layout= "centered",
                             css_file = "styles/style.css", 
                             backround_img_path = "styles/backround.jpg"):
    
    st.set_page_config(page_title=page_title, page_icon=page_icon, layout= layout)
    load_css(css_file = css_file, 
         backround_img_path = backround_img_path)

def add_page_titles(head_title:str, head_subtitle:str = None, head_description_text:str = None):    
    with st.container():
        st.title(head_title)
        if head_subtitle: 
            st.subheader(head_subtitle)
        if head_description_text:
            st.markdown(f'<div class="description-box">{head_description_text}</div>', unsafe_allow_html=True)

        # st.write("###")

def load_content_from_yaml(file_path):
    with open(file_path, 'r') as file:
        content = yaml.safe_load(file)
    return content

def add_centered_element(element_type, text, css_class="centered"):
    if element_type in ["p","ul"]:
        return st.markdown(f"""
        <{element_type} class="{css_class} paragraph">{text}</{element_type}>""",unsafe_allow_html=True)
    else:
        return st.markdown(f"""
        <{element_type} class={css_class} {"paragrapgh" if element_type=="p" else ""}>{text}</{element_type}>""",unsafe_allow_html=True)
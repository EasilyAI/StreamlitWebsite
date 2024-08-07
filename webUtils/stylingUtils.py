import base64
import streamlit as st

def load_css(css_file, backround_img_path = "styles/backround.jpg"):
    background_css = generate_backround_image_css(backround_img_path = backround_img_path)
    with open(css_file) as f:
        page_css = f.read()
        style_content = background_css+page_css
        st.markdown(f"<style>{style_content}</style>", unsafe_allow_html=True)

def generate_backround_image_css(
        backround_img_path = "styles/backround.jpg",
        backround_img_type = "jpg",
        data_testid = "stApp",
        background_size = "cover",
        background_repeat = "no-repeat",
        background_position = "center"):    
    img_object_base64 = get_img_as_base64(backround_img_path)
    page_background_style = f"""
    /* PAGE BACKROUND */
        [data-testid={data_testid}] {{
        background-image: url("data:img/{backround_img_type};base64,{img_object_base64}");
        background-size: {background_size}; 
        background-repeat: {background_repeat}; 
        background-position: {background_position};
        }}"""
    return page_background_style

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_png_img_inlined_in_text(file_path, output_width=140):
    base_64_img = get_img_as_base64(file_path)
    return f"<img src='data:image/png;base64,{base_64_img}' width='{output_width}'>"


# Find more emojis here: 
#    https://www.webfx.com/tools/emoji-cheat-sheet/
#    https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

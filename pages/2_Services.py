from webUtils.pageConfig import load_default_page_config, add_centered_element,load_content_from_yaml

# -------- LOAD PAGE CONFIG & STYLE -------
load_default_page_config(layout="wide")


# -------- LOAD PAGE CONTENT FROM YAML --------
content = load_content_from_yaml('content/services.yml')


# -------- ADD CENTERED CONTENT TO PAGE --------
for element in content['content']:
    add_centered_element(element_type = element['element_type'],text=element['text'])
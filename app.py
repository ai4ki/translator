import deepl
import os
import streamlit as st

DEEPL_API_KEY = os.environ["DEEPL_API_KEY"]

translator = deepl.Translator(DEEPL_API_KEY)

st.set_page_config(layout="wide",
                   page_title="Translator",
                   page_icon=":rocket:",
                   menu_items={"About": "None."})

cols = st.columns([1, 1], gap="large")

with cols[0]:
    st.markdown("### English text")
    text_to_translate = st.text_area(label="Text to translate",
                                     value="",
                                     height=500,
                                     placeholder="Enter some text",
                                     label_visibility="collapsed")
    translate = st.button("Translate")

if translate:
    result = translator.translate_text(text_to_translate, target_lang="DE")

    with cols[1]:
        st.markdown("### Deutsche Übersetzung")
        st.text_area(label="translated text",
                     value=result,
                     height=500,
                     placeholder="Deine Übersetzung",
                     label_visibility="collapsed")
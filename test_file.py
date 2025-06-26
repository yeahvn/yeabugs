import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import streamlit as st
import easyocr
import requests
from pathlib import Path
from io import BytesIO

def ocr_read_text(image_bytes):
    reader = easyocr.Reader(['en', 'ko'], verbose=False)
    results = reader.readtext(image_bytes)
    return [res[1] for res in results]

def translate_text(text, src_lang='en', tgt_lang='ko'):
    url = "https://api.mymemory.translated.net/get"
    params = {
        'q': text,
        'langpair': f'{src_lang}|{tgt_lang}'
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'responseData' in data and 'translatedText' in data['responseData']:
        return data['responseData']['translatedText']
    return None

st.title("OCR + MyMemory 번역 웹앱")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    img_bytes = uploaded_file.read()
    st.image(img_bytes, caption="업로드된 이미지", use_column_width=True)
    
    with st.spinner("텍스트 인식 중..."):
        texts = ocr_read_text(img_bytes)
    
    if texts:
        st.subheader("OCR 인식된 텍스트")
        for t in texts:
            st.write(t)
        
        st.subheader("번역 결과 (영어 → 한국어)")
        for t in texts:
            translated = translate_text(t, src_lang='en', tgt_lang='ko')
            st.write(f"{t} → {translated}")
    else:
        st.write("텍스트를 인식하지 못했습니다.")

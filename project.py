import streamlit as st
import pandas as pd
import docx
import os

# 번역 기능
def get_translation(name, language):
  
    if language == 'English':
        return f"The name in English: {name}"
    elif language == 'Korean':
        return f"The name in Korean: {name}"
    else:
        return "Invalid language selection."

# 액셀 파일 읽기 기능
def read_excel(file):
    df = pd.read_excel(file)
    return df

# 문서형식 파일 읽기 기능
def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# txt파일 읽기 기능
def read_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

#log file 읽기 기능
def read_log(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def main():
    st.title("보안성 검사를 위한 데이터 제공")

    # 사용자 입력
    name = st.text_input("이름을 입력하세요:")

    # 언어 선택
    language_options = ['English', 'Korean']
    language = st.selectbox("Select language:", language_options)

    # 파일 업로드
    uploaded_file = st.file_uploader("Upload a file", type=['xlsx', 'docx', 'db', 'txt', 'log'])

    if uploaded_file is not None:
        # 파일 유형 보여주기
        st.write("File type:", uploaded_file.type)

        #파일 타입에 기초하여 읽고 보여주기
        if uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':  # 엑셀 파일
            df = read_excel(uploaded_file)
            st.write("Data from Excel file:")
            st.write(df)

        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':  # 워드 문서
            text = read_docx(uploaded_file)
            st.write("Text from Word document:")
            st.write(text)

        elif uploaded_file.type == 'text/plain':  # 텍스트 파일
            text = read_txt(uploaded_file)
            st.write("Text from Text file:")
            st.write(text)

        elif uploaded_file.type == 'text/csv':  # 로그 파일
            lines = read_log(uploaded_file)
            st.write("Lines from Log file:")
            st.write(lines)



        else:
            st.write("Unsupported file type")

        # 번역, 결과 보여주기
        if name:
            result = get_translation(name, language)
            st.write(result)

if __name__ == "__main__":
    main()
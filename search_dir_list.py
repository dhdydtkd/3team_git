import streamlit as st
import os

def search_dir_modif():
    st.title("디렉토리 내 파일검사")

    dir_path = 'static/search_dir_list.txt'
    st.subheader('확인할 디렉토리 리스트')
    origin_dir_list = ''
    delete_dir_flag = False
    delete_dir_name = ''

    add_dir_name = st.text_input("추가할 경로를 입력하세요")
    if st.button(f'경로 추가') : 
        print(add_dir_name)
        with open(dir_path,'a', encoding='utf-8') as f:
            f.write(f'{add_dir_name}\n')
            st.success('추가 완료')

    with open(dir_path,'r', encoding='utf-8') as f:
        origin_dir_list = f.read()
    with open(dir_path,'r', encoding='utf-8') as f:
        for dir_name in f.readlines() : 
            new_line = os.path.join(dir_name).replace("\n", "")
            if st.button(f'[{new_line}] 삭제'):
                print(f'[{new_line}]')
                delete_dir_flag = True
                delete_dir_name = new_line

    if delete_dir_flag:
        with open(dir_path,'w', encoding='utf-8') as delete_f:
            if origin_dir_list.replace(f'{delete_dir_name}\n', ''):
                delete_f.write(origin_dir_list.replace(f'{delete_dir_name}\n', ''))
            st.success('삭제 완료')

#streamlit run e:\3team_project\main.py
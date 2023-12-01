
import search_schedule as sschedule
import streamlit as st
import search_dir_list as fs
import dir_warning_find as dwf
import info_safe_warning_result as iswr
import openpyxl
if __name__ == "__main__":

    # sschedule.job2()
    #sschedule.search_schedule()

    fs.search_dir_modif()

    st.title("보안성 검사를 위한 데이터 제공")

    # 사용자 입력

    dir_path = st.text_input("탐색할 디렉토리를 입력해주세요")
    if st.button('디렉토리 수동 검사') : 
        dwf.dir_warning_check(dir_path)
        #결과 뿌려줘야함

    # 파일 업로드
    uploaded_file = st.file_uploader("파일 검사", type=['xlsx', 'txt', 'log'])
    #print(f'uploaded_file : [{uploaded_file}]')
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.xlsx'):
            print(f'uploaded_file : [{iswr.info_safe_warning_result(f'member_data/{uploaded_file.name}')}]')
        if uploaded_file.name.endswith('.txt'):
            print(f'uploaded_file : [{uploaded_file}]')
        if uploaded_file.name.endswith('.log'):
            print(f'uploaded_file : [{uploaded_file}]')

    
            
    
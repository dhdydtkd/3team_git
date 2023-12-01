
import search_schedule as sschedule
import streamlit as st
import search_dir_list as fs
import dir_warning_find as dwf
import info_safe_warning_result as iswr
import detec_file as df
import smtp_slack_check as sscheck

if __name__ == "__main__":

    # sschedule.job2()
    #sschedule.search_schedule()

    fs.search_dir_modif()

    st.title("보안성 검사를 위한 데이터 제공")

    # 사용자 입력

    dir_path = st.text_input("탐색할 디렉토리를 입력해주세요")
    warning_file_list = []
    if st.button('디렉토리 수동 검사') : 
        warning_file_list = dwf.dir_warning_check(dir_path)
        if warning_file_list : 
            for file in warning_file_list:
                st.write(file)
            # df.zip_test(warning_file_list)
            st.warning('현재 압축기능이 개발되지 않았습니다.')
            # st.success('압축 및 다운로드 완료')
        else : 
            st.warning('경로를 찾을 수 없습니다.')
        #결과 뿌려줘야함
    # if st.button('오류가 있는 파일 zip으로 다운로드') : 
    #     print(f'warning_file_list : {warning_file_list}')
    #     if warning_file_list:
    #         df.zip_test(warning_file_list)
    #         st.success('압축 및 다운로드 완료')
    #     else:
    #         st.warning('압축 및 다운로드 할 수 있는 파일이 존재하지 않습니다.')
    # 파일 업로드
    uploaded_file = st.file_uploader("파일 검사", type=['xlsx', 'txt', 'log'])
    #print(f'uploaded_file : [{uploaded_file}]')
    warning_file_list = []
    dir_path_member_data = 'member_data'
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.txt') or uploaded_file.name.endswith('.log'):
            info_warning_line, safe_warning_line = iswr.info_safe_warning_result(f'{dir_path_member_data}/{uploaded_file.name}')
            sscheck.check(f'{dir_path_member_data}/{uploaded_file.name}')

            check = dwf.warning_text_print(info_warning_line, safe_warning_line)
            if check:
                if st.button('검사한 파일 마스킹 하기'):
                    if uploaded_file.name.endswith('.txt') or uploaded_file.name.endswith('.log'):
                        df.detec_file(f'{dir_path_member_data}/{uploaded_file.name}')
                        st.success('해당 파일의 마스킹이 완료되었습니다.')
                    elif uploaded_file.name.endswith('.xlsx'):
                        df.detec_xlsx_file(f'{dir_path_member_data}',f'{dir_path_member_data}/{uploaded_file.name}', uploaded_file.name)
                        st.success('해당 파일의 마스킹이 완료되었습니다.')
                    else:
                        st.warning('txt, log, xlsx 파일만 업로드 해주세요.')
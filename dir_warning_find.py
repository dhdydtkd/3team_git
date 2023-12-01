
import os
import info_safe_warning_result as iswr
import streamlit as st

def warning_text_print(info_warning_line,safe_warning_line):
    if info_warning_line and safe_warning_line:
        st.warning(f'다음과 같은 라인에 info 문제가 있습니다->{info_warning_line}')
        st.warning(f'다음과 같은 라인에 safe 문제가 있습니다->{safe_warning_line}')
        return True
    elif info_warning_line : 
        st.warning(f'다음과 같은 라인에 info 문제가 있습니다->{info_warning_line}')
        return True
    elif safe_warning_line : 
        st.warning(f'다음과 같은 라인에 safe 문제가 있습니다->{safe_warning_line}')
        return True
    else : 
        st.success('문제가 없는 파일 입니다.')
        return False

def dir_warning_check(dir_path):
    # 보안 검사에 통과하지 못한 파일 넣는 리스트

    #전체파일 리스트
    detection_Pass_File = []
    detection_Nonpass_File = []

    warning_file_list = []
    if os.path.isdir(dir_path):
        all_Files = os.listdir(dir_path)
        
        print(f"=====전체 파일 {all_Files}=====")
        # 전체 파일 검사

        for file_Name in all_Files:
            extand = os.path.splitext(file_Name)[1]
            if(extand == ".txt" or extand == ".txt" or extand == ".xlsx" ):
                info_warning_line, safe_warning_line = iswr.info_safe_warning_result(f'{dir_path}/{file_Name}')
                if info_warning_line and safe_warning_line:
                    warning_file_list.append([f'파일 이름 : {file_Name}', f'다음과 같은 라인에 info 문제가 있습니다->{info_warning_line}', f'다음과 같은 라인에 safe 문제가 있습니다->{safe_warning_line}'])
                elif info_warning_line : 
                    warning_file_list.append([f'파일 이름 : {file_Name}', f'다음과 같은 라인에 info 문제가 있습니다->{info_warning_line}'])
                elif safe_warning_line : 
                    warning_file_list.append([f'파일 이름 : {file_Name}', f'다음과 같은 라인에 safe 문제가 있습니다->{safe_warning_line}'])
        return warning_file_list
    else:
        return

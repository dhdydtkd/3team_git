import streamlit as st
import os
import re



# 확장자 확인 필요..
# 확장자를 확인해서 txt 바로 확인 가능한지, 변환 후 진행해야되는 것들 확인
def text_check(dir_path):
    # 보안 검사에 통과하지 못한 파일 넣는 리스트
    # 바로 마스킹 하면 필요 없을듯.
    detection_Pass_File = set()
    detection_Nonpass_File = set()

    #전체파일 리스트
    all_Files = os.listdir(dir_path)
    print(f"=====전체 파일 {all_Files}=====")
    # 전체 파일 검사
    for file_Name in all_Files:
        file_Path = os.path.join(dir_path,file_Name)
        with open(file_Path, 'r',encoding='utf-8') as f:
            
            # 파일에서 가져온 문자열
            lines = f.readlines()
            # print(f"{lines}\n")
            # 한줄씩 검사
            for num, line in enumerate(lines):
                #검출 시 마스킹 + detection_Nonpass_File에 파일이름 추가
                matches = re.findall(r"[\w\.-]+@[\w\.-]+", line)
                if matches:
                    print(f"검출 {matches} fileName : {file_Name}")
                    #이름 중복 방지
                    detection_Nonpass_File.add(file_Name)
                else :
                    print(f"미검출")
                    detection_Pass_File.add(file_Name)
                            
    print(f"검출 파일{detection_Nonpass_File} 미검출{detection_Pass_File}")

if __name__ == '__main__':
     # 여기에 streamit text.input에 값 넣기
    dir_path = "dummy"
    text_check(dir_path)

        
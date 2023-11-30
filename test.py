import streamlit as st
import os
import re
from docx import Document

# 전역 변수로 작성, 함수마다 이름 확인
detection_Pass_File = set()
detection_Nonpass_File = set()
#폴더에 어떤 확장자 있는지 확인

# 확장자 확인 필요..
# 확장자를 확인해서 txt 바로 확인 가능한지, 변환 후 진행해야되는 것들 확인
def text_check(dir_path):
    # 보안 검사에 통과하지 못한 파일 넣는 리스트
    # 바로 마스킹 하면 필요 없을듯.
    # 1. 확장자 확인 2. 확장자 별 체크 3. 마스킹

    
    #전체파일 리스트
    all_Files = os.listdir(dir_path)
    
    print(f"=====전체 파일 {all_Files}=====")
    # 전체 파일 검사
    for file_Name in all_Files:
        print(file_Name)
        if(os.path.splitext(file_Name)[1] == ".docx"):
            docx_checker(file_Name)
        elif(os.path.splitext(file_Name)[1] == ".txt" or ".log" or ".py"):
            txt_checker(file_Name)
        elif(os.path.splitext(file_Name)[1] == ".elsx"):
            print()
        

        
#아직 안됨
def docx_checker(file_Name):
    doc = Document('D:\\team_3\\dummy\\templates.docx')
    print(11)
    # 이름 추출을 위한 정규식 패턴
    name_pattern = re.compile(r'\b[A-Za-z]+(?: [A-Za-z]+)?\b')

    # 이메일 추출을 위한 정규식 패턴
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # 전화번호 추출을 위한 정규식 패턴
    phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')
    def mask_name(match):
        name = match.group(0)
        # 이름에서 아이디 부분만 추출하여 마스킹 (예: John Doe -> J*** D**)
        masked_name = ' '.join([name[0] + '*' * (len(part) - 1) if part.isalpha() else part for part in name.split()])
        return masked_name
    
    for paragraph in doc.paragraphs:
        print (paragraph.text)
        name_pattern.sub(mask_name,(paragraph.text))
    
    doc.save('templates')


# txt, log, py 확인
def txt_checker(file_Name):
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
                with open(file_Path,'w',encoding='utf-8') as ex:
                    # re.sub는 치환해주는 메소드
                    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
                    ex.write(email_pattern.sub(mask_email_id, line))
                    print(email_pattern)
                # print(f"검출 {matches} fileName : {file_Name}")
                #이름 중복 방지
                detection_Nonpass_File.add(file_Name)
            else :
                # print(f"미검출")
                detection_Pass_File.add(file_Name)
                        
    print(f"검출 파일{detection_Nonpass_File} 미검출{detection_Pass_File}")

# email 가림
def mask_email_id(match):
    email = match.group(0)
    # 이메일 주소에서 아이디 부분만 추출하여 가리기 (예: user@example.com -> u****@example.com)
    username, domain = email.split('@')
    masked_username = username[0] + '*' * (len(username) - 1)
    masked_email = masked_username + '@' + domain
    return masked_email

if __name__ == '__main__':
     # 여기에 streamlit text.input에 값 넣기
    dir_path = "dummy"
    text_check(dir_path)
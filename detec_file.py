
import re
import os
import zipfile
from datetime import datetime
# 검출 여부 확인 set 사용해 중복제거


def detec_file_list(detection_Nonpass_Files):
    for file_addr in detection_Nonpass_Files:
        print(file_addr)
        detec_file_Path = os.path.join(file_addr)
        with open(detec_file_Path, 'r',encoding='utf-8') as f:
            # 파일에서 가져온 문자열
            detec_lines = f.readlines()
            # print(f"{lines}\n")
            # 한줄씩 검사
        for num, line in enumerate(detec_lines):
                #검출 시 마스킹 + detection_Nonpass_File에 파일이름 추가
                matches = re.findall(r"[\w\.-]+@[\w\.-]+", line)
                matches_Phone = re.findall(r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b',line)
                if matches:
                    with open(detec_file_Path,'w',encoding='utf-8') as ex:
                        # re.sub는 치환해주는 메소드
                        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
                        phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b')
                        detec_lines[num] = email_pattern.sub(mask_email_id, line)
                        detec_lines[num] = phone_pattern.sub(mask_phone,line)
                        # 수정할때마다 넣어줌
                        ex.writelines(detec_lines)
                elif matches_Phone:
                    with open(detec_file_Path,'w',encoding='utf-8') as ex:
                        phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b')
                        detec_lines[num] = phone_pattern.sub(mask_phone,line)
                        # 수정할때마다 넣어줌
                        ex.writelines(detec_lines)

def detec_file(file_name):
    detec_file_Path = os.path.join(file_name)
    with open(detec_file_Path, 'r',encoding='utf-8') as f:
        # 파일에서 가져온 문자열
        detec_lines = f.readlines()
        # print(f"{lines}\n")
        # 한줄씩 검사
    for num, line in enumerate(detec_lines):
            #검출 시 마스킹 + detection_Nonpass_File에 파일이름 추가
            matches = re.findall(r"[\w\.-]+@[\w\.-]+", line)
            matches_Phone = re.findall(r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b',line)
            if matches:
                with open(detec_file_Path,'w',encoding='utf-8') as ex:
                    # re.sub는 치환해주는 메소드
                    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
                    phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b')
                    detec_lines[num] = email_pattern.sub(mask_email_id, line)
                    detec_lines[num] = phone_pattern.sub(mask_phone,line)
                    # 수정할때마다 넣어줌
                    ex.writelines(detec_lines)
            elif matches_Phone:
                with open(detec_file_Path,'w',encoding='utf-8') as ex:
                    phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b')
                    detec_lines[num] = phone_pattern.sub(mask_phone,line)
                    # 수정할때마다 넣어줌
                    ex.writelines(detec_lines)
            
# 파일 압축 
def zip_test(detection_Nonpass_File_list):
    print('zip_test')
    if detection_Nonpass_File_list:
        zip_file = zipfile.ZipFile(f"warning_zip/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}detection.zip", "w")
        for root, dirs, files in os.walk(detection_Nonpass_File_list):
            for file in files:
                print(f'{file} {detection_Nonpass_File_list}')
                if file in detection_Nonpass_File_list:
                    print(file)
                    zip_file.write(os.path.join(root,file))

    zip_file.close()

def mask_phone(match):
    phone = match.group(0)
    num1,num2,num3 = phone.split('-')
    if(len(num2) == 3):
        num2 = "***"
    elif(len(num2) == 4):
        num2 = "****"
    masked_phone = num1 +'-'+ num2 +'-'+ num3
    print(masked_phone)
    return masked_phone

# email 마스킹
def mask_email_id(match):
    email = match.group(0)
    # 이메일 주소에서 아이디 부분만 추출하여 가리기 (예: user@example.com -> u****@example.com)
    username, domain = email.split('@')
    masked_username = username[0] + '*' * (len(username) - 1)
    masked_email = masked_username + '@' + domain
    return masked_email

    
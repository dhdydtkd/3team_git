from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os
import re
import pandas as pd
import openpyxl

# Slack channel to send the message to

def sendSlackWebhook(file_path):
    SLACK_API_TOKEN = 'xoxb-6262233246663-6279292640596-VkFB8dNYcX4E8QS3GXKkzUzW'
    client = WebClient(token=SLACK_API_TOKEN)
    try:
        response = client.files_upload(
            channels="#프로젝트",
            file=file_path,
            title=f"위험정보 포함 파일입니다."
        )
        print(f"위험 정보 정상적으로 보냄")
    except SlackApiError as e:
        print(f"오류 발생 {e}")

def sendsmtp(file_name,error_report):        
   
    SECRET_ID = 'skyujin4039'
    SECRET_PASS = '12341234!'

    smtp= smtplib.SMTP('smtp.naver.com',587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(SECRET_ID,SECRET_PASS)

    myemail = 'skyujin4039@naver.com'
    youremail = 'skyujin4039@naver.com'

    msg = MIMEMultipart()

    msg['Subject'] ="위험정보 포함 파일 입니다."
    msg['From'] = myemail
    msg['To'] = youremail
    if error_report[0] == 1:
        text =f"""
            목록 줄에 개인정보 위험요소가 포함되어 있습니다.\n
            {error_report[1]}
        """
    elif error_report[0] == 2:
        text =f"""
            목록 줄의 IP가 현재 불안정한 상태입니다.\n
            {error_report[1]}
        """
    elif error_report[0] == 3:
        text =f"""
            목록 줄에 개인정보 위험요소가 포함되어 있습니다.\n
            {error_report[1]}\n
            목록 줄의 IP가 현재 불안정한 상태입니다.\n
            {error_report[2]}
        """
    else:
        text =f"""
            파일 전송 입니다.
        """   
    contentPart = MIMEText(text)
    msg.attach(contentPart)

    
    with open (file_name,'rb') as f:
        etc_part = MIMEApplication(f.read())
        etc_part.add_header('Content-Disposition','attachment', filename=file_name)
        msg.attach(etc_part)
            
    smtp.sendmail(myemail,youremail,msg.as_string())
    smtp.quit()

def check(file_path,ID_PASS):
    file_name = file_path
    
    info_warning_line = []
    safe_warning_line = []

    info_warning = False
    safe_warning = False
    phone_pattern = r'\d{3}-\d{3,4}-\d{4}'
    email_pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"
    

    if file_name.endswitch('.xlsx'):
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active

        for index, row in enumerate(sheet.iter_rows()):
            for i, cell in enumerate(row[:7]):
                if re.findall(phone_pattern,str(cell.value)):
                    info_warning = True
                elif re.findall(email_pattern,str(cell.value)):
                    info_warning = True
                if i==6 and cell.value==False : 
                    safe_warning = True
            if info_warning:
                info_warning_line.append(index)
            if safe_warning:
                safe_warning_line.append(index)
            info_warning = False
            safe_warning = False

    #print(f'info_warning_line : {info_warning_line}');
    #print(f'safe_warning_line : {safe_warning_line}');

    if file_name.endswith('.txt'):
        info_warning = False
        safe_warning = False
        with open(f'{file_name}','r',encoding='utf-8') as f:
            lines = f.readlines()
            head_info=list(map(str,lines[0].split('|')))
            info_warning = False
            for index, line in enumerate(lines[1:]):
                if re.findall(phone_pattern,line.split('|')[1]):
                    info_warning = True
                elif re.findall(email_pattern,line.split('|')[2]):
                    info_warning = True
                if line.split('|')[6] == 'False':
                    safe_warning = True
                if info_warning:
                    info_warning_line.append(index+1)
                if safe_warning:
                    safe_warning_line.append(index+1)
                info_warning = False
                safe_warning = False

        #print(f'info_warning_line : {info_warning_line}');
        #print(f'safe_warning_line : {safe_warning_line}');

    warning_line = [0]
    # 0=위험정보 검출안됨, 1=info_warning_line, 2=ip_warning_line, 3=ip&info_warning_line
    if info_warning_line:
        warning_line.append(info_warning_line)
    if safe_warning_line:
        warning_line.append(safe_warning_line)

    if info_warning_line and safe_warning_line:
        warning_line[0] = 3
        sendSlackWebhook(file_name,warning_line)
        sendsmtp(file_name,warning_line)
    elif info_warning_line:
        warning_line[0] = 1
        sendSlackWebhook(file_name,warning_line)
        sendsmtp(file_name,warning_line)
    elif safe_warning_line:
        warning_line[0] = 2
        sendSlackWebhook(file_name,warning_line)
        sendsmtp(file_name,warning_line)
    else:
        print('위험 정보 검출 안됨')

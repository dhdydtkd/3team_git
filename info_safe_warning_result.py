import os
import re
import openpyxl
import mongo

def info_safe_warning_result(file_name):
    print(f'검색할 {file_name}')  
    info_warning = False
    safe_warning = False
    phone_pattern = r'\d{3}-\d{3,4}-\d{4}'
    email_pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"
    info_warning_line = []
    safe_warning_line = []
    check_result = 'Safe'    

    if file_name.endswith('.xlsx'):
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active

        for index, row in enumerate(sheet.iter_rows()):
            for i, cell in enumerate(row[:7]):
                if re.findall(phone_pattern,str(cell.value)) or re.findall(email_pattern,str(cell.value)) :
                    info_warning = True
                if i==6 and cell.value=='FALSE' : 
                    safe_warning = True
            if info_warning:
                info_warning_line.append(index)
            if safe_warning:
                safe_warning_line.append(index)
            info_warning = False
            safe_warning = False

    #print(f'info_warning_line : {info_warning_line}');
    #print(f'safe_warning_line : {safe_warning_line}');
    
    elif file_name.endswith('.txt'):
        with open(f'{file_name}','r',encoding='utf-8') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                if re.findall(phone_pattern,line) or re.findall(email_pattern,line):
                    info_warning = True
                if info_warning:
                    info_warning_line.append(index+1)
                info_warning = False
    elif file_name.endswith('.log'):
        with open(file_name,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                if re.findall(phone_pattern,line) or re.findall(email_pattern,line):
                    info_warning = True
                if info_warning:
                    info_warning_line.append(index+1)
                info_warning = False
    else:
        print('알 수 없는 파일 확장자')
        check_result = 'Unknown Extension'   
    if info_warning_line or safe_warning_line:
        check_result = 'Not Safe'    
        
    event_data = {
        'file_path' : file_name,
        'info_warning_line' : info_warning_line,
        'safe_warning_line' : safe_warning_line,
        'check_result' : check_result
    }
    mongo.mongoInsert(event_data)
    return info_warning_line, safe_warning_line
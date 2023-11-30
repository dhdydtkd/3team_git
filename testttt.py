import openpyxl
import re
import pandas as pd
import os

file_name = 'member_data/2023-11-30_insert_member.xlsx'
output_path = f"{file_name}"

wb = openpyxl.load_workbook(file_name)
sheet = wb.active

info_warning_line = []
safe_warning_line = []

info_warning = False
safe_warning = False
phone_pattern = r'\d{3}-\d{3,4}-\d{4}'
email_pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"
for index, row in enumerate(sheet.iter_rows()):
    for i, cell in enumerate(row[:7]):
        if re.findall(phone_pattern,str(cell.value)):
            info_warning = True
        elif re.findall(email_pattern,str(cell.value)):
            info_warning = True
        if i==6 and cell.value=='FALSE' : 
            safe_warning = True
    if info_warning:
        info_warning_line.append(index)
    if safe_warning:
        safe_warning_line.append(index)
    info_warning = False
    safe_warning = False

print(f'info_warning_line : {info_warning_line}');
print(f'safe_warning_line : {safe_warning_line}');

info_warning_line = []
safe_warning_line = []



df = pd.read_excel(file_name)
df.to_csv(f'{file_name}.txt',sep='|',index=False)

info_warning = False
safe_warning = False
with open(f'{file_name}.txt','r',encoding='utf-8') as f:
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
    
    
print(f'info_warning_line : {info_warning_line}');
print(f'safe_warning_line : {safe_warning_line}');


#docx


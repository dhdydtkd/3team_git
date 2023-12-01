
import os
import info_safe_warning_result as iswr

def dir_warning_check(dir_path):
    # 보안 검사에 통과하지 못한 파일 넣는 리스트

    #전체파일 리스트
    detection_Pass_File = []
    detection_Nonpass_File = []

    all_Files = os.listdir(dir_path)
    
    print(f"=====전체 파일 {all_Files}=====")
    # 전체 파일 검사

    warning_file_list = []

    for file_Name in all_Files:
        extand = os.path.splitext(file_Name)[1]
        if(extand == ".txt" or extand == ".txt" or extand == ".xlsx" ):
            info_warning_line, safe_warning_line = iswr.info_safe_warning_result(f'{dir_path}/{file_Name}')
            if info_warning_line or safe_warning_line:
                print(f'{file_Name}_{info_warning_line} : info_warning_line')
                print(f'{file_Name}_{safe_warning_line} : safe_warning_line')
                warning_file_list.append(file_Name)

    print(f'{warning_file_list} : warning_file_list')

    #detec_file(detection_Nonpass_File)

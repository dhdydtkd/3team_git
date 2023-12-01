import schedule
import time
import os
import time 

import create_faker_data as cfd

def job1():
    dir_path = ('static/search_dir_list.txt')
    print(f"dir 검사를 시작합니다.")
    with open(dir_path, 'r', encoding='utf8') as f :
        lines = f.readlines()
        for line in lines :
            new_line = os.path.join(line).replace("\n", "")
            if os.path.isdir(os.path.join(new_line)):
                all_files = os.listdir(os.path.join(new_line))
                for file in all_files:
                    if file.endswith('.xlsx') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.hwp') or file.endswith('.log'):
                        print(f"[{new_line}/{file}] 해당 경로에 존재합니다")
                    else:
                        print("파일이 없습니다.")
            else:
                print("폴더가 존재하지 않거나 폴더가 아닙니다.")


# def job2():
#     cfd.create_fake_date(10)


schedule.every(3).seconds.do(job1) # 3분마다 job 실행
#schedule.every(10).minute.do(job2) # 3분마다 job 실행

def search_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


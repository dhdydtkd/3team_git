import schedule
import time
import os

dir_path = "static"
all_files = os.listdir(dir_path)

def job():
    for file in all_files:
        if file.endswith('.xlsx') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.hwp'):
            os.path.isdir("static")
            print("존재합니다")
        else:
            print("파일이 없습니다.")

schedule.every(3).seconds.do(job) # 3분마다 job 실행


while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    job()

# 내부 라이브러리 선언
import sys
import os
import platform
import shutil

# 프로젝트 내 파일
import util

# 변수 선언
before_path = "./before"
after_path = "./after"
extensions = ["jpg", "jpeg", "png", "gif"]

def cnt_photo():
    cnt = 0

    for extension in extensions:
        file_list = util.search_photo(before_path, extension)

        for _ in file_list:
            cnt += 1

    if cnt == 0:
        print("사진이 존재하지 않습니다.")
        sys.exit(1)

    print(f"총 {cnt}개의 사진을 발견하였습니다.")

    while True:
        continue_management = input("계속 진행하시겠습니까? ('yes' or 'no'): ")

        if continue_management == "yes":
            current_os = platform.system()

            if current_os == "Windows":
                os.system("cls")
            else:
                os.system("clear")

            break
        elif continue_management == "no":
            print("프로그램을 종료합니다.")
            sys.exit(0)
        else:
            print("잘못된 값을 입력하셨습니다. 입력값을 확인해 주십시오.")

    return

def change_name():
    for extension in extensions:
        file_list = util.search_photo(before_path, extension)

        for file in file_list:
            name = ""

            date = util.get_photo_date(file)

            if date != "날짜 정보를 찾을 수 없습니다.":
                date = date.replace(":", "_")

                for i in range(0, 10):
                    name += date[i]

                name += "_"

                for i in range(11, len(date)):
                    name += date[i]

                name += ("." + extension)

                try:
                    before_name = os.path.join(file)
                    after_name = os.path.join("./after", name)
                    os.renames(before_name, after_name)
                    print(f"{before_name} >>> {after_name}")
                except Exception as e:
                    print(f"오류가 발생했습니다. {e}")
            else:
                print(date)

    print("-----------------------------------------------")

    return

def changed_name_photo_arrangement():
    for extension in extensions:
        file_list = util.search_photo(after_path, extension)

        for file in file_list:
            folder_name = ""

            for i in range(8, 18):
                folder_name += file[i]

            folder_name = after_path + "\\" + folder_name

            try:
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    print(f"폴더 생성: {folder_name}")

                shutil.move(file, os.path.join(folder_name, os.path.basename(file)))
                print(f"{file} 이동됨.")
            except Exception as e:
                print(f"이동 중 오류가 발생했습니다. {e}")

    print("-----------------------------------------------")

    return

def unchanged_name_photo_arrangement():
    for extension in extensions:
        file_list = util.search_photo(before_path, extension)

        for file in file_list:
            folder_name = "나머지"

            folder_name = after_path + "\\" + folder_name

            try:
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    print(f"폴더 생성: {folder_name}")

                shutil.move(file, os.path.join(folder_name, os.path.basename(file)))
                print(f"{file} 이동됨.")
            except Exception as e:
                print(f"이동 중 오류가 발생했습니다. {e}")

    print("-----------------------------------------------")

    return
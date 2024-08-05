# 내부 라이브러리 선언
import os
import platform

def start():
    print("--------------- 사진 관리 프로그램 ---------------")
    print("프로그램 실행 전 사진을 'before'폴더에 넣어 주십시오.")
    print("결과는 'after'폴더에 저장됩니다.")
    print("-----------------------------------------------")

def prepare():
    current_os = platform.system()

    while True:
        photo_prepare = input("사진을 'before'폴더에 준비하셨습니까? ('yes' or 'no'): ")

        if photo_prepare == "yes":
            if current_os == "Windows":
                os.system("cls")
            else:
                os.system("clear")

            break
        elif photo_prepare == "no":
            print("사진을 먼저 준비해 주십시오.")
        else:
            print("잘못된 값을 입력하셨습니다. 입력값을 확인해 주십시오.")
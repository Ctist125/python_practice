# 사진 관리 프로그램
# 사진의 이름을 날짜로 변경하고, 해당 날짜에 따른 폴더 생성 및 사진 정리를 목적으로 한다.
# 작성자: Tief

# 프로젝트 내 파일
import guide
import management

# 진행 코드
# 시작 가이드
guide.start()

# 사진 준비 여부 확인
guide.prepare()

# 준비된 사진 갯수 확인
management.cnt_photo()

# 사진 이름 변경
management.change_name()

# 사진 정리
# 변경된 사진 정리
management.changed_name_photo_arrangement()

# 나머지 사진 정리
management.unchanged_name_photo_arrangement()


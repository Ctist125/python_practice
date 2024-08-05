# 내부 라이브러리
import os
import glob

# 외부 라이브러리
import exifread


def search_photo(folder_path, extension):
    search_pattern = os.path.join(folder_path, f"*.{extension}")
    files = glob.glob(search_pattern)

    return files

def get_photo_date(file_path):
    try:
        # 'rb' = 바이너리 읽기 모드
        with open(file_path, "rb") as file:
            tags = exifread.process_file(file)
            date = tags.get("EXIF DateTimeOriginal")

            if date:
                return str(date)
            else:
                return "날짜 정보를 찾을 수 없습니다."
    except Exception as e:
        return f"오류 발생: {e}"
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 파이썬 환경변수 라이브러리 "python-dotenv" 설치 및 
# 환경 변수 파일 ".env" 사용하기
# pip install python-dotenv
# 주의사항 - 깃허브(GitHub), 깃소스트리(SourceTree) 등등...
#           오픈 소스 관리 프로그램에는 환경 변수 파일 ".env"을
#           Git 커밋(commit), 푸시(push) 처리하면 오류가 발생하므로
#           해당 환경 변수 파일 ".env"는 Git 커밋(commit), 푸시(push) 처리하면 안 된다.

# 파이썬 환경변수 파일(.env)에서 
# 챗봇에서 사용할 API 토큰 값 가져오기 

# 파이썬 환경변수 라이브러리 "python-dotenv"에 속한
# 함수 load_dotenv 읽어오기
from dotenv import load_dotenv
# 라이브러리 "os" 읽어와서 함수 os.getenv 호출해서 사용하기   
import os

load_dotenv()   # 함수 load_dotenv 호출 

# 함수 load_dotenv
# 매개변수 목록
# 1) dotenv_path - 환경변수 파일 ".env" 경로 문자열 
# 2) verbose 
# verbose = True - 환경변수 파일 ".env" 없는 경우 오류 메시지 출력 
# verbose = False - 환경변수 파일 ".env" 없는 경우에도 오류 메시지 출력 안함
# 매개변수 verbose 자체를 사용 안하면 
# 환경변수 파일 ".env" 없는 경우에도 오류 메시지 출력 안함
# 3) encoding
# encoding = "utf-8" - 환경변수 파일 ".env"에 속한 데이터들 중 한글이 포함된 경우
# load_dotenv(dotenv_path="", verbose=True, encoding="utf-8")

# 함수 os.getenv 호출해서 환경변수 파일 ".env"에 속한
# "MY_TOKEN"에 할당된 값 "abcd" 읽어와서
# 변수 "TOKEN"에 저장하기  
TOKEN = os.getenv("MY_TOKEN")
print(TOKEN)   # 변수 "TOKEN"에 저장된 값 "abcd" 출력 
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# QRCode 관련 라이브러리 2가지 "pyqrcodeng" "pypng" 
# 설치 하기 위해 아래 명령어 입력 및 엔터
# pip install pyqrcodeng pypng

# 함수 read_qrcode_zbar 사용하여 
# QRCode 이미지 파일을 읽기 위해 
# 라이브러리 "pyzbar" 설치하기 
# 참고 URL - https://pypi.org/project/pyzbar/
# 라이브러리 "pyzbar" 설치 하기 위해 
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에  
# 아래 명령어 입력 및 엔터
# pip install pyzbar
# 라이브러리 "pyzbar" 윈도우에서 설치시
# 아래와 같은 오류 메시지 출력되면 
# 반드시 Visual C++ 2013 재배포 가능 패키지 설치 필수
# 오류 메시지 텍스트
# Windows error message
# If you see an ugly ImportError 
# when importing pyzbar on Windows 
# you will most likely need the Visual C++ Redistributable Packages 
# for Visual Studio 2013. 
# Install vcredist_x64.exe if using 64-bit Python, vcredist_x86.exe 
# if using 32-bit Python.

# 함수 read_qrcode_zbar 사용하여 
# QRCode 이미지 파일을 읽기 위해 
# OpenCV 그래픽 라이브러리 "cv2 - opencv-python" 설치하기 
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에  
# 아래 명령어 입력 및 엔터
# pip install opencv-python

# 인코딩(encoding)과 디코딩(decoding) 차이
# 참고 URL - https://blog.naver.com/yoodh0713/221559156214?trackingCode=rss


import pyqrcodeng as qrcode
import os  # QRCode 전용 클래스 QRCreater 구현한 모듈파일(qrcode.py) 절대경로 가져오기 위해 os 모듈 가져오기 
from uuid import uuid4   # 난수(Random Number)를 만들어주는 함수 uuid4 가져오기 
import pyzbar.pyzbar as pyzbar  # QRCode 이미지 파일을 읽기 위해 라이브러리 "pyzbar" 읽어오기
import cv2 # OpenCV 그래픽 라이브러리 "cv2 - opencv-python" 읽어오기 

# **** QRCode 관련 구현한 모든 기능들을 
# "하나의 모듈"로 사용하기위해 
# 아래처럼 QRCode 전용 클래스 QRCreater 구현하기 **** 
class QRCreater():
    # 클래스 QRCreater 생성자 __init__ 구현 
    # self는 클래스 QRCreater 객체 자기자신 
    def __init__(self):
        self.q = None   # None 초기화 
        self.module_color = (0, 0, 0, 0)   # (0, 0, 0, 0) 초기화
        self.back_color = (255, 255, 255, 255)   # rgba - (255, 255, 255, 255) 초기화 
        self.scale = 5 # 5 초기화
    
    # 사용자 요청시 QRCode를 base64 인코딩(encoding) 처리된 문자열로 변환 및 리턴
    # QRCreater().qrcode_wifi("MYIPTIME", "WPA", "12345678").get_base64()
    def get_base64(self):
        # qrcode 객체 self.q에 값이 존재하는 경우 
        if self.q is not None:
            # QRCode 이미지 파일 -> base64 인코딩(encoding) 처리된 문자열로 변환 및 리턴
            return self.q.png_data_uri(module_color=self.module_color, background=self.back_color, scale=self.scale)
        # qrcode 객체 self.q에 값이 없는 경우 
        return None   # None 리턴 
        
    # 전화번호부에 등록할 연락처 정보 QRCode 생성 및 리턴
    def qrcode_namecard(self, name, tel, email=None, url=None, org=None, title=None):
        # VCARD 시작 문자열 처리
        vcard = f"BEGIN:VCARD\n"
        # VCARD 실제 인식 내용 문자열 처리
        vcard += f"VERSION:4.0\n"   # 버전
        vcard += f"FN:{name}\n"     # 이름
        vcard += f"TEL;TYPE=WORK;CELL:{tel}\n"   # 전화번호

        # 함수 qrcode_namecard 
        # 매개변수 org에 할당된 값이 존재하는 경우
        if org is not None:
            vcard += f"ORG:{org}\n"   # 조직이름
        # 매개변수 title에 할당된 값이 존재하는 경우
        if title is not None:
            vcard += f"TITLE:{title}\n" # 직위
        # 매개변수 email에 할당된 값이 존재하는 경우
        if email is not None:
            vcard += f"EMAIL;TYPE=WORK:{email}\n"   # 이메일주소
        # 매개변수 url에 할당된 값이 존재하는 경우
        if url is not None:
            vcard += f"URL:{url}\n"  # URL주소

        # VCARD 끝 문자열 처리
        vcard += "END:VCARD\n"

        # QRCode 객체 self.q 생성 및
        # 변수 vcard에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
        self.q = qrcode.create(vcard, encoding="utf-8")
        self.q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)
        return self    # 클래스 QRCreater 객체 자기자신 self 리턴

    # 스마트폰 카메라로 스캔(촬영)만 하면
    # WIFI 자동 연결(접속)할 수 있는 QRCode 생성 및 리턴
    def qrcode_wifi(self, ssid, encrypt, password):
        data = f"WIFI:S:{ssid};T:{encrypt};P:{password}"
        # QRCode 객체 self.q 생성 및
        # 변수 data에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
        self.q = qrcode.create(data, encoding="utf-8")
        return self   # 클래스 QRCreater 객체 자기자신 self 리턴

    # 문자(SMS - 문자 길이 80 Byte 미만 / MMS - 문자 길이 80 Byte 초과) 
    # 메시지 보내는 QRCode 생성 및 리턴
    # QRCode 문자(SMS) 메시지 사용 예시
    # SMSTO:전화번호:보낼내용
    # MMSTO:전화번호:보낼내용
    def qrcode_sms(self, sendto, msg):
        data = f"SMSTO:{sendto}:{msg}"
        # QRCode 객체 self.q 생성 및
        # 변수 data에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
        self.q = qrcode.create(data, encoding="utf-8")
        return self   # 클래스 QRCreater 객체 자기자신 self 리턴

    # 이메일 보내는 QRCode 생성하기
    # 이메일 직접 보내지는 않고
    # 직접 보내기 직전까지만 입력 해놓은 상태로 멈춘 상태로 QRCode만 생성 및 리턴
    # 함수 qrcode_email 매개변수 목록 
    # email - 이메일주소
    # subject - 이메일제목
    # body - 이메일작성내용
    # QRCode 이메일 입력내용 사용 예시
    # MATMSG:TO:이메일주소;SUB:이메일제목;BODY:이메일작성내용;;
    def qrcode_email(self, email, subject, body):
        data = f"MATMSG:TO:{email};SUB:{subject};BODY:{body};;"
        # QRCode 객체 self.q 생성 및
        # 변수 data에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
        self.q = qrcode.create(data, encoding="utf-8")
        return self   # 클래스 QRCreater 객체 자기자신 self 리턴

    # 스마트폰에 설치된 지도앱이 자동으로 실행될 수 있고
    # 지도앱의 해당 위도,경도 위치를 표기해줄 수 있도록 QRCode 생성 및 리턴
    # 함수 qrcode_email 매개변수 목록 
    # lon - 경도(longitude)
    # lat - 위도(latitude)
        # QRCode 지도앱 사용 예시
        # z=10 - zoom 의미(z - 지도를 얼만큼 확대할지 설정)
        # GEO:경도,위도?z=10
    def qrcode_geo(self, lon, lat):
        data = f"GEO:{lon},{lat}?z=10"
        # QRCode 객체 self.q 생성 및
        # 변수 data에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
        self.q = qrcode.create(data, encoding="utf-8")
        return self   # 클래스 QRCreater 객체 자기자신 self 리턴
    
    # 매개변수 data에 인자값을 넣어서  
    # QRCode 객체 self.q 생성 및 클래스 QRCreater 객체 자기자신 self 리턴
    def make(self, data):
        # QRCode 객체 self.q 생성 및
        # 변수 data에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
        self.q = qrcode.create(data, encoding="utf-8")
        return self   # 클래스 QRCreater 객체 자기자신 self 리턴

    # 클래스 QRCreater 객체 자기자신 self에 속한
    # QRCode 객체 self.q를 가지고 QRCode 이미지 파일 만들기 
    # (예시) QRCreater().qrcode_wifi("MYIPTIME", "WPA", "12345678").png()
    def png(self):
        # 현재 QRCreater 클래스 모듈 파일(qrcode.py)의 
        # 절대경로(os.path.abspath) 가져와서 
        # 그중 해당 모듈 파일의 상위 폴더 경로만 가져와서 변수 cur_dir에 할당 
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        # 변수 filename에 문자열 할당 (변수 cur_dir\\난수(Random Number) 생성 함수 uuid4() 호출.png)
        filename = f"{cur_dir}\\{uuid4()}.png"
        # QRCode 객체 self.q 생성 및
        # 변수 filename에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
        self.q.png(filename, scale=5)
        return filename

# QRCode OpenCV 이미지 파일을 읽는 함수 
def read_qrcode_zbar(opencv_image):
    # 변수 gray에 저장된 OpenCV 이미지를 흑백으로 변경
    # OpenCV는 기본적으로 이미지를 RGB가 아니라 BGR 형태로 읽어들인다.
    # 하여 함수 cv2.cvtColor 사용하여 
    # OpenCV 그래픽 라이브러리 "cv2 - opencv-python" 사용해서 
    # BGR 형태로 읽어드린 이미지를 GRAY로 바꾼 후 변수 gray에 다시 저장한다.
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    # 변수 decoded에 변수 gray 이미지 디코딩(decoding) 처리후 넘겨주기
    decoded = pyzbar.decode(gray)
    # 리스트 객체 results 생성 
    results = []
    # QRCode 이미지 하나에 여러개의 이미지가 있는 경우 
    # for문으로 반복해서 각각의 이미지 모두 방문 
    for d in decoded:
        qr_data = d.data.decode("utf-8")   # "utf-8"로 디코딩(decode) 처리 후 변수 qr_data에 저장 
        qr_type = d.type  # 변수 qr_type에 d.type 값 할당 

        # 매개 변수 opencv_image로 전달된 QRCode 이미지가 여러개인 경우
        # 여러 개의 QRCode 이미지를 뽑고  
        # 함수 append 사용하여 리스트 객체 results에 데이터 추가 
        results.append({
            "data": qr_data,
            "type": qr_type
        })
    return results   # 리스트 객체 results 리턴 

if __name__ == "__main__": 
    # OpenCV 그래픽 라이브러리 "cv2 - opencv-python" 사용 예시
    # QRCode 인식을 하기 위해서 아래처럼 진행
    # # 1. OpenCV 그래픽 라이브러리 "cv2 - opencv-python" 사용해서 
    # 이미지를 읽어드리고 변수 img에 저장하기
    img = cv2.imread("test.png")   
    # 변수 img에 저장된 OpenCV 이미지를 흑백으로 변경
    # OpenCV는 기본적으로 이미지를 RGB가 아니라 BGR 형태로 읽어들인다.
    # 하여 함수 cv2.cvtColor 사용하여 
    # OpenCV 그래픽 라이브러리 "cv2 - opencv-python" 사용해서 
    # BGR 형태로 읽어드린 이미지를 GRAY로 바꾼 후 변수 img에 다시 저장한다.
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a = pyzbar.decode(img)  # 변수 img 디코딩(decode) 처리
    print(a)

    # QRCode 전용 클래스 QRCreater 객체 qr 생성 예시1
    # qr = QRCreater()
    # qr.qrcode_geo()
    # qr.png()

    # QRCode 전용 클래스 QRCreater 객체 qr 생성 예시2
    # qr_wifi_png = QRCreater().qrcode_wifi("MYIPTIME", "WPA", "12345678").png()

    # QRCode 전용 클래스 QRCreater 객체 qr 생성 예시3
    # qr_wifi_base64 = QRCreater().qrcode_wifi("MYIPTIME", "WPA", "12345678").get_base64()
    # print(qr_wifi_base64)

    # 스마트폰에 설치된 지도앱이 자동으로 실행될 수 있고
    # 지도앱의 해당 위도,경도 위치를 표기해줄 수 있도록 QRCode 생성
    # qrcode_geo(37.6591, 127.2456)

    # 스마트폰 카메라로 스캔(촬영)만 하면
    # WIFI 자동 연결(접속)할 수 있는 QRCode 생성
    # qrcode_wifi("IPTIME", "WPA", "12345678")
    # 전화번호부에 등록할 연락처 정보 QRCode 생성
    # qrcode_namecard("남박사", "010-1234-1234", email="abcd@naver.com", url="https://www.naver.com")
    # q = qrcode.create("https://www.naver.com")  # QRCode 객체 q 생성 및 값("https://www.naver.com") 할당 
    # q = qrcode.create("test")  # QRCode 객체 q 생성 및 값("test") 할당 
    # print(q)   # 터미널 창에 QRCode 객체 q에 할당된 정보(데이터) 출력
    
    # QRCode 객체 q에 할당된 정보(데이터) 기반으로 QRCode 이미지를 확장자 .png 파일로 새로 생성
    # q.png("test.png")  
    # 아래처럼 QRCode 코드 색상(module_color=(34, 30, 63)) 설정 및 
    # 이미지 배경 색상 "Yellow"(background=(255, 255, 0)) 및
    # 이미지 파일 크기 "scale=3" 설정 
    # q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)

    # QRCode 이미지 파일을 base64 인코딩(encoding) 처리된 문자열로 변환 
    # (문자열로 해당 파일을 전송해야 하는 경우에 사용)
    # qr_str = q.png_data_uri(module_color=(34, 30, 63), background=(255, 255, 0), scale=3)
    # print(qr_str)

    # QRCode VCARD 사용 예시
    # BEGIN:VCARD  # VCARD 시작
    # # VCARD 실제 인식 내용
    # VERSION:4.0
    # FN:남박사
    # ORG:조직이름
    # TITLE:직위
    # TEL;TYPE=WORK;CELL:010 1234 1234
    # EMAIL;TYPE=WORK:abcd@naver.com
    # URL:https://www.naver.com
    # END:VCARD # VCARD 끝


# 문자(SMS - 문자 길이 80 Byte 미만 / MMS - 문자 길이 80 Byte 초과) 
# 메시지 보내는 QRCode 생성하기
    # QRCode 문자(SMS) 메시지 사용 예시
    # SMSTO:전화번호:보낼내용
# def qrcode_sms(sendto, msg):
#     data = f"SMSTO:{sendto}:{msg}"
#     q = qrcode.create(data, encoding="utf-8")
#     q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)

# 문자(SMS - 문자 길이 80 Byte 미만 / MMS - 문자 길이 80 Byte 초과) 
# 메시지 보내는 QRCode 생성하기
    # QRCode 문자(MMS) 메시지 사용 예시
    # MMSTO:전화번호:보낼내용
# def qrcode_mms(sendto, msg):
#     data = f"MMSTO:{sendto}:{msg}"
#     q = qrcode.create(data, encoding="utf-8")
#     q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)

# 이메일 보내는 QRCode 생성하기
# 이메일 직접 보내지는 않고
# 직접 보내기 직전까지만 입력 해놓은 상태로 멈춘 상태로 QRCode만 생성하기
# 함수 qrcode_email 매개변수 목록 
# email - 이메일주소
# subject - 이메일제목
# body - 이메일작성내용
    # QRCode 이메일 입력내용 사용 예시
    # MATMSG:TO:이메일주소;SUB:이메일제목;BODY:이메일작성내용;;
# def qrcode_email(email, subject, body):
#     data = f"MATMSG:TO:{email};SUB:{subject};BODY:{body};;"
#     q = qrcode.create(data, encoding="utf-8")
#     q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)

# 스마트폰에 설치된 지도앱이 자동으로 실행될 수 있고
# 지도앱의 해당 위도,경도 위치를 표기해줄 수 있도록 QRCode 생성
# 함수 qrcode_email 매개변수 목록 
# lon - 경도(longitude)
# lat - 위도(latitude)
    # QRCode 지도앱 사용 예시
    # z=10 - zoom 의미(z - 지도를 얼만큼 확대할지 설정)
    # GEO:경도,위도?z=10
# def qrcode_geo(lon, lat):
#     data = f"GEO:{lon},{lat}?z=10"
#     q = qrcode.create(data, encoding="utf-8")
#     q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)

# 스마트폰 카메라로 스캔(촬영)만 하면
# WIFI 자동 연결(접속)할 수 있는 QRCode 생성하기
    # QRCode WIFI 사용 예시
    # WIFI:S:공유기이름;T:암호화방식;P:비밀번호 
# 함수 qrcode_wifi 매개변수 목록 
# ssid - 공유기이름
# encrypt - 암호화방식 
# password - wifi 비밀번호
# def qrcode_wifi(ssid, encrypt, password):
#     data = f"WIFI:S:{ssid};T:{encrypt};P:{password}"
#     q = qrcode.create(data, encoding="utf-8")
#     q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)

# 매개변수로 전달받은 인자값을 가지고 
# 전화번호부에 등록할 연락처 정보 QRCode 생성하기 
    # QRCode VCARD 사용 예시
    # BEGIN:VCARD  # VCARD 시작
    # # VCARD 실제 인식 내용
    # VERSION:4.0
    # FN:남박사
    # ORG:조직이름
    # TITLE:직위
    # TEL;TYPE=WORK;CELL:010 1234 1234
    # EMAIL;TYPE=WORK:abcd@naver.com
    # URL:https://www.naver.com
    # END:VCARD # VCARD 끝
# def qrcode_namecard(name, tel, email=None, url=None, org=None, title=None):
#     # VCARD 시작 문자열 처리
#     vcard = f"BEGIN:VCARD\n"
#     # VCARD 실제 인식 내용 문자열 처리
#     vcard += f"VERSION:4.0\n"   # 버전
#     vcard += f"FN:{name}\n"     # 이름
#     vcard += f"TEL;TYPE=WORK;CELL:{tel}\n"   # 전화번호

#     # 함수 qrcode_namecard 
#     # 매개변수 org에 할당된 값이 존재하는 경우
#     if org is not None:
#         vcard += f"ORG:{org}\n"   # 조직이름
#     # 매개변수 title에 할당된 값이 존재하는 경우
#     if title is not None:
#         vcard += f"TITLE:{title}\n" # 직위
#     # 매개변수 email에 할당된 값이 존재하는 경우
#     if email is not None:
#         vcard += f"EMAIL;TYPE=WORK:{email}\n"   # 이메일주소
#     # 매개변수 url에 할당된 값이 존재하는 경우
#     if url is not None:
#         vcard += f"URL:{url}\n"  # URL주소

#     # VCARD 끝 문자열 처리
#     vcard += "END:VCARD\n"

#     # QRCode 객체 q 생성 및
#     # 변수 vcard에 저장된 문자열 데이터를 한글 포함된 인코딩 처리(encoding="utf-8")
#     q = qrcode.create(vcard, encoding="utf-8")
#     q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=3)

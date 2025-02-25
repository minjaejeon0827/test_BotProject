# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 파이썬 환경변수 라이브러리 "python-dotenv" 설치 및 
# 환경 변수 파일 ".env" 사용하기
# pip install python-dotenv
# 주의사항 - 깃허브(GitHub), 깃소스트리(SourceTree) 등등...
#           오픈 소스 관리 프로그램에는 환경 변수 파일 ".env"을
#           Git 커밋(commit), 푸시(push) 처리하면 오류가 발생하므로
#           해당 환경 변수 파일 ".env"는 Git 커밋(commit), 푸시(push) 처리하면 안 된다.

# 서버 간 애플리케이션에 OAuth 2.0 (인증) 사용
# 참고 URL - https://developers.google.com/identity/protocols/oauth2/service-account?hl=ko

# 구글 캘린더 API 범위 선택 참고 자료
# 함수 get_jwt -> 딕셔너리(Dictionary) 객체 "payload" -> 항목 "scope"에 사용 
# "scope": "https://www.googleapis.com/auth/calendar \
#         https://www.googleapis.com/auth/calendar.events",
# 참고 URL - https://developers.google.com/calendar/api/auth?hl=ko

# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# jwt 라이브러리 "pyjwt[crypto]" 설치 하기 위해 아래 명령어 입력 및 엔터
# pip install pyjwt[crypto]

import jwt  # jwt 라이브러리 가져오기 
import time
import requests
from datetime import datetime, timedelta

# jwt 토큰 가져오기 
def get_jwt():
    # private_key_id = ""
    # private_key = "-----BEGIN PRIVATE KEY-----\n-----END PRIVATE KEY-----\n"
    private_key_id = "948013ea97a3f543eca1033f5db6f3bd31abf824"
    private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBzjOqXGe2l4Am\n1hoMEftEuLhfyt/0awOPPJ71eNI6PHvJ1kshT3cR2BX3NYa8j1qTv830X9OGnBsE\nuuIW5uWVEP4PUp1b+DlGmvlcnjuy6S+D0lXbvTAfAWOal6ZxqA48A9x237xL5+j3\nfzXoClMZlbgLC+lHbXdBh3ZjMcSm6un4L03f9gnJh0CQ8eP9yr+n6GSo1oGMyg/H\nMnW6MRURo6EVRhoKBS8PCEyI1ilPh0YOl4RxYYriui2hG7yq5EKCUOnOYt/bAGnb\nC1V8RGbLzrb2/AFkdnfmm/dk1I2W96pXXuGsW4abzq9l/ex475aXOgRqHMCK3kkb\nHHwG6srZAgMBAAECggEADSyeOHt1lWTxEjLFrIJgaUiBSAm7dZr8r/T3/UnMSKcp\n5wuJKeeD+ZON0rMxyImaJ6cHMhB9iY39DDJEAjiJ7Lst+g6sob7a7eDFCLW86ymM\n0FIxAfH3XnQyuCSM7Pb2mL/Occo9u481N/XOzUo+YePake2qWu+nBq5VruKIMqxx\nGLE3BVxvgarOWsxJ746fjN7+Uq/KjEMCtz8mjosUUvrSdAul8w7ayZeFrgZm6I6L\ncCETJ0U4OqHP1X7ukuEJ00Lq+LInkwkDLJDm9lPtpUFRsnKbk0dM4Bkz8ctTVdAf\n0l7rkEIpEfJxijil+2tA/t535S71av7uSv9J46yugQKBgQDe4kvg2DkXGfRMdwxL\nN5c2ntn4VWNtALXn6fMlhqi4MEWcfDA3eUVvLOO9mAifiDJ/yTM/fYwTaWkYt7Li\nUqXw2l+3s8OuLy5c6rAaleFGr8gdur7c8Kf8xjXe/mbWlxxcrBD+7znGQ7zOsGaG\nYDiBG4INFhCAUnbOXuDppDGB6QKBgQDemd08f3dAmbhNtaS8Wl4cDl6EIl5+reSF\nDigNRh1CKAn7PTIK3T6F4IQaxoFJtYyDsIgcP5tXpcqIZVB8AB3ee12ARs3WwMLP\niNw0kNSPWStDVzqrjj83LofEN1m1yOUmkMVbLA1j7754X/W+AwmxUTn2UGDq472L\nDx6AdYn7cQKBgQCw52qUZupBVL9bpa3jUZc6qjCVc6i7zrGTBlSP92aY8u99efCH\nR0D+MeH9DNvjS6XRWS/M9+gjTCo3jS51hmXhWmJYm1z4NsiUxU3LfCTXBxRNzHhL\nQtQCxIvjl4amUkAXqha/Ub9Ih2EnqEln5J1UlDHQEzA7ubhEqnfX2hPVaQKBgQDP\nNTDAmPKb+ruZ8qTXA9OokCOhIhEOILaguI3F1Wd05qpr6QoFHO+PVXADMJa20z1q\ndFAu43KpwtVl49Foq/8h03o05zPCXQq6fu5kLBEBIwLnm3IssavcpP6SQufKFKhi\nHs7nUHlido+5o7Gv30oNecvXofiljbspj7hX4ZHAsQKBgDZQW3m0RKrTkV6Snxo+\noIBHNLBXRFkGZKqiqusPISdxMYF+eLGAUx9qtDSDhz/vdgZv5Y0hW2M+ihuCH9fV\ndO5I2rQJ3/tT1+ap32bjLNgSo6oUyKVr/tajILKVIT2UyoyX2Tp/VkmsEFGIwHBY\nXTW0oYf1c4ugnboHT1Pp+Bns\n-----END PRIVATE KEY-----\n"

    service_account = "calendar@spiritual-vent-451406-s1.iam.gserviceaccount.com"
    iat = time.time()
    exp = iat + 3600  # jwt 토큰 유효시간 3600초 설정 및 변수 exp에 값 저장  
    payload = {
        "iss": service_account,
        "sub": service_account,
        "scope": "https://www.googleapis.com/auth/calendar \
                https://www.googleapis.com/auth/calendar.events",
        "aud": "https://oauth2.googleapis.com/token",
        "iat": iat,
        "exp": exp
    }
    header = {"kid": private_key_id}
    # jwt(Json Web Token) 토큰은 그 안에는
    # 헤더(headers)에는 아래와 같은 데이터가 들어 있다.
    # "type" : "JWT"(타입은 JWT 의미), "alg" : RS256(RS256 알고리즘 사용)
    # 페이로드(PAYLOAD)는 데이터를 담는 실질적인 영역 의미
    # 마지막에 시그니처(SIGNATURE)는 어떤 유효성, 무결성을 보장한다.
    # jwt(Json Web Token) 토큰 생성 및 변수 _jwt에 저장 
    _jwt = jwt.encode(payload, private_key, headers=header, algorithm="RS256")
    return _jwt

# jwt(Json Web Token) 토큰을 가지고 구글 캘린더 API 사용할 액세스 토큰("access_token") 구하기 
def get_access_token():
    _jwt = get_jwt()   # jwt(Json Web Token) 토큰 가져오기 
    url = "https://www.googleapis.com/oauth2/v4/token"
    data = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": _jwt
    }
    # HTTP - POST 요청 진행 
    # 인자로 전달한 URL 주소값이 들어있는 변수 url
    # 데이터 값 들어있는 변수 data
    r = requests.post(url, data=data)

    # HTTP - POST 요청 결과값이 들어있는 변수 r을 json 형태로 변환(json()) 및 
    # json 데이터에 속한 항목 "access_token"(액세스 토큰) 찾아서 리턴 
    return r.json().get("access_token")

# 구글 캘린더의 이벤트 가져오기 
def get_calendar_events(timeMin=None, timeMax=None):
    access_token = get_access_token()   # 구글 캘린더 API 사용하기 위해 액세스 토큰("access_token") 가져오기 
    if access_token is None:
        return []
    # 변수 c_id는 구글 캘린더 아이디 값이 저장되는 변수 의미
    c_id = "minjaejeon0827@gmail.com"
    url = f"https://www.googleapis.com/calendar/v3/calendars/{c_id}/events?timeZone=Asia/Seoul"

    if timeMin is not None:
        if isinstance(timeMin, str):
            timeMin = datetime.strptime(timeMin, "%Y-%m-%d")
        timeMin -= timedelta(hours=9)
        url += f"&timeMin={timeMin.isoformat("T")}Z"
    
    if timeMax is not None:
        if isinstance(timeMax, str):
            timeMax = datetime.strptime(timeMax, "%Y-%m-%d")
        timeMax -= timedelta(hours=9)
        url += f"&timeMax={timeMax.isoformat("T")}Z"

    # 딕셔너리(Dictionary) 변수 headers에 아래처럼 데이터 저장 
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    # HTTP - GET 요청 
    # 구글 서버가 액세스 토큰을 확인해서 정상적으로 권한이 있으면 결과값 반환해줌
    r = requests.get(url, headers=headers)
    print(r.text)
    print(r.json())
    # 결과값이 저장된 변수 r을 json 형태 변환(json()) 및 
    # 항목 "items"에 매핑된 데이터 값 가져와서 변수 _items에 저장 
    _items = r.json().get("items")
    return _items   # 변수 _items 리턴 

# 구글 캘린더에 이벤트 등록하기 
def insert_event(summary, colorId="2", start_date=None, end_date=None, location=None, description=None):
    # 변수 c_id는 구글 캘린더 아이디 값이 저장되는 변수 의미
    c_id = "minjaejeon0827@gmail.com"

    access_token = get_access_token()   # 구글 캘린더 API 사용하기 위해 액세스 토큰("access_token") 가져오기 
    # 액세스 토큰("access_token")이 없는 경우(None)
    # 구글 캘린더 API 사용 불가 
    if access_token is None:
        return None   # None 리턴 
    # 시작날짜(start_date)는 있는데 종료날짜(end_date)는 없는 경우 
    if start_date is not None and end_date is None:
        # print 함수 호출해서 안내문구 터미널창 출력 
        print("시작날짜와 종료날짜는 함께 설정 되어야 합니다.")
        return None
    
    # 시작날짜(start_date) 있고 종료날짜(end_date)도 있는 경우
    if start_date is not None and end_date is not None:
        # 시작날짜(start_date) 변수의 자료형이 str인 경우 
        if isinstance(start_date, str):
            # 변수 시작날짜(start_date)에 날짜 데이터 타입 "연월시분" 변환 및 다시 변수 시작날짜(start_date)에 저장  
            start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
        # 종료날짜(end_date) 변수의 자료형이 str인 경우
        if isinstance(end_date, str):
            # 변수 종료날짜(end_date)에 날짜 데이터 타입 "연월시분" 변환 및 다시 변수 종료날짜(end_date)에 저장  
            end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M")
    
    # 딕셔너리(Dictionary) 변수 event_data 선언 및 데이터 저장  
    event_data = {
        "summary": summary,
        "colorId": colorId,
        "recurrence": ["RRULE:FREQ=DAILY;COUNT=1"],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10},
            ]
        }
    }

    # 시작날짜(start_date) 있고 종료날짜(end_date)도 있는 경우
    if start_date is not None and end_date is not None:
        # 위에서 만든 딕셔너리(Dictionary) 변수 event_data에
        # 메서드 update 호출하여 매개변수 "start", "end" 추가 
        event_data.update({
            "start": {"dateTime": str(start_date.isoformat("T")), "timeZone": "Asia/Seoul"},
            "end": {"dateTime": str(end_date.isoformat("T")), "timeZone": "Asia/Seoul"},
        })
    # 위치(location)이 있는 경우 
    if location is not None:
        # 위에서 만든 딕셔너리(Dictionary) 변수 event_data에
        # 메서드 update 호출하여 매개변수 "location" 추가 
        event_data.update({"location": location})
    # 설명(description) 있는 경우 
    if description is not None:
        # 위에서 만든 딕셔너리(Dictionary) 변수 event_data에
        # 메서드 update 호출하여 매개변수 "description" 추가 
        event_data.update({"description": description})
    
    # 딕셔너리(Dictionary) 변수 headers에 아래처럼 데이터 저장 
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }

    url = f"https://www.googleapis.com/calendar/v3/calendars/{c_id}/events"
    # 구글 캘린더에 이벤트 등록하기 위해 HTTP - POST 요청 진행
    r = requests.post(url, headers=headers, json=event_data)
    print(r.text)
    return r.json()

# 구글 캘린더에 등록된 이벤트 삭제하기 
# 매개변수 event_id - 삭제할 이벤트 아이디 값을 인자로 받음
def delete_event(event_id):
    # 구글 캘린더 API 사용하기 위해 액세스 토큰("access_token") 가져오기 
    access_token = get_access_token()
    # 액세스 토큰("access_token")이 없고 삭제할 이벤트 아이디(event_id)도 없는 경우 
    if access_token is None or event_id is None:
        return False   # False 리턴 (함수 delete_event 실행 종료)
    # 변수 c_id는 구글 캘린더 아이디 값이 저장되는 변수 의미
    c_id = "minjaejeon0827@gmail.com"

    # 딕셔너리(Dictionary) 변수 headers에 아래처럼 데이터 저장 
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }

    url = f"https://www.googleapis.com/calendar/v3/calendars/{c_id}/events/{event_id}"
    # 구글 캘린더에 등록된 이벤트 삭제하기 위해 HTTP - DELETE 요청 진행
    # HTTP - DELETE 요청 결과값 변수 r에 저장 
    r = requests.delete(url, headers=headers)

    # 변수 r에 속하는 속성 "r.status_code"에 할당된 값이 204인 경우 
    if r.status_code == 204:
        return True   # 구글 캘린더에 등록된 이벤트 삭제 처리 완료 
    return False   # 오류 발생시 False 리턴 (함수 delete_event 실행 종료)

if __name__ == "__main__":
    print(delete_event("7pb8rabf8gjou61huruhc1clgs"))
    # print(insert_event("파이썬 봇 만들기", start_date="2025-02-19 12:00", end_date="2025-02-19 16:00", location="홈", description="열심히하자"))
    # events = get_calendar_events(timeMin=datetime.now())
    # for e in events:
    #     print(e)
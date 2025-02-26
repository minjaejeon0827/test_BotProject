# *** 카카오톡 챗봇 나에게 메시지 보내기 API 사용 방법 *****
# 1. 구글 크롬(Chrome) 실행 -> 키워드 "카카오 개발자 센터 " 검색
# 2. Kakao Developers - 카카오 클릭
# 3. Kakao Developers 웹사이트 이동 -> 카카오 계정 로그인 진행
# 4. Kakao Developers 웹사이트 우측 상단 버튼 "내 애플리케이션" 클릭
# 5. 화면 "내 애플리케이션" 이동 -> 화면 항목 "전체 애플리케이션" 하단 버튼 "애플리케이션 추가하기" 클릭
# 6. 팝업화면 "애플리케이션 추가하기" 출력 -> 항목 "앱 이름"에 카카오 챗봇 이름 "Test2_ImagineBuilder" 작성 
#    -> 항목 "회사명"에는 "개인" 입력 -> 항목 "카테고리"에는 "광고/비즈니스" 체크
#    -> 팝업화면 하단 약관 "서비스 이용이 제한되는 카테고리, 금지된 내용, 금지된 행동 관련 운영정책을 위반하지 않는 앱입니다." 체크하기
#    -> 팝업화면 버튼 "저장" 클릭 -> 카카오 챗봇 "Test2_ImagineBuilder" 생성 완료 
# 7. 6번에서 생성한 카카오 챗봇 "Test2_ImagineBuilder" 클릭 -> 화면 "내애플리케이션 > 앱 설정 > 대시보드" 화면 이동
#    -> 해당 화면 좌측 항목 "앱 설정" 하단 버튼 "앱 키" 클릭
#    -> 화면 "내애플리케이션 > 앱 설정 > 앱 키" 이동 
#    -> "네이티브 앱 키", "REST API 키", "JavaScript 키", "Admin 키" 값 존재하면 8번 진행
# 8. 해당 화면 좌측 항목 "제품 설정" 하단 버튼 "카카오 로그인" 클릭
#    -> 화면 "내애플리케이션 > 제품 설정 > 카카오 로그인" 이동
#    -> 항목 "활성화" 설정 하단 상태 버튼 "OFF" 클릭 
#    -> 팝업화면 "카카오 로그인 활성화" 출력 
#    -> 버튼 "활성화" 클릭 버튼 "ON"으로 변경 
#    -> 해당 화면 마우스 스크롤 사용해서 아래로 내리기 
#    -> 항목 "Redirect URI" 하단 버튼 "Redirect URI" 클릭
#    -> 팝업화면 "Redirect URI" 출력되면 
#       카카오 로그인에서 사용할 OAuth Redirect URI 주소를 아래처럼 localhost로 작성(테스트 용도이기 때문)
#       http://localhost:9999
#    -> 버튼 "저장" 클릭
# 9. 화면 "내애플리케이션 > 제품 설정 > 카카오 로그인" 좌측 항목 "카카오 로그인" 밑에 버튼 "동의항목" 클릭
#    -> 화면 "내애플리케이션 > 제품 설정 > 카카오 로그인 > 동의항목" 이동
#    -> 해당 화면 마우스 스크롤 사용해서 아래로 내리기
#    -> 항목 "접근권한" 하단 항목 이름 "카카오톡 메시지 전송" 우측 상태 버튼 "설정" 클릭
#    -> 팝업화면 "동의 항목 설정" 출력 
#    -> 해당 팝업화면 항목 "동의 단계" 하단 라디오 버튼 "이용 중 동의" 체크
#    -> 해당 팝업화면 항목 "동의 목적 [필수]" 하단에 텍스트 "메시지알림" 입력 
#    -> 버튼 "저장" 클릭
#    -> 1~9번 작업을 통해 "접근권한" -> "카카오톡 메시지 전송"을 
#       "이용 중 동의" 설정하지 않으면 카카오톡 챗봇 나에게 메시지 보내기 작업이 불가하다.
#       하여 "접근권한" -> "카카오톡 메시지 전송"을 "이용 중 동의" 설정을 꼭 해야만 한다. 
# 10. 화면 "내애플리케이션 > 제품 설정 > 카카오 로그인 > 동의항목" 
#     좌측 항목 "앱 설정" 하단 버튼 "앱 키" 클릭 
#     -> 화면 "내 애플리케이션 > 앱 설정 > 앱 키" 이동 
#     -> 카카오톡 챗봇 나에게 메시지 보내기 작업을 처리하기 위해서는 토큰이 필요하다.
#        하여 토큰을 발행하기 위해서 아래와 같은 형식의 URL 주소가 필요하다.
#        "https://kauth.kakao.com/oauth/authorize?client_id=962db08df5361f1b0671ea868d912a11&redirect_uri=http://localhost:9999&response_type=code&scope=talk_message"
#        1) 위의 URL 주소에서 "client_id=" 옆에 문자열 값 "962db08df5361f1b0671ea868d912a11"을 얻으려면
#        화면 "내 애플리케이션 > 앱 설정 > 앱 키" 하단 플랫폼 "REST API 키" 
#        옆에 항목 "앱 키" "962db08df5361f1b0671ea868d912a11" 옆에 버튼 "복사" 클릭 하면 얻을 수 있다.
#        2) 위의 URL 주소에서 "&redirect_uri=" 옆에 문자열 값 "http://localhost:9999"은 8번 과정에서 "Redirect URI"에 입력한 localhost URL 주소이다.
#        위의 URL 주소 텍스트를 복사해서 
#        구글 크롬(Chrome) 웹브라우저에 URL 주소 텍스트 붙여넣으면
#        구글 크롬(Chrome) 웹브라우저에 카카오 챗봇 인증 화면이 출력된다.
#        해당 카카오 챗봇 인증 화면에 "전체 동의하기" 체크 -> 항목 "[선택] 서비스 접근 권한" 하단 "카카오톡 메시지 전송" 체크여부 확인
#        -> "카카오톡 메시지 전송" 체크 되었다면 버튼 "동의하고 계속하기" 클릭
#        -> 구글 크롬(Chrome) 웹브라우저에 화면 상단에 출력된 URL 주소 "http://localhost:9999/?code=kTXOAPzryWiTI42YvRUp9XQeGASdkX7NjpFrXntkZb6NghTYk5Q8bwAAAAQKPXLrAAABlUEGG2qGtS2__sNdBQ" 복사
#        -> 복사한 URL 주소중 "code=" 옆에 문자열 "kTXOAPzryWiTI42YvRUp9XQeGASdkX7NjpFrXntkZb6NghTYk5Q8bwAAAAQKPXLrAAABlUEGG2qGtS2__sNdBQ" 중요하므로 문자열 복사하기 
# 주의사항 - 만일 11~13번 과정에서 작성한 파이썬 스크립트 파일 "01-sendme.py" 컴파일 실행하여
#           함수 save_auth_to_json 호출시 토큰 만료로 인해서 "token.json" 파일에 "error"가 출력된다면
#           위의 1번~10번 과정 처음 부터 다시 진행하기 

# 11. 비쥬얼스튜디오 코드(VSCode) 실행 -> 폴더 경로 "D:\minjae\test_BotProject" 이동 -> 파이썬 스크립트 파일 "01-sendme.py" 열기
#     -> 해당 파이썬 스크립트 파일 "01-sendme.py" 상단에 
#        10번에서 복사한 "code=" 옆에 문자열 "kTXOAPzryWiTI42YvRUp9XQeGASdkX7NjpFrXntkZb6NghTYk5Q8bwAAAAQKPXLrAAABlUEGG2qGtS2__sNdBQ" 
#        사용해서 아래처럼 코드 작성하기
# CODE = "kTXOAPzryWiTI42YvRUp9XQeGASdkX7NjpFrXntkZb6NghTYk5Q8bwAAAAQKPXLrAAABlUEGG2qGtS2__sNdBQ"
# 12. 11번에서 열은 파이썬 스크립트 파일 "01-sendme.py"을 아래처럼 구현하기 
# 주의사항 : 
# 1) Kakao Developers 웹사이트 화면 "내 애플리케이션 > 앱 설정 > 앱 키"에 속한 항목 "REST API 키" 옆의 키값 "962db08df5361f1b0671ea868d912a11" 복사해서 
#    함수 "save_auth_to_json" -> 변수 data에 속한 항목 "client_id"에 값 할당하기 
# 2) 11번의 문자열 "kTXOAPzryWiTI42YvRUp9XQeGASdkX7NjpFrXntkZb6NghTYk5Q8bwAAAAQKPXLrAAABlUEGG2qGtS2__sNdBQ" 복사해서
#    함수 "save_auth_to_json" -> 변수 data에 속한 항목 "code"에 값 할당하기 

# 13. Kakao Developers 웹사이트 화면 상단 버튼 "문서" 클릭 
#     -> 화면 "문서" 이동 -> 해당 화면 좌측 항목 "커뮤니케이션" 하단 항목 "메시지" 클릭
#     -> 버튼 "카카오톡 메시지: REST API" 클릭 
#     -> 화면 "문서 > 메시지 > 카카오톡 메시지: REST API" 이동
#     -> 마우스 스크롤바 아래도 내려서 항목 "3. 메시지 전송 대상 선택하기" 하위에 속하는 내용 읽어보기
#     -> 항목 "참고: 선택 조건별 필요한 API" 하위 항목 "전송대상" "나에게 보내기" 옆에 항목 "API" 중 "기본 템플릿으로 메시지 보내기" 클릭
#     -> 화면 "나에게 보내기" 이동 -> 해당 화면에 적힌 내용은 "나에게 보내기" 기능을 실행하기 위한 Rest API 명세서 이므로 다 읽어봐야 한다.
#     -> 화면 "문서 > 메시지 > 카카오톡 메시지: REST API" 다시 돌아와서
#     -> 항목 "나에게 보내기" -> 하위 항목 "URL"에 적혀있는 URL 주소 "https://kapi.kakao.com/v2/api/talk/memo/default/send" 복사 
#     -> 함수 "send_message"에 속한 변수 "url"에 
#        복사한 URL 주소 "https://kapi.kakao.com/v2/api/talk/memo/default/send" 아래처럼 붙여넣기
#        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" 
#     -> 화면 "문서 > 메시지 > 카카오톡 메시지: REST API" 다시 돌아와서
#     -> 항목 "나에게 보내기" -> 하위 항목 "요청" -> 하위 항목 "헤더"에 속한 이름 "Authorization"과 설명 "Authorization: Bearer ${ACCESS_TOKEN}" 복사
#        함수 "send_message"에 속한 변수 "headers"에 위에서 복사한 값 아래처럼 붙여넣기
#        headers = {"Authorization": f"Bearer {access_token}"}
import requests
import json

# TODO : 함수 json.load() / json.dump() 사용해서 json 데이터 처리 기능 구현 (2025.02.26 minjae)
# json 관련 함수 기능
# 1) json.load(json 파일 객체) - json 파일을 읽어서 딕셔너리(dictionary) 객체로 변환
# 2) json.dump(딕셔너리, json 파일 객체) - 딕셔너리(dictionary) 객체를 JSON 파일로 생성
# 참고 URL - https://wikidocs.net/126088

# 인증 토큰 처음 생성 및 json 파일 "token.json"에 쓰기 및 저장
def save_auth_to_json():
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": "962db08df5361f1b0671ea868d912a11",
        "redirect_uri": "http://localhost:9999",
        "code": "kTXOAPzryWiTI42YvRUp9XQeGASdkX7NjpFrXntkZb6NghTYk5Q8bwAAAAQKPXLrAAABlUEGG2qGtS2__sNdBQ"
    }
    # HTTP - POST 통신 실행 
    response = requests.post(url, data=data)
    # 함수 response.json() 실행 
    # -> 서버가 반환한 결과(response)를 json 형식의 데이터로 변환
    # -> 해당 json 형식 데이터를 변수 token에 저장 
    token = response.json()
    # with문 + 함수 json.dump() 실행하여 
    # 변수 token에 저장된 json 형식 데이터를
    # 파일 "token.json"에 그대로 쓰고(쓰기모드 - "w") 저장하기 
    with open("token.json", "w", encoding="utf-8") as f:
        json.dump(token, f)

# 파일 "token.json" 읽어서 토큰(token) 변수 반환
def load_json():
    # with문 + 함수 json.load() 실행하여 
    # 파일 "token.json"에 저장된 json 형식 데이터를
    # 그대로 읽어와서(읽기모드 - "r") 변수 token에 저장하기 
    # 파일 "token.json"에 저장된 json 형식 데이터들 중
    # 액세스 토큰(access token)이 필요하다.
    # 단, 액세스 토큰(access token)의 유효시간은 기본적으로 21,599초(대략 6시간)이다.
    with open("token.json", "r", encoding="utf-8") as f:
        token = json.load(f)
    return token

# 파일 "token.json"에 저장된 액세스 토큰(access token)
# 유효기간 21,599초(대략 6시간) 지나고나서 
# 액세스 토큰(access token) 토큰 만료시
# 토큰(refresh_token) 갱신 처리 
def refresh_token(tokens):
    # json 형식 데이터가 저장된 변수 tokens에서
    # 항목 "refresh_token"에 매핑된 값 가져오기 
    r_token = tokens.get("refresh_token")
    # 변수 r_token에 저장된 값이 존재하는 경우 
    # 액세스 토큰(access token) 갱신 처리 진행 
    if r_token is not None:
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "refresh_token",
            "client_id": "962db08df5361f1b0671ea868d912a11",
            "refresh_token": r_token
        }
        # HTTP - POST 통신 
        response = requests.post(url, data=data)
        # 함수 response.json() 실행 
        # -> 서버가 반환한 결과(response)를 json 형식의 데이터로 변환
        # -> 해당 json 형식 데이터를 변수 receive_token에 저장 
        receive_token = response.json()
        # for 반복문 실행
        # 함수 receive_token.items() 실행하여 키(k)와 값(v) 분리해서
        # 아래 코드 tokens[k] = v 실행하여 값 저장 
        for k, v in receive_token.items():
            tokens[k] = v
        # with문 + 함수 json.dump() 실행하여 
        # 변수 tokens에 저장된 json 형식 데이터를
        # 파일 "token.json"에 그대로 쓰고(쓰기모드 - "w") 저장하기 
        with open("token.json", "w", encoding="utf-8") as f:
            json.dump(tokens, f)
    return tokens   # 변수 tokens 리턴 

# 카카오톡 챗봇으로 나에게 메시지 보내기  
def send_message():
    # 함수 load_json() 호출하여 파일 "token.json" 읽어서 토큰(token) 변수 반환
    # 반환된 토큰(token) 변수를 함수 refresh_token()에 인자로 전달하여
    # 갱신된 토큰(refresh_token) 리턴 및 변수 tokens에 저장 
    tokens = refresh_token(load_json())
    # 변수 tokens에 저장된 json 데이터들 중 
    # 항목 "access_token"에 저장된 값 반환하여
    # 변수 access_token에 저장 
    access_token = tokens.get("access_token")
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        # template_object는 메시지 구성 요소를 담은 객체(Object)
        # 피드, 리스트, 위치, 커머스, 텍스트, 캘린더 중 하나 의미
        "template_object": json.dumps({
            # 항목 "object_type"에는 "text" 할당 
            "object_type": "text",
            "text": "테스트 메세지",
            "link": {
                "web_url": "https://blog.naver.com/nkj2001"
            }
        })
    }
    # HTTP - POST 통신 
    r = requests.post(url, headers=headers, data=data)

    # 함수 r.json().get("result_code") 실행 
    # -> 서버가 반환한 결과(r)를 json 형식의 데이터로 변환
    # -> 해당 json 형식 데이터에 속한 항목 "result_code"에 저장된 값 가져오기 
    # json 형식 데이터에 
    # 속한 항목 "result_code"에 저장된 값이 0인 경우 
    if r.json().get("result_code") == 0:
        print("전송 성공!!")
    # json 형식 데이터에 
    # 속한 항목 "result_code"에 저장된 값이 0이 아닌 경우 
    else:
        # 함수 str(r.json()) 실행 
        # -> 서버가 반환한 결과(r)를 json 형식의 데이터로 변환 -> 문자열 변환 및 출력 
        print(f"전송 실패: {str(r.json())}")

# 카카오톡 챗봇으로 위치정보를 나에게 메시지 보내기  
def send_location():
    # 함수 load_json() 호출하여 파일 "token.json" 읽어서 토큰(token) 변수 반환
    # 반환된 토큰(token) 변수를 함수 refresh_token()에 인자로 전달하여
    # 갱신된 토큰(refresh_token) 리턴 및 변수 tokens에 저장
    tokens = refresh_token(load_json())
    # 변수 tokens에 저장된 json 데이터들 중 
    # 항목 "access_token"에 저장된 값 반환하여
    # 변수 access_token에 저장 
    access_token = tokens.get("access_token")
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        # template_object는 메시지 구성 요소를 담은 객체(Object)
        # 피드, 리스트, 위치, 커머스, 텍스트, 캘린더 중 하나 의미
        "template_object": json.dumps({
            # 항목 "object_type"에는 "location" 할당  
            "object_type": "location",
            "text": "테스트 위치정보 입니다.\n테스트 메세지",
            "address": "경기 성남시 분당구 판교역로 235",
            "content": {
                "title": "지도보기",
                "image_url": "https://cdn.pixabay.com/photo/2018/04/13/16/35/earth-3316984_960_720.png",
                "image_width": 960,
                "image_height": 720,
                "link": {
                    "web_url": ""
                }
            }
        })
    }
    # HTTP - POST 통신 
    r = requests.post(url, headers=headers, data=data)
    # 함수 r.json().get("result_code") 실행 
    # -> 서버가 반환한 결과(r)를 json 형식의 데이터로 변환
    # -> 해당 json 형식 데이터에 속한 항목 "result_code"에 저장된 값 가져오기 
    # json 형식 데이터에 
    # 속한 항목 "result_code"에 저장된 값이 0인 경우 
    if r.json().get("result_code") == 0:
        print("전송 성공!!")
    # json 형식 데이터에 
    # 속한 항목 "result_code"에 저장된 값이 0이 아닌 경우 
    else:
        # 함수 str(r.json()) 실행 
        # -> 서버가 반환한 결과(r)를 json 형식의 데이터로 변환 -> 문자열 변환 및 출력
        print(f"전송 실패: {str(r.json())}")

# 카카오 챗봇 프로그램 실행시 처음 한번 함수 save_auth_to_json() 호출 되야함
# save_auth_to_json() 
# send_message()
send_location()


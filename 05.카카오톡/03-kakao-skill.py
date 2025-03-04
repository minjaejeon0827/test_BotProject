# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 파이썬 웹서버 flask 라이브러리 "Flask" 설치 및 사용하기
# 참고 URL - https://pypi.org/project/Flask/
# pip install Flask

# 파이썬 파이썬 스크립트 파일 "03-kakao-skill.py"에서
# 자체적으로 구현한 파이썬 웹서버 flask 실행시
# 팝업화면 "Windows 보안 경고" 출력시 "공항, 커피숍 등의 공용 네트워크(U)" 체크 -> 버튼 "액세스 허용(A)" 클릭
# 참고 URL - https://m.blog.naver.com/myrikason/221156362651

from flask import Flask, request, jsonify
from modules import weather
from pprint import pprint

app = Flask(__name__)

@app.route("/weather", methods=["POST"])
def get_weather():
    # 카카오톡 서버 -> 파이썬 파이썬 스크립트 파일 "03-kakao-skill.py"에서
    # 자체적으로 구현한 파이썬 웹서버 flask에
    # json 형태로 데이터 전달 및 변수 content에 할당 
    content = request.get_json()
    pprint(content)
    intent = content.get("intent")
    action = content.get("action")
    sys_location = "서울"
    if action:   # action이 있는 경우 
        if action.get("detailParams").get("sys_location") is not None:
            sys_location = action.get("detailParams").get("sys_location").get("origin")
    results = weather.get_weather(sys_location)
    output = ""
    for k, v in results.items():
        output += f"{k}: {v}\n"
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": output
                    }
                }
            ]
        }
    })

@app.route("/test")
def test():
    return "OK"

if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True, port=9034)
    # 함수 app.run() 호출시 매개변수 host에 인자값 "0.0.0.0"으로 전달해야
    # 외부(카카오톡) 서버가 파이썬 스크립트 파일 "03-kakao-skill.py"에서
    # 자체적으로 구현한 파이썬 웹서버 flask에 접속을 할 수 있다.
    # 작업을 할 때 편리하게 하기 위해서 매개변수 debug에는 인자값 "True"로 주고,
    # 매개변수 port는 개발자가 사용하는 PC 환경에서 
    # 사용하지 않는(중복되지 않는) 빈 포트(port) 인자값 "8763"으로 전달해야 한다.
    app.run(host="0.0.0.0", debug=True, port=8763)
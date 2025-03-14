from flask import Flask, request, jsonify, send_from_directory
from modules import qrcode
from pprint import pprint
import urllib.request
import cv2   # OpenCV 라이브러리 "cv2" 읽어오기 

app = Flask(__name__)   # Flask 클래스 객체 app 생성 

@app.route("/qrcode_encode", methods=["POST"])
def qrcode_encode():
    # 카카오톡 서버가 보내준 데이터(request)를 json 형태로 변환(get_json) 및 변수 content에 할당
    content = request.get_json()
    pprint(content)
    url = content.get("action").get("detailParams").get("URL").get("origin")
    qr_image = qrcode.QRCreater().make(url).png()   # QRCODE를 .png 파일로 생성
    filename = qr_image.split("\\")[-1]
    qr_url = f"http://192.168.0.21:8763/image/{filename}"
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    # 이미지를 출력하는 템플릿 항목 "simpleImage"
                    "simpleImage": {
                        "altText": "큐알코드",
                        "imageUrl": qr_url
                    }
                }
            ],
        }
    })

@app.route("/image/<path:file>")
def get_image(file):
    return send_from_directory("modules", file)

@app.route("/qrcode_decode", methods=["POST"])
def qrcode_decode():
    content = request.get_json()
    pprint(content)
    image = content.get("action").get("detailParams").get("이미지")
    image_list = image.get("origin")
    if image_list[0:4] == "List":
        image_list = image_list[5:-1].split(",")
    output = ""
    for img in image_list:
        urllib.request.urlretrieve(img, "qr.png")
        cv_image = cv2.imread("qr.png")
        if cv_image is not None:   # OpenCV 라이브러리 "cv2"로 읽어온 이미지(cv_image)가 문제가 없다면 
            result = qrcode.read_qrcode_zbar(cv_image)
            output += f"{result[0].get('data')}\n"
        else:   # OpenCV 라이브러리 "cv2"로 읽어온 이미지(cv_image)가 문제가 있다면
            output += "QR코드를 찾을 수 없습니다.\n"
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": output
                    }
                }
            ],
        }
    })

@app.route("/qrcode", methods=["POST"])
def get_qrcode():
    result_json = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "메뉴를 선택하세요."
                    }
                }
            ],
            "quickReplies": [
                {
                    "action": "block",
                    "blockId": "67ce7a2fa6c9712a60f5a37c",
                    "label": "QR코드 해석하기"
                },
                {
                    "action": "block",
                    "blockId": "67ce7a1753748b3e0cb146c6",
                    "label": "QR코드 만들기"
                }
            ]
        }
    }
    return jsonify(result_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8763)
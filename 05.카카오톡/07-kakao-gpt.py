from flask import Flask, request, jsonify
from pprint import pprint
from youtube_transcript_api import YouTubeTranscriptApi
import re
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 자연어 처리할 라이브러리 "kiwipiepy" 설치 및 사용하기
# pip install kiwipiepy
# 참고 URL - https://bab2min.github.io/kiwipiepy/v0.20.4/kr/
from kiwipiepy import Kiwi
from dotenv import load_dotenv
import os
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 OpenAI 라이브러리 "openai" 설치 및 사용하기
# pip install openai
from openai import OpenAI
import requests
import threading

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=OPENAI_KEY)
app = Flask(__name__)

def get_chat_complete(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def is_youtube_url(text):
    pattern = r"(https?://)?(www\.)?youtube\.com/watch\?v=([\w-]+)(&\S*)?|youtu\.be/([\w-]+)"
    match = re.match(pattern, text)
    if match:
        return match.group(3) or match.group(5)
    else:
        return None

def get_transcript(video_id, languages=["en"]):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(languages)
    return transcript.fetch()

def get_youtube_transcript(vid, callback_url):
    transcript = get_transcript(vid, languages=['ko'])
    if transcript is not None:
        output = ""
        for t in transcript:
            output += f"{t.get('text')}"
        kiwi = Kiwi()   # Kiwi 클래스 객체 kiwi 생성 
        sents = kiwi.split_into_sents(output)
        output = "\n".join([s.text for s in sents])
        prompt = f'"""{output}"""\n\n위의 내용을 300자 내외로 요약해주세요.'
        summary = get_chat_complete(prompt)
        output = summary
        c = requests.post(callback_url, json={
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
        print(c.status_code, c.json())

@app.route("/fallback", methods=["POST"])
def fallback_skill():
    content = request.get_json()
    output = "죄송합니다. 알아듣지 못했습니다."
    pprint(content)
    user_request = content.get("userRequest")
    callback_url = user_request.get("callbackUrl")
    if user_request:
        utterance = user_request.get("utterance")
        vid = is_youtube_url(utterance)
        if vid is not None:
            threading.Thread(target=get_youtube_transcript, args=(vid, callback_url)).start()
            return jsonify({
                "version": "2.0",
                "useCallback": True,
                "data": {
                    "text": "처리 중입니다. 잠시 기다려 주세요.."
                }
            })
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8763)
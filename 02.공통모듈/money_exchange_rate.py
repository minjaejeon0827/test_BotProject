# TODO : Git SourceTree로 Git Push 진행시 아래와 같은 오류 메시지 출력되면
#        아래와 같은 방법으로 해결 해야함 (2025.02.18 minjae)
# 참고 URL - https://velog.io/@nies/git%EC%97%90-push%ED%95%98%EB%A0%A4%EB%8A%94%EB%8D%B0-remote-Permission-to-git%EC%A3%BC%EC%86%8C-denied-to-user%EC%9D%B4%EB%A6%84-403-error-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-AI-%EC%9B%B9-%EA%B0%9C%EB%B0%9C-%EB%8B%A4%EC%84%AF%EC%A7%B8-%EC%A3%BC2%EC%9D%BC%EC%B0%A8
# 오류 메시지 - git -c diff.mnemonicprefix=false -c core.quotepath=false --no-optional-locks push -v origin main:main
# remote: Permission to minjaejeon0827/BotProject.git denied to bonghakjeon.
# fatal: unable to access 'https://github.com/minjaejeon0827/BotProject.git/': The requested URL returned error: 403
# Pushing to https://github.com/minjaejeon0827/BotProject.git
# 오류가 나면서 완료됨. 

# 파이썬 버전 파이썬 3.12.2 설치 방법
# 참고 URL - https://coding-is-fun.tistory.com/16

# 파이썬 패키지 "BeautifulSoup" 활용하여 웹크롤링 하기 
# 참고 URL - https://goldhong.tistory.com/55

# 파이썬 소스코드로 HTML 파일(.html) 웹브라우저로 불러오기(열기) 
# 참고 URL - https://wikidocs.net/227577
# 참고 2 URL - https://wikidocs.net/177248
# 참고 3 URL - https://whitewing4139.tistory.com/298
# 참고 4 URL - https://sens.tistory.com/534
# 참고 5 URL - https://roadofdevelopment.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B8%B0%EC%B4%88open-%ED%95%A8%EC%88%98%EB%A1%9C-%ED%8C%8C%EC%9D%BC-%EC%9D%BD%EA%B8%B0
# 참고 6 URL - https://codetorial.net/python/file_handling.html
# 참고 7 URL - https://wikidocs.net/16077

# 명령프롬프트(cmd) 실행 -> 터미널 창에 파일 경로 "C:\Users\bhjeon" 설정 
# -> 명령어 "pip install requests lxml beautifulSoup4" 입력 및 엔터
# -> 패키지 3가지 "requests / lxml / beautifulSoup4" 설치 완료 

# 파이썬 터미널창 실행 -> 터미널 창에 아래처럼 명령어 입력 및 엔터
# pip install python-dotenv

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import re

load_dotenv()
KBANK_API_KEY = os.getenv("KBANK_API_KEY")

CURRENCY_LIST = {
    "AED": {
        "country": "아랍에미리트",
        "aliases": "디르함, dirham"
    },
    "ATS": {
        "country": "오스트리아",
        "aliases": "실링, schilling"
    },
    "AUD": {
        "country": "호주",
        "aliases": "호주 달러, australian dollar"
    },
    "BEF": {
        "country": "벨기에",
        "aliases": "프랑, franc"
    },
    "BHD": {
        "country": "바레인",
        "aliases": "디나르, dinar"
    },
    "CAD": {
        "country": "캐나다",
        "aliases": "캐나다 달러, canadian dollar"
    },
    "CHF": {
        "country": "스위스",
        "aliases": "프랑, franc"
    },
    "CNH": {
        "country": "중국",
        "aliases": "위안화, yuan"
    },
    "DEM": {
        "country": "독일",
        "aliases": "마르크, mark"
    },
    "DKK": {
        "country": "덴마크",
        "aliases": "크로네, krone"
    },
    "ESP": {
        "country": "스페인",
        "aliases": "페세타, peseta"
    },
    "EUR": {
        "country": "유로존",
        "aliases": "유로, euro"
    },
    "FIM": {
        "country": "핀란드",
        "aliases": "마르카, markka"
    },
    "FRF": {
        "country": "프랑스",
        "aliases": "프랑, franc"
    },
    "GBP": {
        "country": "영국",
        "aliases": "파운드, pound"
    },
    "HKD": {
        "country": "홍콩",
        "aliases": "홍콩 달러, hong kong dollar"
    },
    "IDR": {
        "country": "인도네시아",
        "aliases": "루피아, rupiah"
    },
    "ITL": {
        "country": "이탈리아",
        "aliases": "리라, lira"
    },
    "JPY": {
        "country": "일본",
        "aliases": "엔, yen"
    },
    "KRW": {
        "country": "한국",
        "aliases": "원, won"
    },
    "KWD": {
        "country": "쿠웨이트",
        "aliases": "디나르, dinar"
    },
    "MYR": {
        "country": "말레이시아",
        "aliases": "링기트, ringgit"
    },
    "NLG": {
        "country": "네덜란드",
        "aliases": "길더, guilder"
    },
    "NOK": {
        "country": "노르웨이",
        "aliases": "크로네, krone"
    },
    "NZD": {
        "country": "뉴질랜드",
        "aliases": "뉴질랜드 달러, new zealand dollar"
    },
    "SAR": {
        "country": "사우디아라비아",
        "aliases": "리얄, riyal"
    },
    "SEK": {
        "country": "스웨덴",
        "aliases": "크로나, krona"
    },
    "SGD": {
        "country": "싱가포르",
        "aliases": "싱가포르 달러, singapore dollar"
    },
    "THB": {
        "country": "태국",
        "aliases": "바트, baht"
    },
    "USD": {
        "country": "미국",
        "aliases": "달러, 미국달러, 달라, dollar"
    },
    "XOF": {
        "country": "서아프리카",
        "aliases": "씨에프에이 프랑, cfa franc"
    }
}

# 구글로 환율 구하기
def google_money_exchange_rate(search, to="원"):
    url = f"https://www.google.com/search?q={search}+{to}"
    # 아래 변수 headers에 할당된 값 중 항목 "User-Agent"에 할당된 값은
    # 사용자가 어떤 브라우저 혹은 핸드폰(스마트폰)으로 접속을 할 수도 있고
    # 여러 가지 브라우저 개체로 접속을 했을 때, 어떤 브라우저로 접속을 했는지를
    # 인식할 수 있는 하나의 값을 의미한다.
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    # 위에 변수 headers에 저장된 접속 정보(웹브라우저 또는 모바일)를 가지고
    # 아래처럼 변수 url에 할당된 URL 주소로
    # HTTP - GET 방식(requests.get(url, headers=headers))으로 호출
    # 단, 변수 url에 할당된 URL 주소로 접속할 때 헤더 정보(headers)도
    #     같이 인자로 넘겨준다.
    # 해당 함수(requests.get) 실행 결과값은 구글 서버가 반환해준 값을 의미하며, 
    # 해당 결과값을 변수 r에 저장 
    r = requests.get(url, headers=headers)
    # BeautifulSoup 클래스 객체 bs 생성해서 
    # r.text의 내용을 "lxml" 파서(Parser)를 통해서 구문분석한 결과를
    # BeautifulSoup 클래스 객체 bs에 저장 
    bs = BeautifulSoup(r.text, "lxml")
    # 객체 bs에 저장된 html 요소를 찾기 위해 함수 find 호출 
    # 객체 bs에 저장된 html 요소들 중에서 
    # 특정 html 요소(<div>)이면서 해당 요소의 
    # 속성(attrs) "data-exchange-rate"의 값이 True인 요소만
    # ("data-exchange-rate"의 값이 존재하는 경우)
    # 모두 가져와서(찾아와서 - find) 변수 div에 저장 
    div = bs.find("div", attrs={"data-exchange-rate": True})
    # 특정 html 요소(<div>)들이 존재하는 경우(> 0)
    if len(div) > 0:
        # 특정 html 요소(<div>)의 자식 html 요소(<span>)중
        # 속성(attrs) "data-name"의 값이 True인 요소만
        # ("data-name"의 값이 존재하는 경우)
        # 모두 가져와서(찾아와서 - find) 변수 names에 저장
        names = div.find_all("span", attrs={"data-name": True})
        # 특정 html 요소(<div>)의 자식 html 요소(<span>)중
        # 속성(attrs) "data-value"의 값이 True인 요소만
        # ("data-value"의 값이 존재하는 경우)
        # 딱 하나만 가져와서(찾아와서 - find) 변수 money에 저장
        money = div.find("span", attrs={"data-value": True})
        # 변수 money, names에 저장된 텍스트 문자열을 튜플로 묶어서 리턴 
        return (money.text, names[0].text, names[1].text)
    # 특정 html 요소(<div>)들이 존재하지 않는 경우(<= 0)
    # 오류가 발생하면 안 되니까 아래처럼 의미없는 값 리턴(return (0, None, None))
    return (0, None, None)

# 네이버로 환율 구하기
def naver_money_exchange_rate(search, to="원"):
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={search}+{to}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, "lxml")
    # <span> 태그 속성 class에 값이 "nt_eng._code"인 요소 가져오기
    source = bs.select_one("span.nt_eng._code")
    # <span> 태그 속성 class에 값이 "nb_txt._pronunciation"인 요소 가져오기
    target = bs.select_one("span.nb_txt._pronunciation")
    # <input> 태그 속성 id 값이 "num"인 요소들 가져오기 
    inputs = bs.select("input#num")
    # <input> 태그 속성 id 값이 "num"인 요소가 2개인 경우
    if len(inputs) == 2:
        money = inputs[1].get("value")
        return (money, source.text, target.text)
    return (0, None, None)

def kbank_money_exchanage_rate_init():
    url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={KBANK_API_KEY}&searchdate=20180102&data=AP01"
    # 변수 url에 저장된 URL 주소로 HTTP - GET 요청 진행 
    #  HTTP - GET 요청 진행한 결과 변수 r에 저장 
    r = requests.get(url)
    # 함수 r.json() 호출하여 변수 r에 저장된 문자열을 json List 형태로 변환후 변수 result에 저장 
    result = r.json() 
    ouput = ""
    # json List 형태인 변수 result를 가지고 반복문 for 실행 
    for item in result:
        # 변수 item에 있는 요소 가져오기
        cur_unit = item.get("cur_unit")
        cur_nm = item.get("cur_nm")
        deal_bas_r = item.get("deal_bas_r")
        CUR = CURRENCY_LIST.get(cur_unit)
        # 변수 CUR에 할당된 값이 None이 아닌 경우 
        if CUR is not None:
            CUR.update({
                "deal_bas_r": deal_bas_r
            })

def money_exchange_rate(search, to=None):
    try:
        # 변수 numbers에 변수 search에 저장된 숫자 할당
        numbers = re.findall(r'\d+', search)[0]
        # 변수 strings에 변수 search에 저장된 문자열 할당 
        strings = re.findall(r'[^\d\s]+', search)[0]
    except:
        # 변수 search에 저장된 숫자와 문자열 분리 실패한 경우 
        return (0, None, None)
    
    for key, value in CURRENCY_LIST.items():
        if strings in value.get("aliases"):
            dbr = value.get("deal_bas_r").replace(",", "")
            kor = float(dbr) * float(numbers)
        
            if to is None:
                return (kor, value.get("country"), value.get("country"))
            else:
                for k, v in CURRENCY_LIST.items():
                    if to in value.get("aliases"):
                        tbr = value.get("deal_bas_r")
                        key = value.get("country")
                        return (kor / float(tbr), key, key)
    return (0, None, None)

if __name__ == "__main__":
    google_money_exchange_rate()
    # kbank_money_exchanage_rate_init()
    print(money_exchange_rate("900달러"))

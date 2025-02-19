import requests  # 기상청 웹사이트와 HTTP - GET 방식으로 통신해서 데이터 가져와야 해서 패키지 "requests" 가져오기 
from bs4 import BeautifulSoup

# def get_testweather(keyword):
#     url = f"https://www.weather.go.kr/w/renew2021/rest/main/place-search.do?query={keyword}&start=1&src=A2"
#     # 기상청 웹사이트로 부터 데이터 받아오기 위해 HTTP - GET 방식 통신 진행 
#     r = requests.get(url)
#     # 함수 r.json() 호출하여 변수 r에 저장된 문자열을 json List 형태로 변환후 변수 _json에 저장 
#     _json = r.json()
#     print(_json)

#     url = "https://www.weather.go.kr/w/wnuri-fct2021/main/current-weather.do?code=1171071000"

def get_weather(keyword):
    url = f"https://www.weather.go.kr/w/renew2021/rest/main/place-search.do?query={keyword}&start=1&src=A2"
    # 기상청 웹사이트로 부터 데이터 받아오기 위해 HTTP - GET 방식 통신 진행 
    r = requests.get(url)
    # 함수 r.json() 호출하여 변수 r에 저장된 문자열을 json List 형태로 변환후 변수 _json에 저장 
    _json = r.json()
    # print(_json)
    _data = None   # 변수 _data를 None으로 초기화 
    # 변수 _json에 들어있는 json List 데이터들을 for문으로 반복해서 방문
    for j in _json:
        # 변수 j 안에 있는 json 데이터(Object)에서 항목 "address"에 매핑된 값을 가져오기
        address = j.get("address")
        # 변수 address에 할당된 사용자가 입력한 주소가 있는 경우 
        if address.find(keyword) >= 0:
            _data = j # 변수 j에 저장된 값을 변수 _data에 저장 
            break

    # 변수 _data에 저장된 데이터가 존재하는 경우 
    if _data:
        # 변수 _data 안에 있는 json 데이터(Object)에서 항목 "dongCode"에 매핑된 값을 가져오기
        dong = _data.get("dongCode")
        # 아래 변수 url에 URL 주소 + 변수 dong 문자열로 연결 및 저장 
        url = f"https://www.weather.go.kr/w/wnuri-fct2021/main/current-weather.do?code={dong}"
        # 위에 변수 url에 저장된 URL 주소에서 데이터 받아오기 위해 HTTP - GET 방식 통신 진행 
        r = requests.get(url)
        # print(r.text)
        # 웹크롤링 하기 위해 BeautifulSoup 클래스 객체 bs 생성 및  
        # 생성자 BeautifulSoup에 인자 전달 
        # 전달한 인자 (r.text - html 코드 / "lxml" - 파서(Parser))
        bs = BeautifulSoup(r.text, "lxml")

        # "span.tmp" - 속성 "class" 값이 "tmp"인 <span> 태그 요소
        # bs.select_one("span.tmp") - <span class="tmp"> 태그인 요소 1개만 선택해서 가져오기 
        _span_tmp = bs.select_one("span.tmp")
        # "span.minmax" - 속성 "class" 값이 "minmax"인 <span> 태그 요소
        # _span_tmp.select("span.minmax > span") - <span class="minmax"> 태그 하위의 <span> 태그 여러 개 구하기  
        _span_minmax = _span_tmp.select("span.minmax > span")
        # <span class="minmax"> 태그 하위의 두번째 <span> 태그 요소의 텍스트 가져오기
        _min_temp = _span_minmax[1].text
        # <span class="minmax"> 태그 하위의 네번째 <span> 태그 요소의 텍스트 가져오기
        _max_temp = _span_minmax[3].text
        _span_tmp.span.decompose()
        # print(_span_tmp)   # decompose되었는지 출력해서 확인
        _temp = _span_tmp.text

        # "span.ic-hm" - 속성 "class" 값이 "ic-hm"인 <span> 태그 요소
        _ic_hm = bs.select_one("span.ic-hm")
        # "span.val" - 속성 "class" 값이 "val"인 <span> 태그 요소
        # _ic_hm_val.parent - <span class="_ic_hm_val"> 의 부모요소 접근
        _ic_hm_val = _ic_hm.parent.select_one("span.val").text
        # print(_ic_hm_val)
        # print(_temp, _ic_hm_val, _min_temp, _max_temp)
        # "span.ic-wind" - 속성 "class" 값이 "ic-wind"인 <span> 태그 요소
        _ic_wind = bs.select_one("span.ic-wind")
        # "span.val" - 속성 "class" 값이 "val"인 <span> 태그 요소
        # _ic_wind.parent - <span class="_ic_wind"> 의 부모요소 접근
        _ic_wind_val = _ic_wind.parent.select_one("span.val").text

        # "span.ic-rn" - 속성 "class" 값이 "ic-rn"인 <span> 태그 요소
        _ic_rn = bs.select_one("span.ic-rn")
        # "span.val" - 속성 "class" 값이 "val"인 <span> 태그 요소
        # _ic_rn.parent - <span class="_ic_rn"> 의 부모요소 접근
        _ic_rn_val = _ic_rn.parent.select_one("span.val").text

        # "span.sunrise" - 속성 "class" 값이 "sunrise"인 <span> 태그 요소
        # _sunrise.parent - <span class="_sunrise"> 의 부모요소 접근
        # select("span")[1].text - _sunrise.parent 부모 요소 하위의 인덱스 1번지의 <span> 태그의 text 값 구하기
        _sunrise = bs.select_one("span.sunrise").parent.select("span")[1].text
        
        # "span.sunset" - 속성 "class" 값이 "sunset"인 <span> 태그 요소
        # _sunset.parent - <span class="_sunset"> 의 부모요소 접근
        # select("span")[1].text - _sunset.parent 부모 요소 하위의 인덱스 1번지의 <span> 태그의 text 값 구하기
        _sunset = bs.select_one("span.sunset").parent.select("span")[1].text

        # "span.air-lvv" - 속성 "class" 값이 "air-lvv"인 <span> 태그 요소
        _air_spans_v = bs.select("span.air-lvv")
        # "span.air-lvt" - 속성 "class" 값이 "air-lvt"인 <span> 태그 요소
        _air_spans_t = bs.select("span.air-lvt")

        for a in _air_spans_t:
            # a.a 링크(속성 href)를 decompose 사용하여 제거
            a.a.decompose()
        
        # 딕셔너리(Dictionary) 객체 _air_levels 선언 및 데이터 "초미세먼지", "미세먼지", "오존" 할당 
        _air_levels = {
            "초미세먼지": f"{_air_spans_v[0].text}({_air_spans_t[0].text})",
            "미세먼지": f"{_air_spans_v[1].text}({_air_spans_t[1].text})",
            "오존": f"{_air_spans_v[2].text}({_air_spans_t[2].text})",
        }
        # print(_air_levels)
        
        # 딕셔너리(Dictionary) 형태로 리턴 
        return {
            "😁기존": _temp,
            "최저": _min_temp,
            "최고": _max_temp,
            "습도": _ic_hm_val,
            "바람": _ic_wind_val,
            "강수량": _ic_rn_val,
            "일출": _sunrise,
            "일몰": _sunset,
            "대기질": _air_levels
        }
    return None   # 정상적으로 처리되지 않았을 경우 None 리턴 

if __name__ == "__main__":
    # get_weather("서울")
    # get_testweather("서울")
    print(get_weather("서울"))
# 영화를 검색해서 결과를 반환해주는 모듈 구현

import requests
from bs4 import BeautifulSoup


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# 사용자가 챗봇을 통해서 어떤 영화 제목을 입력하면
# 해당 영화 제목을 다음(daum)에서 검색 하고 정보를 구해서 
# 그것을 디스코드, 텔레그램, 카카오톡 등등... 에도
# 정보를 공유해주는 기능
def search_movie_daum(keyword):
    url = f"https://search.daum.net/search?w=cin&q={keyword}&DA=EM1&rtmaxcoll=EM1&irt=movie-single-tab"
    # HTTP - GET 통신하여 
    # 사용자가 입력한 영화 제목이 담긴 변수 keyword와 변수 header를 
    # 함수 requests.get에 인자로 전달하여 
    # 사용자가 입력한 영화 제목에 대한 정보를 다음(daum)에서 검색 및 정보 구하기  
    r = requests.get(url, headers=header)
    # print(r.text)
    # BeautifulSoup 클래스 객체 bs 생성해서 
    # r.text의 내용을 "lxml" 파서(Parser)를 통해서 구문분석한 결과를
    # BeautifulSoup 클래스 객체 bs에 저장 
    bs = BeautifulSoup(r.text, "lxml")
    # <c-container> 태그 요소 하나 가져오기
    c = bs.select_one("c-container")
    # print(c)
    # <c-container> 태그 하위에 속한 <c-title> 태그 요소 하나 가져오기
    c_title = c.select_one("c-title")
    # print(c_title)
    # <c-container> 태그 하위에 속한 <c-doc-content> 태그 요소 하나 가져오기
    c_content = c.select_one("c-doc-content")
    # print(c_content)
    # <c-doc-content> 태그 하위에 속한 <c-thumb> 태그 요소 하나 가져오기
    c_thumb = c_content.select_one("c-thumb")
    print(c_thumb)
    # <c-doc-content> 태그 하위에 속한 <c-list-grid-desc> 태그 요소 하나 가져오기 
    c_list = c_content.select_one("c-list-grid-desc")
    # print(c_list)
    # <c-list-grid-desc> 태그 하위에
    # <dt> 태그 요소들 가져오기 (리스트 형태로 가져오기) 
    c_dt = c_list.select("dt")
    # <c-list-grid-desc> 태그 하위에
    # <dd> 태그 요소들 가져오기 (리스트 형태로 가져오기)
    c_dd = c_list.select("dd")
    # <c-list-grid-desc> 태그 하위에
    # <dt>, <dd> 태그 요소 갯수 출력하기 
    print(len(c_dt), len(c_dd))
    c_data = {}
    # 서로 다른 리스트 두개(c_dt, c_dd)를 하나의 요소처럼 쓰기 위해
    # zip() 함수 사용 및 for문 반복하여 서로 다른 리스트 두개에 존재하는 모든 요소들 방문 처리 
    for dt, dd in zip(c_dt, c_dd):
        # print(dt.text)  # dt.text 값이 공백(' ')으로 출력
        # print(dd.text)  # dd.text 값이 공백(' ')으로 출력
        # print(f"s:{dt} t:{type(dt)} v:{dt.text}")
        # dt.text, dd.text 값이 공백(' ')으로 출력 되므로 
        # 아래처럼 dt.contents, dd.contents 사용해서 출력
        # print(f"s:{dt} t:{type(dt)} v:{dt.contents}")
        # print(f"s:{dd} t:{type(dd)} v:{dd.contents}")

        d_text = dt.contents[0]
        d_val = dd.contents[0]
        # dt.contents, dd.contents 값 출력시 리스트 형태로 출력되므로
        # 아래 변수 d_text, d_val 처럼 리스트 객체(dt, dd)의 0번째 인덱스 요소[0]로 가져오기 
        # print(d_text, d_val)

        # c_data[dt] = dd
        # 주의사항 - 아래처럼 코드 작성시 <dt>, <dd> 태그안에 텍스트가 없는 경우 오류 발생해서 프로그램이 강제 종료될 위험한 상황 발생 가능
        # d_text.strip() - <dt> 태그 안에 존재하는 텍스트만 추출(공백 '' 제외) 의미
        # d_val.strip() - <dd> 태그 안에 존재하는 텍스트만 추출(공백 '' 제외) 의미
        c_data[d_text.strip()] = d_val.strip()
    # print(c_data)
    
    return {
        # 영화 제목 가져오기
        "title": c_title.contents[0],
        # <c-thumb> 태그의 속성 "data-original-src"에 할당된 URL 주소 가져오기 
        "thumbnail": c_thumb.get("data-original-src"),
        # 영화 정보 가져오기 
        "info": c_data
    }

if __name__ == "__main__":
    # print(search_movie_daum("매트릭스"))
    print(search_movie_daum("아바타"))
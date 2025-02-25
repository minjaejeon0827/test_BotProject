import requests
import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# 매개변수 data로 전달받은 json 데이터에서
# 매개변수 target_key로 전달받은 특정 키(key)를 찾아주는 함수 
def find_key(data, target_key):
    # 매개변수 data에 저장된 json 데이터가
    # 딕셔너리(dict) 자료형인 경우 
    if isinstance(data, dict):
        # 딕셔너리(dict) 자료형인 
        # 매개변수 data에 저장된 데이터를 추출하려면
        # 아래처럼 data.items() 호출 해서 for 반복문으로 모든 요소 방문
        for key, value in data.items():
            # 매개변수 data에 저장된 키(key)와
            # 매개변수 target_key에 저장된 키(target_key)값이 같은 경우 
            if key == target_key:
                # 파이썬 yield 문법 사용하여 value 반환
                yield value
            # 매개변수 data에 저장된 키(key)와
            # 매개변수 target_key에 저장된 키(target_key)값이 다른 경우 
            else:
                # 파이썬 yield 문법 사용하여 
                # 함수 find_key를 재귀함수 방식으로 호출 
                yield from find_key(value, target_key)
    # 매개변수 data에 저장된 json 데이터가
    # 리스트(list) 자료형인 경우 
    elif isinstance(data, list):
        # 리스트(list) 자료형인 
        # 매개변수 data에 저장된 데이터를 추출하려면
        # 그냥 아래처럼 for 반복문 사용 
        for item in data:
            # 파이썬 yield 문법 사용하여 
            # 함수 find_key를 재귀함수 방식으로 호출 
            # 리스트(list) 자료형인 매개변수 data에
            # 저장된 데이터는 딕셔러니(dict) 형식이기 때문에
            # 아래처럼 재귀함수 방식으로 호출 
            yield from find_key(item, target_key)

def search_youtube(keyword):
    results = []
    url = f"https://www.youtube.com/results?search_query={keyword}"
    # HTTP - GET 통신 
    r = requests.get(url, headers=header)
    # 유튜브 웹에서 찾아올 데이터 시작 부분 
    p_start = "var ytInitialData = "
    # 유튜브 웹에서 찾아올 데이터 끝 부분
    p_end = "};"

    # r.text 변수에 저장된 문자열 전체에서 
    # 변수 p_start에 저장된 문자열을 찾아서 위치(인덱스) 값을 변수 index_start에 저장 
    index_start = r.text.find(p_start)
    # r.text 변수에 저장된 문자열 전체에서 
    # 시작점(index_start) 부터 변수 p_end에 저장된 문자열을 찾아서 위치(인덱스) 값을 변수 끝지점(index_end)에 저장 
    index_end = r.text.find(p_end, index_start)
    # print(index_start, index_end)
    
    # 끝지점(index_end)이 시작점(index_start) 보다 작은 경우
    # 프로그램에 문제가 생긴것으로 판단하여 
    # results = [] 값 그대로 리턴 
    if index_end < index_start:
        return results
    
    # 끝지점(index_end)이 시작점(index_start) 보다 크거나 같은 경우
    # 프로그램에 정상적으로 작동하여 아래코드 실행
    # 변수 "var ytInitialData = { ... };" 중괄호 안에 들어있는 코드 및 데이터 가져와서 터미널창에 출력하기 
    data = r.text[index_start + len(p_start) : index_end + 1]
    # print(data)

    # 파이썬 with문 사용하여  
    # 위에 변수 data에 저장된 변수 "var ytInitialData = { ... };" 
    # 중괄호 안에 들어있는 코드 및 데이터를 
    # 텍스트 파일("test.txt")에 쓰기모드로 작성 및 임시로 저장
    # with open("test.txt", "w", encoding="utf-8") as f: 
    #     f.write(data)

    # 위에 변수 data에 저장된 변수 "var ytInitialData = { ... };" 
    # 중괄호 안에 들어있는 코드 및 데이터를 
    # json 형식의 데이터로 변환 및 변수 _json에 변환된 json 형식 데이터 저장
    _json = json.loads(data)
    # _json 변수에 저장된 json 데이터 항목 "contents" -> 하위 항목 "twoColumnSearchResultsRenderer" 
    # -> 하위 항목 "primaryContents" -> 하위 항목 "sectionListRenderer" 
    # -> 하위 항목 "contents"에 속한 json 데이터 가져와서 변수 contents에 저장  
    # 변수 contents에 저장된 json 데이터는 리스트형식으로 여러가지 데이터가 저장됨.
    contents = _json.get("contents").get("twoColumnSearchResultsRenderer").get("primaryContents").get("sectionListRenderer").get("contents")
    # 재귀함수 find_key 호출하여
    # 변수 contents에 저장된 json 데이터 중 
    # 특정키(target_key) 항목 "videoRenderer"에 속한 json 데이터 찾아서
    # 변수 video_renderer에 json 데이터 저장
    video_renderer = list(find_key(contents, "videoRenderer"))

    # for문 사용하여 변수 video_renderer에 저장된 모든 요소 방문
    for vr in video_renderer:
        # print(vr)
        # 변수 vr에 저장된 json 데이터 중 항목 "videoId"에 속한 
        # json 데이터 가져와서 변수 vid에 저장  
        vid = vr.get("videoId")
        # 변수 vr에 저장된 json 데이터 중 항목 "thumbnail" 
        # -> 항목 "thumbnails"리스트 0번째 인덱스[0]
        # -> 항목 "url"에 속한 
        # json 데이터 가져와서 변수 vthumb에 저장  
        vthumb = vr.get("thumbnail").get("thumbnails")[0].get("url")
        # 변수 vr에 저장된 json 데이터 중 항목 "lengthText"에
        # 속한 json 데이터 가져와서 변수 vlength에 저장  
        vlength = vr.get("lengthText")

        # 변수 vlength에 저장된 json 데이터가 만약 없다면 
        if vlength is None:
            continue  # continue 처리 

        # 변수 vlength에 저장된 json 데이터 항목 "simpleText"에 속한
        # json 데이터 가져와서 변수 vduration에 저장
        vduration = vlength.get("simpleText")
        # 변수 vr에 저장된 json 데이터 중 항목 "viewCountText"
        # -> 항목 "simpleText" 에 속한 
        # json 데이터 가져와서 변수 vcount에 저장  
        vcount = vr.get("viewCountText").get("simpleText")
        # 변수 vr에 저장된 json 데이터 중 항목 "title"
        # -> 항목 "runs" -> 항목 "text" 에 속한 
        # json 데이터 가져와서 변수 vtitle에 저장  
        vtitle = vr.get("title").get("runs")[0].get("text")

        # 함수 append 호출하여 
        # 리스트 객체 results에 아래처럼 딕셔너리(dict) 형태로 데이터 추가
        results.append({
            "vid": vid,
            "vtitle": vtitle,
            "vcount": vcount,
            "vthumb": vthumb,
            "vduration": vduration
        })
    # 위의 for문 실행 끝나고 아래처럼 리스트 객체 results 리턴 
    return results

if __name__ == "__main__":
    results = search_youtube("남박사")
    for r in results:
        print(r)
        print("=====================================")

# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 윈도우 프로그래밍 win32 라이브러리 "pywin32" 설치
# pip install pywin32

import win32con, win32api, win32gui, ctypes, win32clipboard
import time
import re
from modules import weather
from modules import money_exchange_rate
_user32 = ctypes.WinDLL("user32")

CURRENCY_LIST = ["달러", "위안", "엔", "유로", "페소", "루블", "홍콩달러", "호주달러"]


def send_key(hwnd, keycode):
    # 운영체제가 카카오톡 메시지 전송하는 것을 처리하고 결과 기다리지 않고
    # 메시지 전송해 라고 하고 그냥 다음 코드 줄로 넘어간다.
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, keycode, 0)
    time.sleep(0.01)   # 0.01초 대기 

    # 운영체제가 카카오톡 메시지 전송하는 것을 처리하고 결과 기다리지 않고
    # 메시지 전송해 라고 하고 그냥 다음 코드 줄로 넘어간다.
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, keycode, 0)

# 카카오톡 메시지 전송 
def send_message(chatroom_name, text):
    # 해당 chatroom_name 변수에 가진 문자열과 같은 윈도우 핸들 값 가져오기 
    hwndMain = win32gui.FindWindow(None, chatroom_name)
    # 부모 윈도우 핸들 값을 가진 "hwndMain"의 자식 윈도우 "RichEdit50W"의 핸들 값 가져오기 
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RichEdit50W", None)
    # 운영체제가 카카오톡 메시지 전송하는 것을 처리하고 결과를 기다림
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    # 엔터키(win32con.VK_RETURN) 입력(처리)
    send_key(hwndEdit, win32con.VK_RETURN)

def open_chat(chat_name):
    # 윈도우 제목(title - "카카오톡")으로 주면 
    # 해당 제목(title - "카카오톡")을 갖는 윈도우를 찾아서 그 윈도우의 핸들(Handle) 값 반환
    # 윈도우의 핸들(Handle)이라는 것은 윈도우 상의 모든 프로그램 혹은 자원을 관리하기 위한 어떤 하나의 아이디 같은 개념이다.
    hwndKakao = win32gui.FindWindow(None, "카카오톡")
    # 해당 제목(title - "카카오톡")을 갖는 
    # 윈도우의 핸들 값 10진수 "4262348" 출력 
    print(hwndKakao)   

    # 해당 제목(title - "카카오톡")을 갖는 
    # 윈도우의 핸들 값 16진수 "0x4109cc" 출력 
    print(hex(hwndKakao))

    if hwndKakao:
        # 부모 윈도우 핸들 값을 가진 "hwndKakao"의 자식 윈도우 "EVA_ChildWindow"의 핸들 값 가져오기 
        hwnd1 = win32gui.FindWindowEx(hwndKakao, None, "EVA_ChildWindow", None)
        # 자식 윈도우 "EVA_ChildWindow"의 핸들 값을 가진 "hwnd1"의 첫 번째 자식 윈도우 "EVA_Window"의 핸들 값 가져오기 
        hwnd2 = win32gui.FindWindowEx(hwnd1, None, "EVA_Window", None)
        # 자식 윈도우 "EVA_ChildWindow"의 핸들 값을 가진 "hwnd1"의 두 번째 자식 윈도우 "EVA_Window"의 핸들 값 가져오기 
        hwndChatList = win32gui.FindWindowEx(hwnd1, hwnd2, "EVA_Window", None)
        print(f"{hex(hwndChatList)}")
        # 자식 윈도우 "EVA_ChildWindow"의 핸들 값을 가진 "hwnd1"의 
        # 두 번째 자식 윈도우 "EVA_Window"의 핸들 값을 가진 "hwndChatList"의 자식 윈도우 "Edit" 핸들 값 가져오기 
        hwndEdit = win32gui.FindWindowEx(hwndChatList, None, "Edit", None)
        win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, chat_name)
        time.sleep(0.5) # 시간 0.5초 대기 
        # 엔터키(win32con.VK_RETURN) 입력(처리)
        send_key(hwndEdit, win32con.VK_RETURN)
        return True
    return False

def kakao_get_message(chatname):
    hwndMain = win32gui.FindWindow(None, chatname)
    if hwndMain:
        hwnd = win32gui.FindWindowEx(hwndMain, None, "EVA_VH_ListControl_Dblclk", None) 
        thread_id = _user32.GetWindowThreadProcessId(hwnd, None)
        lparam = win32api.MAKELONG(0, _user32.MapVirtualKeyA(ord('A'), 0))
        PBYTE = ctypes.c_ubyte * 256
        pKeyBuffers = PBYTE()
        pKeyBuffers_old = PBYTE()
        pKeyBuffers[win32con.VK_CONTROL] |= 128 #10000000

        _user32.AttachThreadInput(win32api.GetCurrentThreadId(), thread_id, True)
        _user32.GetKeyboardState(ctypes.byref(pKeyBuffers_old))
        _user32.SetKeyboardState(ctypes.byref(pKeyBuffers))

        time.sleep(0.01)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, ord('A'), lparam)
        time.sleep(0.01)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, ord('A'), lparam | 0xC0000000)
        time.sleep(0.01)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, ord('C'), lparam)
        time.sleep(0.01)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, ord('C'), lparam | 0xC0000000)
        time.sleep(0.01)
        _user32.SetKeyboardState(ctypes.byref(pKeyBuffers_old))
        time.sleep(0.01)
        _user32.AttachThreadInput(win32api.GetCurrentThreadId(), thread_id, False)

        lparam = win32api.MAKELONG(10, 130)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lparam)
        time.sleep(0.5)
        data = copy_clipboard().split("\r\n")
        print(data)
        messages = []
        date = ""
        for d in data:
            if d.find("]") >= 0:
                _name = d[1:d.find("]")]
                d = d[d.find("]") + 1:].strip()
                _datetime = date + " " + d[1:d.find("]")]
                _msg = d[d.find("]") + 1:].strip()
                messages.append({
                    "name": _name,
                    "datetime": _datetime,
                    "msg": _msg
                })
            else:
                date = d
        return messages
    return []

def copy_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def main(chatname):
    last_message = ""
    my_message = ""
    while True:
        if open_chat(chatname):
            messages = kakao_get_message(chatname)
            if len(messages) > 0:
                message = messages[-1]
                msg = message.get("msg")
                if last_message == "":
                    last_message = msg
                if msg != last_message and msg != my_message:
                    match_money = re.search(f"^([0-9]+\s?)({"|".join(CURRENCY_LIST)})+$", msg)
                    match_weather = re.search("^([가-힣]{2})\s?날씨$", msg)
                    if match_money:
                        src = match_money.group()
                        result = money_exchange_rate.google_money_exchange_rate(src)
                        output = f"{result[1]} {result[0]} 원"
                    else:
                        output = f"{msg}에 대한 환율 정보 구하기 실패"
                    
                    if match_weather:
                        src = match_weather.group().replace("날씨", "")
                        w = weather.get_weather(src)
                        if w:
                            output = ""
                            for k, v in w.items():
                                output += f"{k}: {v}\r\n"
                        else:
                            output = f"{msg}에 대한 날씨 정보 구하기 실패"
                    
                    send_message(chatname, output)
                    my_message = output
                    last_message = msg
                time.sleep(1)
            else:
                print("메세지가 없습니다.")
        else:
            print("카카오톡이 실행중이 아닙니다.")

if __name__ == "__main__":
    # hwndKakao = win32gui.FindWindow(None, "카카오톡")
    # # 부모 윈도우 핸들 값을 가진 "hwndKakao"의 자식 윈도우 "EVA_ChildWindow"의 핸들 값 가져오기 
    # hwnd1 = win32gui.FindWindowEx(hwndKakao, None, "EVA_ChildWindow", None)
    # # 자식 윈도우 "EVA_ChildWindow"의 핸들 값을 가진 "hwnd1"의 첫 번째 자식 윈도우 "EVA_Window"의 핸들 값 가져오기 
    # hwnd2 = win32gui.FindWindowEx(hwnd1, None, "EVA_Window", None)
    # # 자식 윈도우 "EVA_ChildWindow"의 핸들 값을 가진 "hwnd1"의 두 번째 자식 윈도우 "EVA_Window"의 핸들 값 가져오기 
    # hwndChatList = win32gui.FindWindowEx(hwnd1, hwnd2, "EVA_Window", None)
    # print(f"{hex(hwndChatList)}")
    # hwndKakao = win32gui.FindWindow(None, "카카오톡")
    # print(hwndKakao)
    # print(hex(hwndKakao))
    # chatname = "남박사"
    # main(chatname)
    chat_name = "전민재"
    open_chat(chat_name)
    time.sleep(0.5)
    send_message("전민재", "안녕하세요 봇입니다.")

    
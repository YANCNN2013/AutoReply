import os
import time
import pyautogui
import up
import message

call_count = 0
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True


def click_button() -> None:
    while True:
        try:
            button_pos = pyautogui.locateCenterOnScreen('button.png', confidence=0.9)
            if button_pos:
                for i in range(3):    # 防止点击失效
                    pyautogui.click(button_pos)
                time.sleep(1)
                break 
        except pyautogui.ImageNotFoundException:
            break


def main() -> None:
    global call_count
    call_count += 1
    up.up_window("微信")
    time.sleep(0.5)
    pyautogui.hotkey('alt','printscreen')
    if call_count == 1:
        os.system("start https://chat.baidu.com")
        time.sleep(10)
    else:
        pyautogui.hotkey('alt', 'tab')   
        pyautogui.click(520, 911)
    
    try:
        button_pos = pyautogui.locateCenterOnScreen('chinese.png', confidence=0.9)
        if button_pos:
            time.sleep(1)
    except pyautogui.ImageNotFoundException:
        pyautogui.press("shift")
    pyautogui.write("bang'wo'hui'fu'zhe'tiao'xiao'xi")
    pyautogui.press("space")
    pyautogui.write("zhi'yao'hui'fu")
    pyautogui.press("space")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    pyautogui.press("enter")
    while True:
        try:
            button_pos = pyautogui.locateCenterOnScreen('copy_icon.png', confidence=0.99)
            if button_pos:
                for i in range(2):    # 防止点击失效
                    pyautogui.click(button_pos)
                time.sleep(1)
                break 
        except pyautogui.ImageNotFoundException:
            click_button()
            time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")


if __name__ == "__main__":
    if os.name != "nt":   
        print("支持linux")   
        exit(1)    

    print("开始自动回复,按Ctrl+C结束")
    time.sleep(5)
    try:
        main()
        time.sleep(0.5)   
        initial = message.get_screen_roi()
        print("开始监控界面变化...")
        while True:
            is_changed, diff_img = message.detect_screen_change(initial)
            if is_changed:
                main()    
                initial = message.get_screen_roi()  # 更新快照
            time.sleep(1)
    except KeyboardInterrupt, pyautogui.FailSafeException:
        print("\n自动回复已结束")

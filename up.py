import win32gui  # type: ignore
import win32con  # type: ignore

def up_window(name: str) -> None:
    if not isinstance(name, str):
        raise TypeError("name must is string")
    hwnd = win32gui.FindWindow(None, name)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        print("窗口已调到最上层")
    else:
        raise ValueError("未找到窗口，请确认窗口已打开")
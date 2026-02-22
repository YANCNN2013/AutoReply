import win32clipboard
import win32con

def is_clipboard_image() -> bool:
    """
    检测剪贴板内容是否为图片类型
    返回值：True（是图片）/ False（不是图片）
    """
    # 标记是否成功打开剪贴板
    clipboard_opened = False
    try:
        # 打开剪贴板，并标记状态
        win32clipboard.OpenClipboard()
        clipboard_opened = True
        
        # 检测核心图片格式：CF_DIB（设备无关位图）、CF_BITMAP（位图）
        has_dib = win32clipboard.IsClipboardFormatAvailable(win32con.CF_DIB)
        has_bitmap = win32clipboard.IsClipboardFormatAvailable(win32con.CF_BITMAP)
        
        return has_dib or has_bitmap  # type: ignore
        
    except Exception as e:
        print(f"检测出错：{str(e)}")
        return False
    finally:
        # 只有确实打开了剪贴板，才执行关闭操作
        if clipboard_opened:
            win32clipboard.CloseClipboard()


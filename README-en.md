# WeChat Auto-Reply Script
An automated WeChat message response tool implemented with Python + PyAutoGUI, which completes the full automated process of message monitoring and replying through screen recognition and keyboard/mouse simulation.

## I. Feature Introduction
- Automatically locate and activate the WeChat window
- Monitor changes in the WeChat chat interface and trigger automatic replies when new messages are detected
- Automatically call Baidu ERNIE Bot (chat.baidu.com) to generate reply content
- Complete button clicks, content copy/paste, and other operations through screen image recognition
- Support keyboard and mouse simulation on Windows systems with a retry mechanism to prevent click failures

## II. Environment Requirements
### (1) System Requirements
Only supports **Windows systems** (restricted by `os.name == "nt"` in the script; MacOS and Linux systems will exit directly)

### (2) Dependency Installation
1. Ensure Python 3.7+ is installed
2. Install core dependency packages:
```bash
pip install pyautogui opencv-python pillow pywin32
```
3. Note: `pyautogui` depends on OpenCV. If installation fails, try:
```bash
pip install opencv-python==4.8.0.74
```

### (3) Custom Module Description
The script depends on the following two custom modules (ensure they are in the same directory as the script):
- `up.py`: Contains the `up_window()` function for activating/keeping specified windows (e.g., WeChat) on top
- `message.py`: Contains `get_screen_roi()` and `detect_screen_change()` functions for monitoring screen area changes
- `check.py`: Contains `is_clipboard_image()` for detecting successful copying

## III. Preparations
1. **Prepare image files for recognition** (must be in the same directory as the script; pre-prepared):
   - `button.png`: Screenshot of the button to be clicked
   - `chinese.png`: Screenshot of the Chinese input method status indicator (used to determine input method status)
   - `copy_icon.png`: Screenshot of the copy button (used to copy generated reply content)
   - `copy.png`: Alternate version of copy_icon.png

2. **WeChat Settings**:
   - Ensure WeChat is open and its icon is visible in the taskbar

## IV. Usage Instructions
1. Place the script file (`auto_reply.py`), custom modules, and recognition images in the same directory
2. Open WeChat
3. Run the script:
```bash
python auto_reply.py
```
4. After startup, the script will start a 5-second countdown before automatically beginning monitoring
5. Terminate the script: Press `Ctrl + C` or move the mouse to the top-left corner (0,0) to stop running

## V. Core Process Description
1. Open the Baidu ERNIE Bot webpage on first run; switch windows via `Alt + Tab` on subsequent runs
2. Detect input method status; automatically press `Shift` to switch to Chinese if not already active
3. Input preset text, paste clipboard content, and send the generated reply
4. Identify and click the copy button to copy the reply content to the clipboard
5. Switch back to the WeChat window, paste and send the reply content
6. Continuously monitor screen changes and repeat the above process when new messages are detected

## VI. Notes
- **Screen Resolution**: Coordinates in the script (e.g., `520, 911`) are based on a specific resolution; re-adjust coordinate values after changing devices/resolutions
- **Image Recognition Accuracy**: `confidence=0.9` means 90% image matching accuracy; lower the value (e.g., 0.8) if recognition fails, but excessively low values may cause misrecognition
- **Permission Issues**: Run as a regular user on Windows; administrator privileges may cause window activation failures
- **Anti-Failure Mechanism**: The script checks for successful button clicks and triggers alternate click logic if failed
- **Safety Note**: PyAutoGUI's `FAILSAFE = True` means moving the mouse to the top-left corner of the screen triggers an emergency stop to prevent script out-of-control

## VII. Common Issues
### Q1: FileNotFoundError Prompt
- Check if image files exist and are named correctly

### Q2: Failed to Activate WeChat Window
- Confirm the `up_window("WeChat")` function in `up.py` can correctly identify the WeChat window name
- Close multiple WeChat instances and keep only one WeChat window running

### Q3: Garbled Input from Input Method
- Ensure the system default input method is Chinese and `chinese.png` can correctly identify Chinese status
- The script includes `pyautogui.press("shift")` to switch input methods; manually switch if this fails, then re-run the script

## VIII. Disclaimer
This script is for learning and personal use only. Do not use it for commercial purposes or in scenarios that violate WeChat's User Agreement. The user assumes all risks arising from its use.

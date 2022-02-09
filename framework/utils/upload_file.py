import time
import pyautogui


class UploadFile:

    @staticmethod
    def upload_file(path):
        time.sleep(4)
        pyautogui.write(f"{path}")
        pyautogui.press('enter')

import sys

sys.path.append('/Users/yaroslav/Desktop/Development/Pets/Jarvis')

import time
import pyautogui
import webbrowser
import pytesseract
import os
import keyboard
import playsound
from pytesseract import Output
from datetime import datetime
from Body.Config.CONFIG import *
from PIL import Image, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
safari_is_open = False


def get_time():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


def update_safari_state():
    global safari_is_open

    cmd = """osascript -e 'tell application "System Events" to get name of (processes where background only is false)'"""
    opened_apps = os.popen(cmd).read()
    safari_is_open = 'Safari' in opened_apps


def close_browser():
    tap = 'cmd+w' if safari_is_open else 'cmd+w, cmd+q'
    keyboard.press_and_release(tap)


def increase_conversion():
    image = Image.open(ORIGINAL)
    image = image.convert('L')
    factor = 4
    enchancer = ImageEnhance.Contrast(image)
    result = enchancer.enhance(factor)
    result.save(CHANGED)


def clear_temp_files():
    [os.remove(i) for i in {ORIGINAL, CHANGED}]


def get_text_location():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(ORIGINAL)
        increase_conversion()

        data = pytesseract.image_to_data(CHANGED, lang='rus', output_type=Output.DICT)
        clear_temp_files()
        boxes = len(data['text'])

        for i in range(boxes):
            accuracy = int(data['conf'][i])
            recognized_word = data['text'][i]

            if accuracy > MIN_ACCURACY and recognized_word == RAISE_WORD:
                return [data['left'][i], data['top'][i]]
    except:
        print(
            f'{RED}Error at: {get_time()}\n"{RAISE_WORD}" not found: screen seems to be inactive, or check connection and site contents. Waiting for next attempt now...\n')


def proceed():
    playsound.playsound(f'{SOUNDS_PATH}/cv_raiser/start.mp3')
    update_safari_state()
    webbrowser.open_new(CV_LINK)
    time.sleep(LOADING_DURATION)

    raise_text_location = get_text_location()

    if raise_text_location:
        x_spacing = 20
        y_spacing = 5
        x = raise_text_location[0] + x_spacing
        y = raise_text_location[1] + y_spacing
        print(f'{BLUE}"{RAISE_WORD}" detected! Coordinates: {x, y}')
        pyautogui.moveTo(x, y, duration=MOUSE_MOVEMENT_DURATION, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(LOADING_DURATION)
        close_browser()
        print(f'{MAGENTA}CV raised at: {get_time()}\n')


def run_loop():
    sec = 0

    while True:
        if sec % MSG_DELAY == 0:
            proceed()

        time.sleep(1)
        sec += 1


if __name__ == "__main__":
    print(f'{CYAN}\nCV page: {CV_LINK}\nAttempt: every {INTERVAL} hour(s)\n')
    run_loop()

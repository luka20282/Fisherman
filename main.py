import time
import pyautogui
from pynput.keyboard import Controller
import cv2
import numpy as np

keyboard = Controller()

time.sleep(5)

while True:
    pyautogui.hotkey("e")

    while True:
        start_biting = pyautogui.locateOnScreen("ad_key1.png", confidence=0.8)
        if start_biting is not None:
            break
        else:
            print('searching')

    img1 = pyautogui.screenshot('scr1.png')
    time.sleep(1)
    img2 = pyautogui.screenshot('scr2.png')

    template = cv2.imread('fish1.png', 0)
    methods = [cv2.TM_CCOEFF]
    h, w = template.shape

    imgB = cv2.imread('scr1.png', 0)
    imgA = cv2.imread('scr2.png', 0)

    for method in methods:
        imgCB = imgB.copy()

        result1 = cv2.matchTemplate(imgCB, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result1)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location1 = min_loc
        else:
            location1 = max_loc
        bottom_right1 = (location1[0] + w, location1[1] + h)
        print(bottom_right1)
        x_axys1 = location1[0] + w
        # cv2.rectangle(imgCB, location1, bottom_right1, 255, 5)
        # cv2.imshow('Match', imgCB)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    for method in methods:
        imgCA = imgA.copy()

        result2 = cv2.matchTemplate(imgCA, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result2)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc
        bottom_right2 = (location[0] + w, location[1] + h)
        print(bottom_right2)
        x_axys2 = location[0] + w
        # cv2.rectangle(imgCA, location, bottom_right2, 255, 5)
        # cv2.imshow('Match', imgCA)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    print(x_axys1 - x_axys2)

    if (x_axys1 - x_axys2) < 0:
        keyboard.press('a')
        t_end = time.time() + 7
        while time.time() < t_end:
            print('a')
        keyboard.release('a')
    else:
        keyboard.press('d')
        t_end = time.time() + 7
        while time.time() < t_end:
            print('d')
        keyboard.release('d')

    click = pyautogui.locateOnScreen("mou1.png", confidence=0.8)

    print(click)

    if click:
        t_end = time.time() + 18
        while time.time() < t_end:
            pyautogui.mouseDown()

    pyautogui.mouseUp()

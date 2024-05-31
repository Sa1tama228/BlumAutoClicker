import cv2
import numpy as np
import pyautogui
import mss
import time


def click_on_yellow():
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    with mss.mss() as sct:
        monitor = sct.monitors[1]

        while True:
            screenshot = np.array(sct.grab(monitor))
            hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    pyautogui.click(cx, cy)

            time.sleep(0.01) # fps


if __name__ == "__main__":
    click_on_yellow()

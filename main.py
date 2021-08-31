import pydirectinput as pd
import pyautogui
import time
import cv2
import keyboard
from collections import defaultdict
import numpy as np



def setupCamera():
    # Adjusting Zoom 6o
    for i in range(5):
        pd.press('o')
    pd.mouseDown(button="right")
    pd.move(0, 250, relative=True)
    pd.mouseUp(button="right")

def detectEdge(img):
    image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    edges = cv2.Canny(image=img_blur, threshold1=50, threshold2=175)
    return edges

def pause():
    print("paused")
    time.sleep(10)
    print("resume")
    return 'none'



imgNum = 0
keymap = defaultdict(lambda: 'none', {'a':'a', 's':'s', 'd':'d', 'space':'space', 'q':pause()})
images = np.zeros(10000, dtype=object)
keys = np.zeros(10000, dtype=object)

time.sleep(2)
setupCamera()
time.sleep(2)
print("GO")

while imgNum <= 50:
    img = pyautogui.screenshot()
    key = keymap[keyboard.read_key()]
    images[imgNum] = np.array(img)
    keys[imgNum] = key
    imgNum+=1

imgNum = 0
while imgNum <= 50:
    cv2.imwrite('C:\\Users\\gosee\\PycharmProjects\\CreateTrainingExamples\\trainingExamples\\' + keys[imgNum] + r'\img' + str(imgNum) + '.jpg', detectEdge(images[imgNum]))
    imgNum+=1

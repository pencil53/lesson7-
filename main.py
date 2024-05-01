import cv2
import numpy as np
import time as t

video = cv2.VideoCapture("download.mp4")
t.sleep(1)
bg = 0
count = 0
for i in range(60):
    #video.read() returns two information, first imformation is the return status which could be true or false depending upon whether python was able to read every indidivual frame
    #second information is the frame of the video itself
    return_val,bg = video.read()
    if return_val == False:
        continue

bg = np.flip(bg,axis=1)

while video.isOpened():
    status,frame = video.read()
    if not status:
        break
    count += 1 
    img = np.flip(frame,axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
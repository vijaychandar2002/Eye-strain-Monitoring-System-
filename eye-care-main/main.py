import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import pyautogui as pag
import screen_brightness_control as sbc
from window_resize import *
import time

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector()
alert = 0
close = 0

obj = changes()
start_time = time.time()*1000.0
curr_time = start_time


start_time_blink = time.time()*1000.0
curr_time_blink = start_time_blink


while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    curr_time = time.time()*1000.0

    if int(curr_time - start_time) >= 11200000:
        pag.alert(text="You have been staring at monitor for very long time. Please look at objects 20m far away to refocus", title="Time Alert")
        start_time = curr_time

    if faces:
        face = faces[0]

        left_pupil = face[145]
        right_pupil = face[374]

        w, _info, _image = detector.findDistance(left_pupil, right_pupil, img)
        W = 6.3
        f = 600
        D = W*f/w

        leftUp = face[159]
        leftDown = face[23]

        lengthVer, _ = detector.findDistance(leftUp, leftDown)
        blink = int((lengthVer*100))
        curr_time_blink = time.time()*1000.0

        if blink <= 1200:
            start_time_blink = curr_time_blink

        if int(curr_time_blink - start_time_blink) >= 20000:
            pag.alert(
                text="You have'nt blinked from past 20 seconds\nTo maintain eye health don't continuously stare the screen ", title="Blink Alert")
            start_time_blink = curr_time_blink

        # cvzone.putTextRect(
        #     img, f'Distance {int(D)} cm', (face[10][0]-100, face[10][1]-20), 2, 3)

        if D < 30:
            if(alert >= 5):
                pag.alert(text="You are very close to your Display, Doctors recommend to stay atleast 50 cms away from your monitor to avoid eye-strain, We are dimming your monitor's brightness If you are still to close to your monitor", title="Distance Alert")
                alert = 3
                sbc.set_brightness(0)
            else:
                pag.alert(text="You are very close to your Display, Doctors recommend to stay atleast 50 cms away from your monitor to avoid eye-strain", title="Distance Alert")
                alert += 1
        else:
            change(i=int(D), obj=obj)

    if not faces:
        close += 1
        if close >= 500:
            cap.release()
            cv2.destroyAllWindows()
            break

    '''
    If you want to see Distance of your face from your PC realtime, un-comment the line below
    '''
    # cv2.imshow("Image", img)
    cv2.waitKey(1)

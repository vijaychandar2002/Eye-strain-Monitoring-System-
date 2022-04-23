
import pyautogui as pag

alert = 0


class changes():

    def __init__(self):
        self.last = 35


def change(i, obj):
    last = obj.last
    if i > 0 and i < 40:
        if last > 0 and last < 40:
            pass
        else:
            pag.hotkey('ctrl', '-')

    elif i > 40 and i < 61:
        if last > 40 and last < 61:
            pass
        else:
            if last > 0 and last < 61:
                pag.hotkey('ctrl', '+')
            else:
                pag.hotkey('ctrl', '-')

    elif i > 60:
        if last > 60:
            pass
        else:
            pag.hotkey('ctrl', '+')

    obj.last = int(i)
    return


# def main():
#     obj = changes()
#     while True:
#         success, img = cap.read()
#         img, faces = detector.findFaceMesh(img, draw=False)

#         if faces:
#             face = faces[0]

#             left_pupil = face[145]
#             right_pupil = face[374]

#             w, _info, _image = detector.findDistance(
#                 left_pupil, right_pupil, img)

#             W = 6.3

#             f = 600
#             D = W*f/w

#             cvzone.putTextRect(
#                 img, f'Distance {int(D)} cm', (face[10][0]-100, face[10][1]-20), 2, 3)

#             change(i=int(D), obj=obj)

#         cv2.imshow("Image", img)
#         cv2.waitKey(1)


# main()

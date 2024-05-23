import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)  # -- modify the camera entry point here

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        print(fingerUp)
        cnt.led(fingerUp)
        if fingerUp == [0, 0, 0, 0, 0]:  # -- no finger up
            cv2.putText(frame,
                        'Nenhum dedo!',
                        (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)
        elif fingerUp == [0, 1, 0, 0, 0]:  # -- index finger up
            cv2.putText(frame,
                        'Um dedo!',
                        (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 0, 0]:  # -- middle finger up
            cv2.putText(frame,
                        'Dois dedos!',
                        (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 0]:  # -- ring finger up
            cv2.putText(frame,
                        'Três dedos!',
                        (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 1]:  # -- little finger up
            cv2.putText(frame,
                        'Quatro dedos!',
                        (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)
        elif fingerUp == [1, 1, 1, 1, 1]:  # -- thumb up
            cv2.putText(frame,
                        'Cinco dedos!',
                        (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)

    cv2.imshow("Retorno", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()

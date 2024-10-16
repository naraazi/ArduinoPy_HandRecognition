import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
from time import sleep

ser = serial.Serial("/dev/ttyACM0", 9600)  # -- modify the serial port here
sleep(2)

detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)  # -- modify the camera entry point here

previous_fingerUp = None  # -- variable to store the previous gesture

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)

    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        if fingerUp != previous_fingerUp:  # -- check if the gesture has changed
            previous_fingerUp = fingerUp  # -- update the previous gesture

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
                ser.write('a'.encode('utf-8'))
            elif fingerUp == [0, 1, 1, 0, 0]:  # -- middle finger up
                cv2.putText(frame,
                            'Dois dedos!',
                            (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (255, 255, 255),
                            1,
                            cv2.LINE_AA)
                ser.write('b'.encode('utf-8'))
            elif fingerUp == [0, 1, 1, 1, 0]:  # -- ring finger up
                cv2.putText(frame,
                            'Três dedos!',
                            (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (255, 255, 255),
                            1,
                            cv2.LINE_AA)
                ser.write('c'.encode('utf-8'))
            elif fingerUp == [0, 1, 1, 1, 1]:  # -- little finger up
                cv2.putText(frame,
                            'Quatro dedos!',
                            (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (255, 255, 255),
                            1,
                            cv2.LINE_AA)
                ser.write('d'.encode('utf-8'))
            elif fingerUp == [1, 1, 1, 1, 1]:  # -- thumb up
                cv2.putText(frame,
                            'Cinco dedos!',
                            (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (255, 255, 255),
                            1,
                            cv2.LINE_AA)
                ser.write('e'.encode('utf-8'))
    else:
        previous_fingerUp = None  # -- reset previous gesture when no hands are detected

    cv2.imshow("Retorno", frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
ser.close()

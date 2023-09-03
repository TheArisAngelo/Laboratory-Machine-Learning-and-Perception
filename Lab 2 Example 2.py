import numpy as np
import cv2 as cv
cap = cv.VideoCapture('In 30 sec, These Hilarious Slow-Mo Corgi Puppies Will Make You Laugh & Smile!.mp4')
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

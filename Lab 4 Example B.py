import numpy as np
import cv2 as cv
cap = cv.VideoCapture(1)
while True:

    ret, frame = cap.read()
    cv.imshow('Original', frame)
    edges = cv.Canny(frame, 200, 600)
    cv.imshow('Canny Edges', edges)


    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
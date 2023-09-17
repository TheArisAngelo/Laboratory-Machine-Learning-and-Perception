import cv2 as cv

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    edge = cv.Laplacian(frame, cv.CV_64F)

    cv.imshow('Original', frame)
    cv.imshow('Laplacian', edge)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


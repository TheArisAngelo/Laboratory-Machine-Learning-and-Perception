import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('tokyo manji gang.png')

blur = cv.blur(img, (10, 10))
blur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
blur = cv.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


plt.subplot(121), plt.imshow(img), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


plt.subplot(121), plt.imshow(img), plt.title('Median')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(median), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


plt.subplot(121), plt.imshow(img), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])


plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

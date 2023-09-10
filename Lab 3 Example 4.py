import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('mangekyou sharingan.jpg')
blur = cv.bilateralFilter(img,50,500,500)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

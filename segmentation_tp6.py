import cv2 as cv
import numpy as np

img = cv.imread('E:\\lmgrj\\masterwisd\\s2\\autumn.png') #change path

red_min = 190
red_max = 255
green_min = 180
green_max = 255
blue_min = 160
blue_max = 255

gray_low = np.array([blue_min,green_min,red_min])
gray_hi = np.array([blue_max,green_max,red_max])

mask = cv.inRange(img,gray_low,gray_hi)

img[mask>0] = (212, 167, 140)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

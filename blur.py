from statistics import median
import cv2 as cv
from numpy import average

img = cv.imread('photos/spider.jpg')

cv.imshow('spider',img) 

#gauss
gauss =cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('gauss', gauss)

#median
median =cv.medianBlur(img,7)
cv.imshow('median', median)

#average
aver=cv.blur(img,(10,10))
cv.imshow('average',aver)


cv.waitKey(0)
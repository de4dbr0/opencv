import cv2 as cv
from cv2 import resize

img = cv.imread('photos/spider.jpg')

cv.imshow('spider',img) 

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur =cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

#dilating
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

#eroded
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (300,300))
cv.imshow('resize',resized)

#crop
crop = img[50:700, 200:700]
cv.imshow('crop',crop)

cv.waitKey(0)
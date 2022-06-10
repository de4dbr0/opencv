import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)
img = cv.imread('photos/spider.jpg')
cv.imshow('spider', img)

# #paint
# blank [200:300, 200:400] = 0,255,255
# cv.imshow('green', blank)

#rectangle
cv.rectangle(blank, (0,0), (400,250), (255,255,0), thickness=cv.FILLED)
cv.imshow('rectangle',blank)

#circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=5)
cv.imshow('circle',blank)
#center
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 80, (0,255,255), thickness=10)
cv.imshow('circle',blank)
#line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=5)
cv.imshow('line',blank)
#text
cv.putText(blank,'this working?', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0.255,200), 2)
cv.imshow('text',blank)

cv.waitKey(0)
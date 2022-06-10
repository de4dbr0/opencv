import cv2 as cv

img = cv.imread('photos/cars.jpg')

cv.imshow('spider',img) 

capture = cv.VideoCapture('video/blue.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
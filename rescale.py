import cv2 as cv
img = cv.imread('photos/spider.jpg')
cv.imshow('spider',img) 

def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('video/blue.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized=rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
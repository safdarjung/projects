<<<<<<< HEAD
import cv2
import time
import imutils



# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture(0)
time.sleep(1)

firstFrame = None
area = 500

while True:
    _, img = cam.read()
    text = 'Normal'
    img = imutils.resize(img, width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    # first frame will be None only in the first iteration, so that if no frame is captured, the loop will continue
    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    
    # calculating difference between the first frame and all other frames
    img_diff = cv2.absdiff(firstFrame, gaussianImg)
    # converting img pixels to binary form
    threshImg = cv2.threshold(img_diff, 25,225, cv2.THRESH_BINARY)[1]
    # dilating the image to fill in the holes
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    # finding contours of the moving object
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        text = 'Moving Object Detected'
    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)




    cv2.imshow('video_cam1.jpg',img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()

=======
import cv2
import time
import imutils



# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture(0)
time.sleep(1)

firstFrame = None
min_area = 8
max_area = 8000
count = 0
while True:
    _, img = cam.read()
    # the text will show normal when nothing moving is detected
    text = 'Normal'   
    img = imutils.resize(img, width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)
    
    # first frame will be None only in the first iteration, so that if no frame is captured, the loop will continue
    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    
    # calculating difference between the first frame and all other frames
    img_diff = cv2.absdiff(firstFrame, gaussianImg)
    # converting img pixels to binary form
    threshImg = cv2.threshold(img_diff, 25,225, cv2.THRESH_BINARY)[1]
    # dilating the image to fill in the holes
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    # finding contours of the moving object
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # c is the moving object in the contours
    for c in cnts:
        # if cv2.contourArea(c) < area:
        if cv2.contourArea(c) < min_area or cv2.contourArea(c) > max_area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count+=1
        text = 'Moving Object Detected'
    print(text)
    print(count)
    # cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(img, f'Frame: {count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('video_cam1.jpg',img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()
>>>>>>> 6d1b335 (Initial commit)

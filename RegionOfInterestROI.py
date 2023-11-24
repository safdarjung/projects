import cv2

width=640
height=360

cam=cv2.VideoCapture('http://192.168.1.13:6767/video')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frameROI = frame[150:210,250:390]
    grayframeROI = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    
    #if we convert BGR img to gray the color info is lost so it cannot be converted back to BGR
    #So the command below will not convert the gray img to BGR
    #only color is lost but if we convert the gray img back to bgr the img array will contain 3 args with all the values same as 125
    frameROIBGR = cv2.cvtColor(grayframeROI,cv2.COLOR_GRAY2BGR)

    #this line places frameROBGR on the desired position on the starting working frame
    frame[150:210,250:390] = frameROIBGR

    cv2.imshow('BGR ROI',frameROIBGR)
    cv2.moveWindow('BGR ROI',650,180)

    cv2.imshow('gray ROI',grayframeROI)
    cv2.moveWindow('gray ROI',650,90)

    cv2.imshow('ROI',frameROI)
    cv2.moveWindow('ROI',650,0)

    cv2.imshow('winName',frame)
    cv2.moveWindow('winName',0,0)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
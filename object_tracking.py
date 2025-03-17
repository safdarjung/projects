<<<<<<< HEAD
'''
Object tracking based on color:
- convert RGB to HSV(hue saturation value)
- return coordinates of a minimum enclosing circle at the center of the object
- find the center of the object using Moments
- draw the minimum enclosing circle
- minimum enclosing circle tracks left, right, near, far
'''
import numpy as np
import imutils
import cv2


h_lo = 11
h_hi = 179
s_lo = 149
s_hi = 245
v_lo = 100
v_hi = 216

white_hsv_lo = np.array([h_lo, s_lo, v_lo])
white_hsv_hi = np.array([h_hi, s_hi, v_hi])

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    frame = imutils.resize(frame,width=600)
    blurred = cv2.GaussianBlur(frame,(11,11),0)
    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,white_hsv_lo,white_hsv_hi)    # differentiate only the required color
    mask = cv2.erode(mask,None,iterations=2)    # remove the noise
    mask = cv2.dilate(mask,None,iterations=2)    # increase the size of the object
    # if found some points on the object, contous connects all the points and gives a kind of outline for the object
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]  
    center = None
    if len(cnts) > 0:     # if there is a change in the contours{movement in any direction}
        c = max(cnts,key=cv2.contourArea)      # largest contour in the mask
        (x,y),radius = cv2.minEnclosingCircle(c)    # draw the minimum enclosing circle
        M = cv2.moments(c)    # helps to find the center of the object
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))     #coordinates of the center
        if radius>10:    # if the radius is greater than 10, then only draw the circle
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)    # draw the minimum enclosing circle
            cv2.circle(frame,center,5,(0,0,255),-1)    # draw the center point of the object
            print(center)
            if radius>250:
                print("stop")
            else:
                if center[0]<150:
                    print("left")
                elif center[0]>450:
                    print("right")
                elif center[1]<150:
                    print("up")
                elif center[1]>450:
                    print("down")
                elif radius<250:
                    print('front')
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

           


=======
'''
Object tracking based on color:
- convert RGB to HSV(hue saturation value)
- return coordinates of a minimum enclosing circle at the center of the object
- find the center of the object using Moments
- draw the minimum enclosing circle
- minimum enclosing circle tracks left, right, near, far
'''
import numpy as np
import imutils
import cv2


h_lo = 11
h_hi = 179
s_lo = 149
s_hi = 245
v_lo = 100
v_hi = 216

white_hsv_lo = np.array([h_lo, s_lo, v_lo])
white_hsv_hi = np.array([h_hi, s_hi, v_hi])

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    frame = imutils.resize(frame,width=600)
    blurred = cv2.GaussianBlur(frame,(11,11),0)
    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,white_hsv_lo,white_hsv_hi)    # differentiate only the required color
    mask = cv2.erode(mask,None,iterations=2)    # helps remove the noise
    mask = cv2.dilate(mask,None,iterations=2)    # helps increase the size of the object
    # if found some points on the object, contous connects all the points and gives a kind of outline for the object
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]  
    center = None
    if len(cnts) > 0:     # if there is a change in the contours{movement in any direction}
        c = max(cnts,key=cv2.contourArea)      # largest contour in the mask
        (x,y),radius = cv2.minEnclosingCircle(c)    # draw the minimum enclosing circle
        M = cv2.moments(c)    # helps to find the center of the object
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))     #coordinates of the center
        if radius>10:    # if the radius is greater than 10, then only draw the circle
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)    # draw the minimum enclosing circle
            cv2.circle(frame,center,5,(0,0,255),-1)    # draw the center point of the object
            print(center)
            if radius>250:
                print("stop")
            else:
                if center[0]<150:
                    print("left")
                elif center[0]>450:
                    print("right")
                elif center[1]<150:
                    print("up")
                elif center[1]>450:
                    print("down")
                elif radius<250:
                    print('front')
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

           


>>>>>>> 6d1b335 (Initial commit)

'''
Haar Cascade frontalFace Algorithm:
- ML based algorithm {Adaboost Algo} uses mathematical functions to process pixels and detects faces oriented towards the camera
- selects features with specific patterns having contrasting pixel intensities that are common in human faces.
'''
import cv2
import os

dataset = 'dataset'
name = 'Unknown'
path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)

WIDTH,HEIGHT = 130,100

harCasxml='haarcascade_frontalface_default.xml'
# Load the cascade
haar_cascade = cv2.CascadeClassifier(harCasxml)
cam = cv2.VideoCapture(0)
count = 1

while count<31:
    _,img= cam.read()
    greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(greyImg,1.3,4)
    if face is not None:
        for (x,y,w,h) in face:
            print('face detected')
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            face_only = greyImg[y:y+h,x:x+w]
            resizeImg = cv2.resize(face_only,(WIDTH,HEIGHT))
            cv2.imwrite(f'{path}/{count}.jpg',resizeImg)
            count+=1
    else:
        print('No Face Found')
    cv2.imshow('Face Detection',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print('Collecting Samples Completed')
cam.release()
cv2.destroyAllWindows()



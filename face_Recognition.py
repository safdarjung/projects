'''
FisherFace Recognizer: helps to recognize features that may differ from person to person (Principle Component Analysis)
- we will use this model and train it with the images of the person
- then we will use the model to recognize the person from the images using the euclidean distance
LBPHFace Recognizer: Local Binary Pattern Face Recognizer is a texture operator.
- it tries to find the structure of a face by comparing each pixel with its neighboring pixels
- it extracts a small part (3X3) and compares it with a threshold  (if the pixel is greater than the threshold, then it is set to 1, else 0)
- converts the 3X3 matrix into a single binary value. Repeats for the full image and gives us somewhat lower level representation of the image
'''

import cv2
import os
import numpy as np

dataset = 'dataset'
(images,labels,names,id) = ([],[],{},0)
harCasxml='haarcascade_frontalface_default.xml'
haar_cascade = cv2.CascadeClassifier(harCasxml)

for (subdirs,dirs,files) in os.walk(dataset):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dataset,subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path,0))
            labels.append(int(lable))
        id += 1
images,labels = [np.array(i) for i in [images,labels]]
WIDTH,HEIGHT = 130,100


model=cv2.face.LBPHFaceRecognizer_create()
# model=cv2.face.FisherFaceRecognizer_create()

model.train(images,labels)

cam = cv2.VideoCapture(0)
cnt = 0

while True:
    _,img= cam.read()
    greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(greyImg,1.3,4)
    if face is not None:
        for (x,y,w,h) in face:
            print('face detected')
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            face_only = greyImg[y:y+h,x:x+w]
            resizeImg = cv2.resize(face_only,(WIDTH,HEIGHT))






# # Load the cascade
# haar_cascade = cv2.CascadeClassifier(harCasxml)
# cam = cv2.VideoCapture(0)
# count = 1

# while count<51:
#     _,img= cam.read()
#     greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     face = haar_cascade.detectMultiScale(greyImg,1.3,4)
#     if face is not None:
#         for (x,y,w,h) in face:
#             print('face detected')
#             cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#             face_only = img[y:y+h,x:x+w]
#             resizeImg = cv2.resize(face_only,(WIDTH,HEIGHT))
#             cv2.imwrite(f'{path}/{count}.jpg',resizeImg)
#             count+=1
#     else:
#         print('No Face Found')
#     cv2.imshow('Face Detection',img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# print('Collecting Samples Completed')
# cam.release()
# cv2.destroyAllWindows()
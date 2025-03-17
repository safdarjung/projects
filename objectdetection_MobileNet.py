import numpy as np
import imutils
import time
import cv2

# Load the pre-trained MobileNet SSD model
model='D:\CV_Projects\pre-trained models\MobileNetSSD_deploy.caffemodel'  # Path to the model file
prototxt='D:\CV_Projects\pre-trained models\MobileNetSSD_deploy.prototxt.txt'  # Path to the model prototxt file
confThresh=0.2  # Confidence threshold for object detection

# Class labels and colors for object detection
CLASSES =['background', 'aeroplane', 'bicycle', 'bird', 'boat','bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable','dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep','sofa', 'train', 'tvmonitor']
COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))  # Generate random colors for each class

# Load the MobileNet SSD model
print('Loading model...')
net = cv2.dnn.readNetFromCaffe(prototxt,model)  # Load the model from the given prototxt and caffemodel files
print('Model loaded')

# Open the webcam
cam = cv2.VideoCapture(0)  # Open the default webcam
time.sleep(2)

# Loop to continuously detect objects in the webcam feed
while True:
    # Read a frame from the webcam
    _,frame=cam.read()
    frame=imutils.resize(frame,width=500)  # Resize the frame to a width of 500 pixels
    (h,w)=frame.shape[:2]  # Get the height and width of the frame
    imResizeBlob=cv2.resize(frame,(300,300))  # Resize the frame again to meet the input dimension requirements for the pretrained mobilenet model
    blob=cv2.dnn.blobFromImage(imResizeBlob,0.007843,(300,300),127.5)  # Convert image to blob

    # Set the input to the MobileNet SSD model
    net.setInput(blob)
    # Perform a forward pass to get object detections
    detections = net.forward()
    detShape = detections.shape[2]  # Get the shape of the detections
    for i in np.arange(0,detShape):  # Loop over each detection
        confidence = detections[0,0,i,2]  # Get the confidence of the detection
        if confidence > confThresh:  # If the detection is confident
            idx = int(detections[0,0,i,1])  # Get the index of the class label
            if idx == 5:  # If the class label is 'person'
                print('bottle detected')
            box = detections[0,0,i,3:7]*np.array([w,h,w,h])  # Get the bounding box coordinates
            (startX,startY,endX,endY) = box.astype('int')  # Convert the coordinates to integers
            label = '{}: {:.2f}%'.format(CLASSES[idx],confidence*100)  # Get the label and confidence
            cv2.rectangle(frame,(startX,startY),(endX,endY),COLORS[idx],2)  # Draw the bounding box
            y = startY - 15 if startY - 15 > 15 else startY + 15  # Calculate y coordinate for the label
            cv2.putText(frame,label,(startX,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,COLORS[idx],2)  # Put the label on the frame
    
    # Display the output frame
    cv2.imshow("Output Frame", frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cam.release()
cv2.destroyAllWindows()


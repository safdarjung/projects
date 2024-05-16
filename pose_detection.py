'''
angle between right hip and nose is used for calculating if the body is tilted in any direction
nose_shoulder_ratio is used for calculating if the body is leaning right or left

'''


import cv2
import mediapipe as mp
import math
import numpy as np
import streamlit as st

st.title('Pose_Detection App')
frame_placeholder = st.empty()
stop_button_pressed=st.button('Stop')

mp_drawing=mp.solutions.drawing_utils   #for drawing visualizations on images or videos, often used for debugging or displaying results
mp_pose=mp.solutions.pose               #provides functionalities specifically designed for pose estimation


def analyse_posture(landmarks):
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    # left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]
    nose = landmarks[mp_pose.PoseLandmark.NOSE]
    posture = "straight"
    dist_nose_shoulder_left = math.sqrt((left_shoulder.x - nose.x)**2 + (left_shoulder.y - nose.y)**2)
    dist_nose_shoulder_right = math.sqrt((right_shoulder.x - nose.x)**2 + (right_shoulder.y - nose.y)**2)
    nose_shoulder_ratio = dist_nose_shoulder_left / dist_nose_shoulder_right
    # shoulder_midpoint = np.average([left_shoulder.x, right_shoulder.x], axis=0)
    shoulder_midpoint = (math.sqrt((left_shoulder.x - right_shoulder.x)**2 + (left_shoulder.y - right_shoulder.y)**2))/2
    # hip_midpoint = np.average([left_hip.x, right_hip.x], axis=0)

    if right_shoulder.y < right_hip.y:
        right_hip_angle = math.degrees(math.atan((right_hip.y - right_shoulder.y) / (right_shoulder.x - right_hip.x)))
    else:
        right_hip_angle = math.degrees(math.atan((right_hip.y - right_shoulder.y) / (right_shoulder.x - right_hip.x)) + math.pi)
    if right_shoulder.y < nose.y:
        nose_angle = math.degrees(math.atan((nose.y - right_shoulder.y) / (right_shoulder.x - nose.x)))
    else:
        nose_angle = math.degrees(math.atan((nose.y - right_shoulder.y) / (right_shoulder.x - nose.x)) + math.pi)

# tell whether the body is tilted or not base on the angles calculated from the nose and hip
    if (right_hip_angle - nose_angle) >= 90 or (right_hip_angle - nose_angle) <= -90:    
        #  the ratio between the nose and left shoulder with respect to the nose and right shoulder is used to find the posture
        if nose_shoulder_ratio > 1.15:
            posture='right'
            print(nose_shoulder_ratio,posture)
        elif nose_shoulder_ratio < 0.85:
            posture = 'left'
            print(nose_shoulder_ratio,posture)
        elif nose_shoulder_ratio > 0.85 and nose_shoulder_ratio < 1.15:
            posture = 'straight'
            print(nose_shoulder_ratio,posture)
        else:
            pass
    elif nose.y > shoulder_midpoint-50:
        posture= "leaning forward"
        print(nose_shoulder_ratio,posture)  
    else:
        pass
    return posture

cap = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:    #setup Mediapipe instance
    while cap.isOpened() and not stop_button_pressed:
        ret,frame=cap.read()
        if not ret:
            st.write("Error: Failed to read frame from video capture")
            break
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img.flags.writeable = False        # Sets the image flag to read-only (temporary). This might be done for internal processing within MediaPipe to avoid unintended modifications.
        results = pose.process(img)
        img.flags.writeable = True
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        # extracting the joint landmarks
        try:
            landmarks=results.pose_landmarks.landmark
            posture = analyse_posture(landmarks)
#             print(f"Detected Posture: {posture}")
            cv2.putText(img, posture, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        except:
            pass
        
        mp_drawing.draw_landmarks(img,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66),thickness=2,circle_radius=2),
                                 mp_drawing.DrawingSpec(color=(245,66,230),thickness=2,circle_radius=2)
                                 )
        # cv2.imshow('MediaPipe Feed', img)
        frame_placeholder.image(img,channels='RGB')

        if cv2.waitKey(25) & 0xff == ord('q') or stop_button_pressed:
            break
    cap.release()
    cv2.destroyAllWindows()


# for lndmrk in mp_pose.PoseLandmark:
#     print(lndmrk)

# print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value] )  # landmarks full position


def analyze_posture(landmarks):
    # Essential landmarks
    neck = np.array([landmarks[1].x, landmarks[1].y])
    shoulder = np.array([landmarks[11].x, landmarks[11].y])
    hip = np.array([landmarks[23].x, landmarks[23].y])

    # Calculate vectors
    neck_to_shoulder = shoulder - neck
    neck_to_hip = hip - neck

    # Leaning angle calculation
    angle_in_radians = np.arccos(np.dot(neck_to_shoulder, neck_to_hip) / (np.linalg.norm(neck_to_shoulder) * np.linalg.norm(neck_to_hip)))

    # Thresholds (adjust based on your needs)
    leaning_forward_angle_threshold = np.deg2rad(45)
    leaning_backward_angle_threshold = np.deg2rad(120)
    tilting_threshold = np.deg2rad(30)
    straight_posture_tolerance = np.deg2rad(20)

    # Determine posture based on angles
    if angle_in_radians > leaning_forward_angle_threshold:
        posture = "Leaning Forward"
    elif angle_in_radians < leaning_backward_angle_threshold:
        posture = "Leaning Backward"
    else:
        # Check for tilting (using shoulder vector and Y-axis)
        shoulder_midpoint_y = (shoulder[:, 1] + neck[:, 1]) / 2
        tilting_vector = np.array([0, 1])
        tilting_angle = np.arccos(np.dot(neck_to_shoulder, tilting_vector) / (np.linalg.norm(neck_to_shoulder) * np.linalg.norm(tilting_vector)))
        if tilting_angle > tilting_threshold:
            posture = "Tilting Right" if shoulder_midpoint_y < neck[:, 1] else "Tilting Left"
        else:
            # Check for straight posture (considering angle tolerance)
            if abs(angle_in_radians - np.pi / 2) < straight_posture_tolerance:
                posture = "Straight Posture"
            else:
                posture = "Uncertain Posture"

    return posture

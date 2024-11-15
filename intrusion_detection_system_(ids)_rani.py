# -*- coding: utf-8 -*-
"""INTRUSION DETECTION SYSTEM (IDS)_RANI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vqAgudL4k0TLGMWXS_Nj--iTap2PaQZ5

# **INTRUSION DETECTION SYSTEM (IDS) USING PYTHON**
DATE: 6 NOVEMBER 2024

**DESCRIPTION**: THIS IS THE TASK 2 OF LEVEL 3 PROJECT OF THE INTERNSHIP OF **OPTIFYX TECHNOLOGY**. THIS WAS A 4 WEEK INTERNSHIP IN WHICH THIS IS ONE OF THE  PROJECT.

**We had to Implement a basic intrusion detection
system that can monitor network
traffic for suspicious activities and
generate alerts. Use pattern matching
or anomaly detection techniques.**

**------------------------Import required libraries--------------------------------**
"""

# Install required libraries
!pip install cvzone
!pip install mediapipe

import cv2  # Import OpenCV library for computer vision tasks
import cvzone  # Import CVZone library for pose detection
from cvzone.PoseModule import PoseDetector  # Import PoseDetector class from CVZone

# Load pre-recorded video
cap = cv2.VideoCapture('video.mp4')  # Load video file using OpenCV's VideoCapture

# Initialize pose detector
detector = PoseDetector()  # Create an instance of PoseDetector

# Initialize variables
detect_count = 0  # Initialize detection count to track human presence
sent_sms = False  # Initialize SMS sent flag to prevent multiple notifications

while True:  # Infinite loop to process video frames
    # Read image from video
    success, img = cap.read()  # Read a frame from the video using OpenCV

    # Check if image capture was successful
    if not success:  # If frame reading fails
        print("Failed to capture image. Exiting...")  # Print error message
        break  # Exit the loop

    # Find pose in image
    img = detector.findPose(img)  # Use PoseDetector to find human pose in the frame
    imlist, bbox = detector.findPosition(img)  # Get pose landmarks and bounding box

    # Check if pose landmarks are detected
    if len(imlist) > 0:  # If pose landmarks are found
        print("Human Detect")  # Print detection message
        detect_count += 1  # Increment detection count

        # Check if detection count exceeds threshold (50)
        if detect_count > 50 and not sent_sms:
            # Replace SMS sending with alternative notification
            print("Intrusion detected!")  # Print notification message
            sent_sms = True  # Set SMS sent flag to prevent multiple notifications
    else:  # If no pose landmarks are found
        detect_count = 0  # Reset detection count
        sent_sms = False  # Reset SMS sent flag

    # Display image
    cv2.imshow("Output", img)  # Display the output frame using OpenCV

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Check for 'q' key press
        break  # Exit the loop

# Release video and close window
cap.release()  # Release video capture resource
cv2.destroyAllWindows()  # Close all OpenCV windows

"""Explanation of Key Components:

1. OpenCV (cv2): A computer vision library used for image and video processing.
2. CVZone: A library built on top of OpenCV for pose detection and tracking.
3. PoseDetector: A class from CVZone used to detect human poses in images.
4. VideoCapture: An OpenCV function to load video files or capture live video.
5. findPose: A PoseDetector method to detect human poses in images.
6. findPosition: A PoseDetector method to get pose landmarks and bounding boxes.
7. imshow: An OpenCV function to display images.
8. waitKey: An OpenCV function to handle keyboard events.
"""
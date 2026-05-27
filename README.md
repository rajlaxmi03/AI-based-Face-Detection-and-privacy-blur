
# AI-based-Face-Detection-and-privacy-blur


## Institute Name
KodNest

## Problem Statement
Problem 2 - Face Blur on Video Chunks / Images

## About Project
This project is made using Python and OpenCV.  
The system detects faces from a video and blurs them for privacy protection.

## Technologies Used
- Python
- OpenCV

## How the Project Works

1. The input video is read frame-by-frame using OpenCV.
2. Each frame is converted into grayscale format.
3. Haar Cascade face detector is used to detect human faces.
4. Gaussian Blur is applied on detected face regions.
5. Processed frames are saved into a new output video.
## Steps to Run

1. Install libraries

pip install -r requirements.txt

2. Add input video in project folder

3. Run command

python face_blur.py --mode video --filePath input_video.mp4

## Output
Output video will be saved in:

output/output.mp4

## Conclusion
This project helped me learn basic face detection and video processing using OpenCV.

import cv2
import os
import argparse

# -----------------------------
# Face Detection Model
# -----------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# -----------------------------
# Function to Blur Faces
# -----------------------------
def process_img(img):

    # Improve brightness for low-light videos
    img = cv2.convertScaleAbs(img, alpha=1.2, beta=20)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    for (x, y, w, h) in faces:

        face_region = img[y:y+h, x:x+w]

        blurred_face = cv2.GaussianBlur(
            face_region,
            (99, 99),
            30
        )

        img[y:y+h, x:x+w] = blurred_face

    return img


# -----------------------------
# Argument Parser
# -----------------------------
args = argparse.ArgumentParser()

args.add_argument("--mode", default='video')
args.add_argument("--filePath", default='input_video.mp4')

args = args.parse_args()

# -----------------------------
# Output Folder
# -----------------------------
output_dir = './output'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# -----------------------------
# IMAGE MODE
# -----------------------------
if args.mode == "image":

    img = cv2.imread(args.filePath)

    img = process_img(img)

    cv2.imwrite(os.path.join(output_dir, 'output.png'), img)

# -----------------------------
# VIDEO MODE
# -----------------------------
elif args.mode == 'video':

    cap = cv2.VideoCapture(args.filePath)

    ret, frame = cap.read()

    output_video = cv2.VideoWriter(
        os.path.join(output_dir, 'output.mp4'),
        cv2.VideoWriter_fourcc(*'mp4v'),
        25,
        (frame.shape[1], frame.shape[0])
    )

    while ret:

        frame = process_img(frame)

        output_video.write(frame)

        cv2.imshow("Face Blur Output", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        ret, frame = cap.read()

    cap.release()
    output_video.release()
    cv2.destroyAllWindows()

# -----------------------------
# WEBCAM MODE
# -----------------------------
elif args.mode == 'webcam':

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    while ret:

        frame = process_img(frame)

        cv2.imshow('Webcam Face Blur', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        ret, frame = cap.read()

    cap.release()
    cv2.destroyAllWindows()
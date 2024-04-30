import os
import cv2
import numpy as np

# OpenCV의 얼굴 감지기 준비
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def has_single(image_paths):
    print("has single")
    return len(image_paths)

def remove_non_single_faces(image_paths):
    imgs = os.listdir(image_paths)
    for img in imgs:
        new_img_path = image_paths + "/" + img
        if new_img_path.endswith(".jpg"):
            img = cv2.imread(new_img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            print("faces count:", faces, len(faces))

        # 사진에 얼굴이 한 명만 존재하지 않으면 삭제
        if (len(faces) != 1):
            os.remove(new_img_path)
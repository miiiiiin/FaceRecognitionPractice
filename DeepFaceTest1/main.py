import cv2
import os
import json
from deepface import DeepFace

# face matching
result = DeepFace.verify(img1_path="ji1.jpg", img2_path="db/taylor2.jpg")
# 데이터 간결하게 보기 위해 json.dumps 적용
# print(json.dumps(result, indent=2))

# find face in db
# img = cv2.imread(os.path.join("./db", "ji1.jpg"))
# image_face = DeepFace.extract_faces(img)
# print(image_face)

# identity hash  ...  threshold  distance
# img_path의 이미지와 유사한걸 db 폴더에서 추려냄

dfs = DeepFace.find(img_path="ji1.jpg", db_path="./db")
print(dfs)

# face analysis
# objs = DeepFace.analyze(img_path = "ji1.jpg",
#         actions = ['age', 'gender', 'race', 'emotion']
# )
objs = DeepFace.analyze(img_path = "ji1.jpg")
print(json.dumps(objs, indent=2))

import os
import shutil
import json
from PIL import Image
from deepface import DeepFace

w = 255

# data_dir = "Celebrity Faces Dataset"
data_dir = "Celeb Dataset"
for directory in os.listdir(data_dir):
        joined = os.path.join(data_dir, directory)
        if os.path.isdir(joined):
                first_file = os.listdir(joined)[0]
                first_file_path = joined+"/"+first_file
                if os.path.isfile(first_file_path):
                        img = Image.open(first_file_path)
                        img = img.resize((w, int(w * (img.height / img.width))))
                        print("imgsize:", img.width, img.height)
                        print("firstfile:", first_file)
                        print("outputfile:", os.path.join(data_dir, directory, first_file))
                        output_filename = "Samples"
                        # os.makedirs(os.path.dirname(output_filename), exist_ok=True)
                        img.save(os.path.join(output_filename, f"{directory}.jpg"))
                        # shutil.copyfile(os.path.join(data_dir, directory, first_file), os.path.join("Samples", f"{directory}.jpg"))


smallest_distance = None

for file in os.listdir("Samples"):
        print("file: ", file)
        if file.endswith(".jpg"):
                result = DeepFace.verify("person8.jpg", f"Samples/{file}")
                print(json.dumps(result, indent=2))
                if result['verified']:
                        print("This person looks exactly like", file.split(".")[0])
                        break
                if smallest_distance is None:
                        smallest_distance = (file.split(".")[0], result['distance'])
                else:
                        smallest_distance = (file.split(".")[0], result['distance']) if result['distance'] < smallest_distance[1] else smallest_distance
else:
        print(f"No exact match found! Closest match is {smallest_distance[0]}")

# result = DeepFace.verify("person1.jpg", f"Samples/Angelina Jolie.jpg ")
# distance: 두 이미지가 얼마나 동떨어져있는지 확인 (distance가 낮으면 두 이미지가 유사하다는 의미)


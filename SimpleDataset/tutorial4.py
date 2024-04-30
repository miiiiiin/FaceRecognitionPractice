from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import torchvision
from torchvision import transforms

# ransforms.Compose를 통해 Resize, ToTensor, Normalize를 시켜줍니다. 이미지의 높이와 너비가 조금씩 다를 수 있고, 이미지 데이터를 정규화 해주기위해 전처리를 진행합니다. ToTensor를 통해 이미지를 텐서형태로 바꿔줍니다.
# trainset을 ImageFolder를 사용하여 저장
# trans를 transform 파라미터 값으로 넣어 데이터가 전처리 될 수 있도록 한다.
trans = transforms.Compose(([transforms.Resize(255, 255), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]))
trainset = torchvision.datasets.ImageFolder(root="../ImageCrawler/train_dataset/")

trainset.__getitem__(5)

len(trainset)

classes = trainset.classes
print(classes)

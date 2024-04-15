from torchvision import transforms
from torchvision.datasets import ImageFolder

# transform 정의 : Resize 후 Tensor 형태로
transform = transforms.Compose([
    transforms.Resize((250, 250)),
    transforms.ToTensor(),
])

data = ImageFolder(root="../ImageCrawler/train_dataset",
                   transform=transforms.ToTensor())

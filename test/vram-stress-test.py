import torch
import torchvision.models as models

# load ResNet-152 model
model = models.resnet152(pretrained=True)

# move model into GPU
device = torch.device("cuda")
model = model.to(device)

# set large batch size
batch_size = 32

# generate input data
input_data = torch.randn(batch_size, 3, 224, 224).to(device)

# run
output = model(input_data)

# output
print("GPU 메모리 사용량 (bytes):", torch.cuda.max_memory_allocated(device=device))

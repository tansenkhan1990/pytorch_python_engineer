import torch
import numpy as np
# a = torch.ones(3)
# print('torch ')
# print(a)
# b = a.numpy()
# print('numpy array')
# print(b)
# a = a + 1
# print('a after add ones')
# print(a)
# print('after add one in a and check b')
# print(b)

a = np.ones(3)
print('numpy array')
print(a)
b= torch.from_numpy(a)
print('after convery into tensor')
print(b)

# CPU and GPU
if torch.cuda.is_available():
    device = torch.device('cuda')
    x = torch.ones(5 , device = device)
    # another example
    y = torch.ones(5)
    y = y.to(device)
    # change the device to cpu 
    y = y.to('cpu')

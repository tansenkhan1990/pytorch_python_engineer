import torch
x = torch.rand(3 , requires_grad= True)
print(x)
y = x * 4
y = y.mean()
y.backward()
print(x.grad)

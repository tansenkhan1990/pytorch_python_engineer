import torch
x = torch.rand(3 , requires_grad= True)
print(x)
y = x * 4
# y = y.mean()
v = torch.tensor([1,3,4] , dtype = torch.float64)
y.backward(v)
print('this is gradient value')
print(x.grad)

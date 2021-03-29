import torch

x = torch.ones(3, 2 ,5)
y = torch.zeros(3, 2 ,5)

print('x datatype : ', x.dtype)
print('x datatype : ', y.dtype)
print('x size : ', x.size())
# list to tensor
newtensor = torch.tensor([5,3,1,2,3,4,5,66])
print('this is a newtensor')
print(newtensor)
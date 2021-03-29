import torch

x = torch.ones(3, 2 ,5)
y = torch.zeros(3, 2 ,5)

# print('x datatype : ', x.dtype)
# print('x datatype : ', y.dtype)
# print('x size : ', x.size())
# # list to tensor we can also tranfer numpy array or list into a tensor
# newtensor = torch.tensor([5,3,1,2,3,4,5,66])
# print('this is a newtensor')
# print(newtensor)
# row and column operation
rowAndColumn = torch.rand(3,4)
print('row and column')
print(rowAndColumn)
print('first row and all column')
print(rowAndColumn[1,:])
print('all row and first column')
print(rowAndColumn[:,1])
print('first element of first row')
print(rowAndColumn[1,1])
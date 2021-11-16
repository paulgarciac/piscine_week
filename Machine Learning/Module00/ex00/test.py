from vector import Vector

### Vector Columns 
v1 = Vector([[2] , [3] , [5]])
v2 = Vector([[10] , [5], [2]]) 
# print(v1 + v2)
# print(v1.shape())

### Vector Column and line
v1 = Vector([[2] , [3] , [5]])
v2 = Vector([[10 , 5, 2]]) 
m1 = Vector([[10, 5, 2],[9, 4, 1]]) 
m2 = Vector([[10, 5, 2],[9, 4, 1]]) 

### Dot products
print("v1 i", len(v1.datalist[:]))
print("v1 j", len(v1.datalist[0][:]))
print("v2 i", len(v2.datalist[:]))
print("v2 j", len(v2.datalist[0][:]))
print("m1 i", len(m1.datalist[:]))
print("m1 j", len(m1.datalist[0][:]))

print("Dot products")
print(m1.__dot__(m2).datalist)

print("Transpose two vectors and a matrix")
print(v1.datalist, "transpose :", v1.T().datalist)
print(v2.datalist, "transpose :", v2.T().datalist)
print(m1.datalist)
print(m1.T().datalist)

print("printing shapes")
print(m1.shape())
print(m1.T().shape())

### Simple one dimension Vectors 
v1 = Vector([2 , 3 , 5])
v2 = Vector([10 , 5, 5])
print(v1 + v2)

### Vector column & scalar 
# v1 = Vector([[2] , [3] , [5]])
# v2 = Vector(5)  
# print(v2.datalist)
# print(v1.datalist)
# print(v2.shape())




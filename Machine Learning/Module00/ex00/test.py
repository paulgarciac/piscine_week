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

### Dot products
print("i : ", len(v1.datalist[:]))
print("j : ", len(v1.datalist[0][:]))
print("v2 i : ", len(v2.datalist[:]))
print("v2 j : ", len(v2.datalist[0][:]))
print("m1 i : ", len(v2.datalist[:]))
print("m1 j : ", len(v2.datalist[0][:]))

print("print Transpose")

print(v1.T())
print(v2.T())
print(m1.T())

### Simple one dimension Vectors 
# v1 = Vector([2 , 3 , 5])
# v2 = Vector([10 , 5, 5])
# print(v1.datalist[1])
# print(v1 + v2)
# print(v1.shape())

### Vector column & scalar 
# v1 = Vector([[2] , [3] , [5]])
# v2 = Vector(5)  
# print(v2.datalist)
# print(v1.datalist)
# print(v2.shape())




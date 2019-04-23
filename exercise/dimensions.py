dimensions = (200, 50)
print(dimensions)
print(dimensions[1])

# dimensions[0] = 250   类型错误！元组的元素不能改变，'元组'对象不支持项目分配

for dimension in dimensions:
    print(dimension)

# 虽然不能修改元组的元素，但是可以给存储元组的变量赋值
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100, 200)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


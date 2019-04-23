cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#sort()永久性地按照字母升序排列（改变原来cars列表中的元素顺序）
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#sort(reverse = True)永久性地按照字母降序排列（改变原来cars列表中的元素顺序）
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the orignial list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))	#升序排列，不改变原来cars列表中的元素顺序
print(sorted(cars, reverse=True))	#升序排列，不改变原来cars列表中的元素顺序

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the orignial list:")
print(cars)
#reverse()永久性地反转原来列表中元素的排列顺序
print("\nHere is the reversed list:")
cars.reverse()
print(cars)

#函数len()返回列表长度（即元素个数）
l=len(cars)
print(l)




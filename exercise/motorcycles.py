motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#append()在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

#insert()在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(1,'ducati')
print(motorcycles)

#del语句删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#pop()删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()	#删除末尾元素并存储
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)	#删除指定元素并存储
print(motorcycles)
print(popped_motorcycle)

#remove()根据元素值删除元素
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki', 'ducati']
print(motorcycles)
del_motor = 'ducati'
motorcycles.remove(del_motor)		#每次仅删除列表中与指定元素值相同第一个元素
print(motorcycles)
motorcycles.remove(del_motor)
print(motorcycles)

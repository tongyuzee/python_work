for value in range(0,5):
	print(value)

numbers = list(range(0,5))
print(numbers)

even_numbers = list(range(0,11,2))
print(even_numbers)


squares = []
print(squares)
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)

squares = []
print(squares)
squares = [value ** 2 for value in range(1,11)]
print(squares)
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = []
requested_toppings = ['mushrooms', 'green peppers', 'french fries', 'extra cheese']

if requested_toppings:		# 当列表名用在条件表达式中时，python将在列表中至少含有一个元素时返回True，列表为空时返回False。
	for requested_topping in requested_toppings:
		if requested_topping not in available_toppings:
			print("Sorry, we don't have " + requested_topping + ".")
		else:
			print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure ypu want a plain pizza?")

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

x=user_0.items()		# 返回键-值对列表
print(x)
# 遍历所有键-值对
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

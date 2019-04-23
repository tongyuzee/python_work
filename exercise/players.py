players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:5])
print(players[2:])
#负数索引返回离列表末尾相应距离的元素
print(players[-3:])		#返回最后三个元素
print(players[-3:-1])
print(players[:-3])		#相当于players[:2]
print(players[:2])

print("Here are the first three players on my team:")
for player in players[:3]:
	print("\t" + player.title())

# copy_players = players[:]		# 创建一个新的列表，复制列表中的元素，两个列表中的元素相同
copy_players = players 			# 指向同一个列表，相当于复制列表地址
print(copy_players)
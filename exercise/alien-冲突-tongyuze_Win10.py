# 字典
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 添加键-值对 
print(alien_0)
alien_0['x_position'] = 5
alien_0['y_position'] = 20
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print("The alien is " + alien_0['color'] + '.')
# 修改字典中的值
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 删除键-值对
print(alien_0)
del alien_0['speed']
print(alien_0)

favorite_languages = {
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'python',
}

print(favorite_languages)
# 遍历所有键-值对
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language +".")
# 遍历所有键
# for name in favorite_languages.keys():
print(favorite_languages.keys())
for name in favorite_languages:		# 遍历字典时，默认遍历所有的键
	print(name.title())
# 遍历所有值
print("The favorite languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):	# set()找出列表中独一无二的元素
	print(language.title())
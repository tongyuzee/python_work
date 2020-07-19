# -*- coding: utf-8 -*
# -------------------
# Author: tongyuze
# Date: 
# -------------------
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
print(set(pets))
pets.remove('cat')  # 每次仅删除列表中的第一个元素
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

from random import *

users = range(1, 21)
users = list(users)

shuffle(users)
Winners = sample(users, 4) # users에서 4명 뽑아서 1명은 치킨, 3명은 커피

print("치킨 당첨자 : {0}".format(Winners[0]))
print("커피 당첨자 : {0}".format(Winners[1:]))
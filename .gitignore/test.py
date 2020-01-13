import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chosen = random.choice(list)
print(chosen)
list.remove(chosen)
print(list)
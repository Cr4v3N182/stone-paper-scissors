from random import randint

dict_items = {1: "stone", 2: "paper", 3: "scissors"}

def draw_function():
    random_num = randint(1,3)
    item = dict_items[random_num]
    return item
print(draw_function())





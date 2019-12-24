# モジュールを用いる際はimport hogehoge
import random

print(random.random())
print(random.randint(0, 6))
number_list = [0, 1, 2, 3, 4, 5]
random.shuffle(number_list)
print(number_list)
print(random.choice(number_list))

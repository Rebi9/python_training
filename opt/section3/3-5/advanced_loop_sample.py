# while文

counter = 1
while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter = counter + 1

print("-----------")

# ループのelse
# Pythonではループが終了した後に実行されるブロックを定義することができる。

number = 59
for num in range(2, number):
    if number % num == 0:
        print(number, "は素数ではありません。")
        break
else:
    print(number, "は素数です。")

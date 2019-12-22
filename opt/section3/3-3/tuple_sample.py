# タプルはリストに似ているが、要素の変更ができない。

month_names = ("January", "February", "March", "April", "May", "June")
print(month_names[0])

# ↓はエラー
# month_names[0] = "睦月"

# タプル同士の結合は可能
month_names = month_names + ("July", "August", "September", "October", "November", "December")
print(month_names[11])

# 要素が1つのタプルを作成する際はカンマをつける。(10)だと括弧付きの数値と解釈されてしまう。
single_element_tuple = (10,)


### タプルの利点
# タプルは変更されないため、ディクショナリのキーやsetの要素に用いることができる。

pref_capitals = {(43.06, 114.34) : "北海道(札幌)", (40.82, 140.74) : "青森(青森)", (39.70, 141.15) : "岩手(盛岡)"}
location = (39.70, 141.15)
for key in pref_capitals:
    if location == key:
        print(pref_capitals[key])
        break

location = (41, 140)
nearest_capital = ""
nearest_distance = 10000000000
for key in pref_capitals:
    distance = (location[0] - key[0]) ** 2 + (location[1] - key[1]) ** 2
    if nearest_distance > distance:
        nearest_distance = distance
        nearest_capital = pref_capitals[key]
print(nearest_capital)


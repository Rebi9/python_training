# setは集合を扱うために作られた。
# setにリストやディクショナリは変更できてしまうので、要素として追加できない。

# 和集合は|で求める。
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8 ,13}

prime_fib = prime | fib
print(prime_fib)

# 差集合は-で求める。
dice = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6, 8, 10}

odd_dice = dice - even
print(odd_dice)

# 論理積は&、排他論理和は^で求める。
prefs = {"北海道", "青森", "秋田", "岩手"}
capitals = {"札幌", "青森", "秋田", "盛岡"}

pref_cap = prefs & capitals
print(pref_cap)

pref_cap2 = prefs ^ capitals
print(pref_cap2)


###

# リストはsetに変換可能。
codon = ["ATG", "GGC", "TCC", "AAG", "TTC", "TGG", "GAC", "TCC"]
codon_set = set(codon)
print(len(codon), len(codon_set))

# setはin演算子で要素の検索が可能。
# <=で部分集合かどうかを調べることができる。
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8 ,13}
prime_fib = prime & fib
message = "は素数で、フィボナッチ数でもある"
if 13 in prime_fib:
    print("13" + message)
if {2, 3} <= prime_fib:
    print("2, 3" + message)

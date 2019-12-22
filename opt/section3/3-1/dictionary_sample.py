# ディクショナリ
# JavaのMapに近い概念か

profile = {"名前" : "桜木花道", "高校" : "湘北高校", "部活" : "バスケット部"}

print(profile["名前"])
print(profile)

profile["名前"] = "三井寿"
print(profile)

profile["ポジション"] = "SG"
print(profile)

del profile["ポジション"]
print(profile)

# ディクショナリをループに用いるとキーに対するループを組むことができる
for key in profile:
    print(key, profile[key])

### ディクショナリの利用例

# キーに存在しない値を受け取った時のことを考えた、エラーハンドリングが重要
def convert_number(num):
    roman_nums = {1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX"}

    if num in roman_nums:
        return roman_nums[num]
    else:
        return "変換出来ません"


# PythonのTrue, Falseは大文字始まり。(true, falseではない。)

if True:
    print("true")

# Pythonの「または」および「かつ」はor, and.(||, &&ではない。)
if True and True:
    print("and")

if True or False:
    print("or")

# Javaと異なり、a > 100 and a < 150を 100 < a < 150と書ける。
v = 30000
if v < 28400:
    print("地上に落下します。")
if 28400 <= v < 40300:
    print("月とお友達です。")
if 40300 <= v < 60100:
    print("惑星の仲間入りです。")
if 60100 <= v:
    print("アルファケンタウリを目指せ。")

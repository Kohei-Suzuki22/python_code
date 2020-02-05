
# 型変換
print(int(2.5))
print(float(2))
print("I have " + str(2) + "pens.")

# dict (Hash)
sales = {"Tokyo":100,"new york":120, "paris": 80}
## ※ 注意: dictのkeyも型の定義をしっかりしないとエラーになる。



# While文のelse
a = 5
while a > 0:
    print("a =", a)
    a -=1
else:
    print("end of while.")


# 関数
def f(x,a=3):
    return a * x ** 2, 2 * a * x

y, y_prime = f(1)

print(y)
print(y_prime)


# library

## ※ 注意: ライブラリと同じ名前のファイルを作成してしまうとうまくライブラリが読み取れない。

import math
sin = math.sin(math.pi/2)
print(sin)

import math as m
## as ~ によって、mathのエイリアスを提供
sin = math.sin(m.pi/2)
print(sin)

from math import cos,pi
## from ... import ~ によって、 ....ライブラリの ~ 関数を引数なしでそのまま使えるようになる
print(cos(pi))

from math import *
## ワイルドカード(*)によって、mathライブラリの関数全て使えるようになる。

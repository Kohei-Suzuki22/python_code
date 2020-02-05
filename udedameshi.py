import matplotlib.pyplot as plt
import numpy as np

# 配列の初期値に0を入れて、メモリーを確保。

a = 5
x = [0.2]   # x(t)を格納
t = []      # tを格納
x1 = []     # x(t+1)を格納

# x(t)の関数
def func(x,t,a):
    return a * x[t] * (1 - x[t])

# 配列xにt=0~999までのx(t)の値をいれる。
for i in range(1000):
    x.append(func(x,i,a))
    x1.append(func(x,i+1,a))
    t.append(i)

# 配列の要素数合わせ。
x.pop(1)

x = np.array(x)
t = np.array(t)
x1 = np.array(x1)
#
plt.plot(t,x)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

# plt.scatter(x,x1)
# plt.xlabel("x(t)")
# plt.ylabel("x(t+1)")
# plt.show()

# plt.plot → 線グラフ
# plt.scatter → 散布図

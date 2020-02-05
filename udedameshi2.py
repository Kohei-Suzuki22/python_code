import matplotlib.pyplot as plt
import numpy as np

# x(t)の関数
def func(x,t,a):
    return a * x[t] * (1 - x[t])

def set_a_range():
    # a_range = np.arange(3,4,0.001)  ← 誤差がでる。
    a_range = np.arange(3000,4000,1)
    return  np.array(list(map(lambda x: x/1000, a_range)))

# a_range * a_range の二次配列 (1000 * 1000 = 1000000)
def make_2d_array(range):
    return np.array([[0 for i in range] for j in range], dtype = "float")

a_range = set_a_range()
_2d_array = make_2d_array(a_range)

for i,a in enumerate(a_range):
    x = [0.2]
    for t in range(1500):
        x.append(func(x,t,a))
        # t < 500 の範囲を消す。
        if t >= 500:
            _2d_array[i][t-500] = x[t]


# グラフプロット
for i,a in enumerate(a_range):
    y = [0] * len(a_range)
    for j,_ in enumerate(a_range):
        y[j] = _2d_array[j][i]
    plt.scatter(a_range,y,s=5)

plt.xlabel("a")
plt.ylabel("x(t)")
plt.xlim(3.000,4.000)
plt.show()

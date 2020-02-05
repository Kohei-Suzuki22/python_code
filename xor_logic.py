import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# パーセプトロンによるANDゲート
def ANDgate(x1, x2):
    f = 1.0 * x1 + 1.0 * x2
    if f <= 1.0:
        y = 0
    else:
        y = 1
    return y

# パーセプトロンによるORゲート
def ORgate(x1, x2):
    f = 0.5 * x1 + 0.5 * x2
    if f <= 0.2:
        y = 0
    else:
        y = 1
    return y

# パーセプトロンによるNANDゲート
def NANDgate(x1, x2):
    f = -0.8 * x1 + -0.8 * x2
    if f <= -0.9:
        y = 0
    else:
        y = 1
    return y

x1 = np.arange(-2.2, 2.2, 0.1)            # x1軸を作成
x2 = np.arange(-2.2, 2.2, 0.1)            # x2軸を作成
X1, X2 = np.meshgrid(x1, x2)              # x1軸とx2軸からグリッドデータを作成

# 多層パーセプトロンの計算をグリッドで実行
Y = np.zeros((len(X1), len(X2)))
for i in range(len(X1)):
    for j in range(len(X2)):
        out1 = NANDgate(X1[i, j], X2[i, j])
        out2 = ORgate(X1[i, j], X2[i, j])
        Y[i, j] = ANDgate(out1, out2)

# ここからグラフ描画
# フォントの種類とサイズを設定する。
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Times New Roman'

# グラフの入れ物を用意する。
fig = plt.figure()
ax1 = Axes3D(fig)

# 軸のラベルを設定する。
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y')

# データプロットする。
ax1.scatter3D(X1, X2, Y)

# グラフを表示する。
plt.show()
plt.close()



import numpy as np

# numpy を使うことにより、「数式の見た目どおり」に実装できるようになる。

I = np.array([[1,0],[0,1]])
C = np.array([[1,2],[3,4]])

print(I[0])
print(C)

## ※注意: I * C とするとベクトルの要素積のなる。(内積にはならない。)


# 内積
## → np.matmul() もしくは np.dot()を用いる。


# matmul() と dot()の違い
## → 二次元では同じ挙動。 三次元以降になると変化。
## ブロードキャストへの対応が異なる。


# numpyの配列の初期化
## → .zeros() や .ones()を使う。
np.zeros(4)
np.ones(4)

np.arange(4)
# => array([0,1,2,3])
np.arange(4,10)
# => array([4,5,6,7,8,9])
np.arange(4,10,3)       # ← 第三引数で間隔を指定。
# => array([4,7])

# 多次元配列 → 1次元配列 or 1次元配列 → 多次元配列
## → .reshape(1,2)を使う。 ← 1行2列の行列を生成。


# スライス
a = np.arange(10)
a[1:5:2]    # 第三引数は要素取得の間隔を指定。
# => [1,3]
a[::-1]
# => [9,8,7,6,5,4,3,2,1,0]


a = np.arange(1,7).reshape(2,3)
a # => array([[1,2,3],
            # [4,5,6]])

a[:2]  # => array([[1,2,3],
                # [4,5,6]])

a[:2, 0] # ← 第二引数は、各要素となっている配列の成分を取得
         # つまり、[1,2,3] と [4,5,6] それぞれのindex(0)の値 [1,4]を返す。

a[:2, 0:2]
# => array[[1,2],
#           [4,5]]

a[:2, ::-1]
# => array[[3,2,1],
#          [4,5,6]]


# np.newaxis

## → 要素を持たない次元を追加する。
a = np.array[1,2,3]
a[:, np.newaxis]    # ← 列ベクトルの作成。
# => array([[1],
#           [2],
#           [3]])

a[np.newaxis,:]     # ← 行ベクトルの作成。
# => array([[1,2,3]])

## ※ a[:,np.newaxis] == a[:,None]
## ※ a[np.newaxis,:] == a[None,:]

import numpy as np
import matplotlib.pyplot as plt


class SimplePerceptron(object):

    '''
    単純パーセプトロン
    '''

    # オブジェクトの長さと重み、バイアスを初期化。
    def __init__(self,input_length):
        self.input_length = input_length
        # np.random.nornal(loc=0.0,scale=1.0,size=None)
        # → 平均loc, 標準偏差scaleを正規分布に従う乱数を返す。
        self.w = np.random.normal(size=(input_length,))
        self.b = 0.

    # xを入力して、戻り値をyとして伝播する。
    def forward(self, x):
        y = step(np.matmul(x,self.w.T) + self.b)
        return y


    # 誤差計算。Δw,Δbを求める。
    # t は期待値(正解の出力)
    def compute_deltas(self, x, t):
        y = self.forward(x)
        delta = y - t
        dw = x * delta
        db = delta
        return dw, db

    # ステップ関数

def step(fx):
    return 1 * (fx > 0)

if __name__ == "__main__":
    np.random.seed(123)

    '''
    1.データの準備
    '''
    d = 2   # 入力次元
    N = 20  # 全データ数

    mean = 5    # ニューロン発火の基準。平均値がmeanを超えていれば発火。

    # np.random.randn(10,2) → 10行2列 の行列。
    x1 = np.random.randn(N//2, d) + np.array([0,0])
    x2 = np.random.randn(N//2, d) + np.array([mean,mean])

    # x1,x2の要素数がそれぞれ10個。 x = x1 + x2 で要素は20個。
    # x1の10個は0に近い値が入る。x2の10個はmeanに近い値が入る。
    x = np.concatenate((x1,x2), axis = 0)
    # axis = 0  → shapeで表したときの 0番目の要素について連結する。


    # N//2個の要素を持つ t1とt2を作成。
    # t1 は値が 0 になる要素を N//2個。
    # t2 は値が 1 になる要素を N//2個。
    t1 = np.zeros(N//2)
    t2 = np.ones(N//2)

    t = np.concatenate((t1,t2))

    # plt.plot(x,t)
    # plt.show()


    '''
    2.モデルの構築
    '''
    model = SimplePerceptron(d)


    '''
    3.モデルの学習
    '''


    def compute_loss(dw,db):
        return all(dw == 0) * (db == 0)

    def train_step(x,t):
        dw, db = model.compute_deltas(x,t)
        loss = compute_loss(dw,db)
        model.w = model.w - dw
        model.b = model.b - db
        return loss

    while True:
        classified = True
        for i in range(N):
            loss = train_step(x[i], t[i])
            classified *= loss

        if classified:
            break

    '''
    4.モデルの評価
    '''

    print("w:", model.w)
    print("b:", model.b)

    y = model.w[0] * x1 + model.w[1] * x2 + model.b


    print("0,0 =>", model.forward([0,0]))
    print("5,5 =>", model.forward([5,5]))

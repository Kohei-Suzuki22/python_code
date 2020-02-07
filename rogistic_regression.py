# ロジスティック回帰のモデルでORゲートを再現する。


import numpy as np

class LogisticRegression(object):
    '''
    ロジスティック回帰
    '''

    # 初期設定
    ## モデルへの入力の長さを設定
    ## パラメータ w, b の初期値を設定
    def __init__(self,input_length):
        self.input_length = input_length
        # input_length個の正規分布に従う乱数を返す。
        self.w = np.random.normal(size=(input_length,))
        self.b = 0.

    # ※__call__ : これをクラス内に実装すると、インスタンスを関数として
    #              呼び出せるようになる。
    ## model(x)を呼び出すだけで、model.forward(x)が実行される。
    def __call__(self,x):
        return self.forward(x)

    # xを入力して、戻り値をyとして伝播する。
    def forward(self,x):
        return sigmoid(np.matmul(x,self.w) + self.b)

    # 勾配を計算する。(誤差計算)
    def compute_gradients(self,x,t):
        y = self.forward(x)
        delta = y - t
        dw = np.matmul(x.T, delta)
        db = np.matmul(np.ones(x.shape[0]), delta)
        return dw,db


# シグモイド関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    np.random.seed(123)


    '''
    1.データの準備
    '''
    # OR
    # 入力x
    x = np.array([[0,0],[0,1],[1,0],[1,1]])
    # 期待値t
    t = np.array([0,1,1,1])

    '''
    2.モデルの構築
    '''
    model = LogisticRegression(input_length=2)

    '''
    3.モデルの学習
    '''
    # 交差エントロピー誤差関数
    def compute_loss(t,y):
        return (-t * np.log(y) - (1-t) * np.log(1-y)).sum()

    # 勾配降下法(パラメータ更新)
    def train_step(x,t):
        dw,db = model.compute_gradients(x,t)
        # learning_rate(学習率)を0.1と定めて使用する
        lr = 0.1
        model.w -= lr * dw
        # model.w = model.w - lr * dw
        model.b -= lr * db
        # model.b = model.b - lr * db
        loss = compute_loss(t,model(x))
        return loss

    update_counts = 100

    for update_count in range(update_counts):
        train_loss = train_step(x,t)

        if update_count % 5 == 0 or update_count == update_counts - 1:
            print("epoch: {}, loss: {:.3f}".format(update_count+1, train_loss))



    '''
    4.モデルの評価
    '''
    for input in x:
        print("{} => {:.3f}".format(input,model(input)))


class Company:
    # 「__」 はアンダーバー二つ。
    # __init__ の最初の引数は selfをとらなければならない。
    def __init__(self, sales, cost, persons):
        self.sales = sales
        self.cost = cost
        self.persons = persons

    def get_profit(self):
        return self.sales - self.cost



comp_A = Company(100, 80, 10)
comp_B = Company(40, 60, 20)


print(comp_A.sales)
# 関数呼び出しの際は、「.get_profit()」のように()をつけなければならない。
print(comp_A.get_profit())
comp_A.sales = 0
print(comp_A.sales)
print(comp_A.get_profit())

print(comp_B.get_profit())

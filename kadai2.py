import numpy as np

update_count = 1000
w1 = np.random.rand(3)
w2 = np.random.rand(3)
x = [[0,0,1],[0,1,1],[1,0,1],[1,1,1]]

and_expect_values = [0,0,0,1]
or_expect_values = [0,1,1,1]
nand_expect_values = [1,1,1,0]
xor_expect_values = [0,1,1,0]
learning_coefficient = np.random.rand(1)


flow_of_change_weights1 = np.array([[0,0,0] for i in range(update_count)], dtype='float')
flow_of_change_weights2 = np.array([[0,0,0] for i in range(update_count)], dtype='float')

# ここのしきい値は w[2] 今はランダムなものが入っている。

def step_func(w,x,n):
    return 0 if w[0]*x[n][0] + w[1]*x[n][1] + w[2] < 0 else 1



for update in range(1000):
    for i in range(4):
        y = step_func(w1,x,i)
        e = y - and_expect_values[i]
        # e = y - or_expect_values[i]
        for j in range(3):
            w1[j] -= learning_coefficient * e * x[i][j]
            flow_of_change_weights1[update][j] = w1[j]

#
# for update in range(1000):
#     for i in range(4):
#         or_y = step_func(w1,x,i)
#         nand_y = step_func(w2,x,i)
#         or_e = or_y - or_expect_values[i]
#         nand_e = nand_y - nand_expect_values[i]
# #         # e = y - xor_expect_values[i]
#         for j in range(3):
#             w1[j] -= learning_coefficient * or_e * x[i][j]
#             w2[j] -= learning_coefficient * nand_e * x[i][j]
#             flow_of_change_weights1[update][j] = w1[j]
#             flow_of_change_weights2[update][j] = w2[j]

def xor(or_v, nand):
    return or_v and nand



# or_v = step_func(w1,x,0)
# nand = step_func(w2,x,0)
# y = xor(or_v,nand)
# print(y)
# or_v = step_func(w1,x,1)
# nand = step_func(w2,x,1)
# y = xor(or_v,nand)
# print(y)
# or_v = step_func(w1,x,2)
# nand = step_func(w2,x,2)
# y = xor(or_v,nand)
# print(y)
# or_v = step_func(w1,x,3)
# nand = step_func(w2,x,3)
# y = xor(or_v,nand)
# print(y)



#
y = step_func(w1,x,0)
print(y)
y = step_func(w1,x,1)
print(y)
y = step_func(w1,x,2)
print(y)
y = step_func(w1,x,3)
print(y)

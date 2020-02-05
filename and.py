import matplotlib.pyplot as plt
import numpy as np
import random


def omomi():
    omomis = []
    for i in range(3):
        omomis.append(random.random())
    return omomis

def input(x,w):
    return x[0]*w[0] + x[1]*w[1] + x[2]*w[2]

def step_func(input):
    # return 0 if input < 0 else input
    if input < 0:
        return 0
    else:
        return 1

def e(y,d):
    return y - d

# def update_weight(omomi,lc,e,x):
#     omomi =  float(omomi - lc * e * x)


# print(update_weight(1,2,3,4))
# y = step_func(input)


input_values = [[0,0,1],[0,1,1],[1,0,1],[1,1,1]]
weights = omomi()
lc = random.random()
expect_and_logic = [0,0,0,1]



for i in range(1000):
    for j in range(4):
        input_value = input(input_values[j],weights)
        y = step_func(input_value)
        e_value = e(y,expect_and_logic[j])

        for k in range(3):
            weights[k] -=  lc * e_value * input_values[j][k]




input = input(input_values[0],omomi())
print(step_func(input))

# input = input(input_values[1],omomi())
# print(step_func(input))
# input = input(input_values[2],omomi())
# print(step_func(input))
# input = input(input_values[3],omomi())
# print(step_func(input))

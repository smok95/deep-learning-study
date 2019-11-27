'''
    1. 1.0-perceptron.py와 동일하나 numpy를 사용하여 구현
    또한 편향을 도입하여 퍼셉트론 계산식을 약간 변경한다.

    입력신호(x1, x2) * 가중치(w1, w2)와 편향(bias)의 총합이 0을 넘으면 1을 출력하고 그렇지 않으면 0을 출력한다.

    2. XOR 게이트 구현
'''
import numpy as np

def perceptron(x1, x2, w1, w2, b):
    x = np.array([x1, x2])  # 입력
    w = np.array([w1, w2])  # 가중치
    ret = np.sum(x*w) + b
    if ret > 0:
        return 1
    else:
        return 0

# 퍼셉트론으로 AND게이트 구현
def AND(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.5)

# 퍼셉트론으로 NAND게이트 구현
def NAND(x1, x2):
    return perceptron(x1, x2, -0.5, -0.5, 0.6)

# 퍼셉트론으로 OR게이트 구현
def OR(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.4)

# 기존 게이트를 조합하여 XOR게이트 구현
def XOR(x1, x2):
    return AND(NAND(x1,x2), OR(x1,x2))



# 테스트
def gate_test(func):
    arr = [[0,0], [0,1], [1,0], [1,1]]
    print(func.__name__ + " gate ________________")
    for i in range(len(arr)):
        x1 = arr[i][0]
        x2 = arr[i][1]
        print('%d , %d = %d'%(x1, x2, func(x1,x2)))


def do_test():
    gate_test(AND)
    gate_test(NAND)
    gate_test(OR)
    gate_test(XOR)


do_test()
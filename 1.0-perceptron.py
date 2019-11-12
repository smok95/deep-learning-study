
'''
    퍼셉트론
    입력신호(x1, x2) * 가중치(w1, w2) 의 총합이 정해진 한계(theta 임계치)를 넘을 때만 1(뉴런 활성화), 넘지않으면 0을 출력한다.
'''
def perceptron(x1, x2, w1, w2, theta):
    ret = x1*w1 + x2*w2
    if ret <= theta:
        return 0
    elif ret > theta:
        return 1


# 퍼셉트론으로 AND게이트 구현
def AND(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, 0.6)

# 퍼셉트론으로 NAND게이트 구현
def NAND(x1, x2):
    return perceptron(x1, x2, -0.5, -0.5, -0.6)

# 퍼셉트론으로 OR게이트 구현
def OR(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, 0.4)


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


do_test()
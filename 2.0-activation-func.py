'''
    활성화 함수(activation function)
     입력 신호의 총합을 출력 신호로 변환하는 함수를 일반적으로 활성화 함수라 한다.
    
    계단 함수(step function)
    임계값을 경계로 출력이 바뀌는 함수
'''
import numpy as np
import matplotlib.pylab as plt
import platform


def step(x):
    """ 계단 함수 """
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    """ 시그모이드 함수 """
    return 1/(1+np.exp(-x))


def test(activation_func):
    x = np.arange(-5.0, 5.0, 0.1)
    y = activation_func(x)

    plt.clf()   # 이전 그래프 삭제
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y축의 범위

    if platform.system() == "Linux":
        # 리눅스일때 아래와 같은 문제로 이미지로 저장한다.
        # Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
        plt.savefig("2.0-activation-func." + activation_func.__name__ + ".png")
    else:
        plt.show()


test(step)
test(sigmoid)

'''
    활성화 함수(activation function)
     입력 신호의 총합을 출력 신호로 변환하는 함수를 일반적으로 활성화 함수라 한다.
    
    계단 함수(step function)
    임계값을 경계로 출력이 바뀌는 함수

    시그모이드 함수(sigmoid function)
    입력에 따라 출력이 연속적으로 변하며, 부드러운 곡선 헝태를 가진다.


    시그모이드와 계단 함수 비교

    차이점.
    계단 함수가 0과 1 중 하나의 값만 출력하는 반면
    시그모이드 함수는 실수(0.731..., 0.880... 등)를 출력한다.
    다시 말하면 퍼셉트론에서는 뉴런사이에 0 또는 1이 흘렀다면,
    신경망에서는 연속적인 실수가 흐른다.

    공통점.
    두 함수는 매끄러움이라는 점에서는 다르지만, 
    입력이 작을 때는 출력은 0에 가깝고
    입력이 커지면 출력이 1에 가까워진다.

    또한 비선형 함수로 1개의 직선으로는 그릴 수 없다는 공통점이 있다.

    ReLU(Rectified Linear Unit)
    입력이 0을 넘으면 그 입력을 그대로 출력, 0이하면 0을 출력하는 함수
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

def relu(x):
    """ ReLU 함수 """
    return np.maximum(0, x)


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
test(relu)

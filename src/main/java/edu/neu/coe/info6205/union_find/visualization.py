
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import leastsq

n = []
m = []


def load_data(filename):
    # read data from csv file
    f = open(filename)

    for line in f.readlines():
        line = line.strip().split()
        n.append(int(line[0]))
        m.append(float(line[1]))


def viz():
    # plot the n-m relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(n, m)
    plt.title("m-n relationship")
    plt.xlabel("n")
    plt.ylabel("m")
    plt.show()
    plt.pause(0)
    plt.ioff()


def cal_by_lse():
    def func(p, x):
        # guess the function format should be y = k * x + b via the graph
        k = p
        return k * x

    def error(p, x, y):
        return func(p, x) - y

    # calculate the expression via LSE(least squares method)
    xi = np.asarray(n)
    yi = np.asarray(m)

    p0 = np.asarray([5])   # guess the init value of k via the graph

    p = leastsq(error, p0, args=(xi, yi))
    k = p[0][0]

    return k


# Remove outliers
def cal_by_lse_2():
    def func(p, x):
        # guess the function format should be y = k * x + b via the graph
        k = p
        return k * x

    def error(p, x, y):
        return func(p, x) - y

    # calculate the expression via LSE(least squares method)
    xi = np.asarray(n)
    yi = np.asarray(m)

    for i, each in enumerate(yi[1:]):
        if each / yi[i - 1] > 1.1:
            # yi[i] = 0.5 * (yi[i - 1] + yi[i + 1])
            yi[i] = 0.8 * yi[i - 1] + 0.2 * yi[i]

    p0 = np.asarray([5])  # guess the init value of k via the graph

    p = leastsq(error, p0, args=(xi, yi))
    k = p[0][0]

    return k


def viz_with_line(k1, k2):
    # plot the distance-steps relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(n, m)

    x = range(0, 50001, 10000)
    y = k1 * x
    plt.plot(x, y, linewidth=2, label="original data")

    x = range(0, 50001, 10000)
    y = k2 * x
    plt.plot(x, y, linewidth=2, label="removed outliers", color="red")

    plt.title("m - n relationship")
    plt.xlabel("n")
    plt.ylabel("m")
    plt.legend()
    plt.show()
    plt.pause(0)
    plt.ioff()


# guess the function format should be y = k * x^2 via the graph
def cal_by_lse_3():
    def func(p, x):
        k = p
        return k * x * x

    def error(p, x, y):
        return func(p, x) - y

    # calculate the expression via LSE(least squares method)
    xi = np.asarray(n)
    yi = np.asarray(m)

    p0 = np.asarray([5])  # guess the init value of k via the graph

    p = leastsq(error, p0, args=(xi, yi))
    k = p[0][0]

    return k


# guess the function format should be y = k * x * log(x) via the graph
def cal_by_lse_4():
    def func(p, x):
        k = p
        return k * x * np.log(x)

    def error(p, x, y):
        return func(p, x) - y

    # calculate the expression via LSE(least squares method)
    xi = np.asarray(n)
    yi = np.asarray(m)

    p0 = np.asarray([5])  # guess the init value of k via the graph

    p = leastsq(error, p0, args=(xi, yi))
    k = p[0][0]

    return k


def viz_with_square_log(k1, k2):
    # plot the distance-steps relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(n, m)

    x = range(1, 50002, 10000)
    y = k1 * x * x
    plt.plot(x, y, linewidth=2, label="m = k1 * n^2")

    y = k2 * x * np.log(x)
    plt.plot(x, y, linewidth=2, label="m = k2 * n * log(n)", color="red")

    plt.title("m - n relationship")
    plt.xlabel("n")
    plt.ylabel("m")
    plt.legend()
    plt.show()
    plt.pause(0)
    plt.ioff()


# guess the function format should be y = k1 * pow(n, k2) via the graph
def cal_by_lse_5():
    def func(p, x):
        k, kk = p
        return k * np.power(x, kk)

    def error(p, x, y):
        return func(p, x) - y

    # calculate the expression via LSE(least squares method)
    xi = np.asarray(n)
    yi = np.asarray(m)

    p0 = np.asarray([0.005, 1.5])  # guess the init value of k via the graph

    p = leastsq(error, p0, args=(xi, yi))
    k, kk = p[0][0], p[0][1]

    return k, kk


def viz_with_power(k1, k2):
    # plot the distance-steps relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(n, m)

    x = range(1, 50002, 10000)
    y = k1 * np.power(x, k2)
    plt.plot(x, y, linewidth=2, label="m = k1 * pow(n, k2)")

    plt.title("m - n relationship")
    plt.xlabel("n")
    plt.ylabel("m")
    plt.legend()
    plt.show()
    plt.pause(0)
    plt.ioff()


if __name__ == '__main__':

    load_data("./result.csv")
    n = n[: 1000]
    m = m[: 1000]
    # viz()

    K1 = cal_by_lse()
    K2 = cal_by_lse_2()
    print("result expression: m =", K1, "* n")
    print("result expression: m =", K2, "* n")
    # viz_with_line(K1, K2)

    K3 = cal_by_lse_3()
    K4 = cal_by_lse_4()
    print("result expression: m =", K3, "* n ^", 2)
    print("result expression: m =", K4, "* n * log(n)")
    # viz_with_square_log(K3, K4)

    K5, K6 = cal_by_lse_5()
    print("result expression: m =", K5, "* pow(n,", K6, ")")
    viz_with_power(K5, K6)
    # K = cal_by_lse_2()



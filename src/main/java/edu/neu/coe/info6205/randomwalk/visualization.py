
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import leastsq

steps = []
distance = []


def load_data(filename):
    # read RandomWalk data from file
    f = open(filename)

    for line in f.readlines():
        line = line.strip().split()
        steps.append(int(line[0]))
        distance.append(float(line[1]))


def viz():
    # plot the distance-steps relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(steps, distance)
    plt.title("distance-steps relationship")
    plt.xlabel("steps")
    plt.ylabel("distance")
    plt.show()
    plt.pause(0)
    plt.ioff()


def cal_by_lse():
    def func(p, x):
        # guess the function format should be y = k * x + b via the graph
        k, b = p
        return k * x + b

    def error(p, x, y):
        return func(p, x) - y

    # calculate the expression via LSE(least squares method)
    xi = np.asarray(steps)
    yi = np.asarray(distance)
    p0 = np.asarray([1 / 25.0, 2.5])   # guess the init value of k via the graph

    p = leastsq(error, p0, args=(xi, yi))
    k, b = p[0][0], p[0][1]

    return k, b


def viz_with_line(k, b):
    # plot the distance-steps relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(steps, distance)

    x = range(1, 5002, 1000)
    y = k * x + b
    plt.plot(x, y)

    plt.title("distance-steps relationship")
    plt.xlabel("steps")
    plt.ylabel("distance")
    plt.show()
    plt.pause(0)
    plt.ioff()


def cal_by_lse_2():
    def func(p, x):
        # guess the function format should be y = k * sqrt(x) via the graph
        k = p
        return k * np.sqrt(x)

    def error(p, x, y):
        return func(p, x) - y

    # calculate the expression via LSE(least squares method)
    xi = np.asarray(steps)
    yi = np.asarray(distance)
    p0 = np.asarray([1 / 25.0])   # guess the init value of k via the graph

    p = leastsq(error, p0, args=(xi, yi))
    k = p[0][0]

    return k


def viz_with_line_2(k):
    # plot the distance-steps relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(steps, distance)

    x = range(1, 5002, 100)
    y = k * np.sqrt(x)
    plt.plot(x, y, linewidth=3)

    plt.title("distance-steps relationship")
    plt.xlabel("steps")
    plt.ylabel("distance")
    plt.show()
    plt.pause(0)
    plt.ioff()


if __name__ == '__main__':

    load_data("./result.csv")
    # viz()
    # K, b = cal_by_lse()
    # print("result expression: distance =", K, "* steps + ", b)

    K = cal_by_lse_2()
    print("result expression: distance =", K, "* sqrt(steps)")

    viz_with_line_2(K)

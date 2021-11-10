import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import leastsq

# n = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
all_n = []
all_times = []
n = []
times = []


def load_data(filename):
    # read data from csv file
    f = open(filename)

    for line in f.readlines()[2:-1]:
        line = line.strip().split()
        n.append(float(line[0]))
        times.append(float(line[1]))

    all_times.append(times)
    all_n.append(n)


def viz():
    # plot the n-m relationship
    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    for i, each in enumerate(all_times):
        plt.plot(all_n[i], each, label=str(pow(2, i)) + " threads")

    plt.legend()
    plt.title("time-cutoff relationship(Array size: 200w)")
    plt.xlabel("cutoff percent")
    plt.ylabel("time(ms)")
    plt.show()
    plt.pause(0)
    plt.ioff()


if __name__ == '__main__':
    f_name = "./result/result_"
    t_num = 1
    while t_num <= 1024:
        load_data(f_name + str(t_num) + "_200w.csv")
        times = []
        n = []
        t_num *= 2
    viz()

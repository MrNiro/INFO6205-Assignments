import matplotlib.pyplot as plt


def viz():
    n = [1000, 2000, 4000, 8000, 16000, 32000]

    t1 = [3.7804, 6.2933, 22.0400, 83.1732, 330.6761, 1537.1798]
    t2 = [0.0080, 0.0221, 0.0265, 0.0421, 0.0810, 0.1610]
    t3 = [0.1482, 0.4953, 2.1481, 7.8354, 34.9747, 138.1176]
    t4 = [2.5945, 11.2133, 40.5606, 164.3221, 643.3314, 2824.3726]

    plt.ion()
    plt.figure(figsize=(8, 8))  # 可视化
    plt.plot(n, t1, label="random")
    plt.plot(n, t2, label="ordered")
    plt.plot(n, t3, label="partially ordered")
    plt.plot(n, t4, label="inverse")
    plt.title("time-n relationship")
    plt.xlabel("n")
    plt.ylabel("time")
    plt.legend()
    plt.show()
    plt.pause(0)
    plt.ioff()


if __name__ == '__main__':
    viz()

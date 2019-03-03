import numpy as np
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import os

exec_times = []

with open("benchmark.txt", "r") as f:
    lines = f.readlines()

for idx, item in enumerate(lines):
    if (idx + 1) % 3 == 0:
        exec_times.append(round(float(item[16:24:]) * 10 ** 3, 3))

threads = []

for i in range(0, 7):
    threads.append(exec_times[i * 10 : i * 10 + 10])

means = []
std = []

for i in threads:
    means.append(round(np.mean(i), 3))
    std.append(round(np.std(i), 3))

pprint.pprint(threads)
pprint.pprint(means)
pprint.pprint(std)

if not os.path.exists("data.xlsx"):
    data = pd.DataFrame(np.transpose(threads))
    data.to_excel("data.xlsx")
if not os.path.exists("std.xlsx"):
    ms = pd.DataFrame([means, std])
    ms.to_excel("std.xlsx")

fig, ax = plt.subplots()
if not os.path.exists("bar.png"):
    ind = range(1, 8)
    plt.bar(ind, means)

    ax.set_xticklabels(["0", "1", "2", "4", "6", "8", "10", "12"])

    ax.set_xlabel("Number of threads")
    ax.set_ylabel("Execution time, ms")
    ax.set_title("Thread test")

    plt.savefig("bar.png")

if not os.path.exists("improvement.png"):
    ind = range(1, 7)
    improve = []
    for i in range(1, 7):
        improve.append(round((1 - means[i] / means[0]) * 100, 2))

    print(improve)

    plt.bar(ind, improve)

    ax.set_xticklabels(["0", "2", "4", "6", "8", "10", "12"])

    ax.set_xlabel("Number of threads")
    ax.set_ylabel("Improvement, %")
    ax.set_title("Improvement in comparison with one thread")

    plt.savefig("improvement.png")

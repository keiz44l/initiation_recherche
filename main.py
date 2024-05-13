import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np

def main():
    instances = []
    instance = {}
    # Read the data
    with open("./bbob-biobj_f01_d02_hyp.tdat", "r") as file:
        for line in file:
            if line[0] == "%" and instance:
                instances.append(instance)
                instance = {}
            if line[0] == "%":
                continue
            line = line.split()
            instance[int(line[0])] = float(line[1])
        instances.append(instance)

    #show_instances(instances)
    """
    instances = to_numpy(instances)
    my_median = median(instances)
    show_median(my_median)"""


def to_numpy(instances):
    # convert to numpy
    for i, instance in enumerate(instances):
        instances[i] = np.array(list(instance.items()))

    return instances

def median(instances):
    # Do the median
    median = {}
    for instance in instances:
        for x, y in instance:
            if x not in median:
                median[x] = []
            median[x].append(y)
    for x in median:
        median[x] = np.median(median[x])
    return median

def standardized(instances):
    # Ecart type
    std = {}
    for instance in instances:
        for x, y in instance:
            if x not in std:
                std[x] = []
            std[x].append(y)
    for x in std:
        std[x] = np.std(std[x])

    return std

def ecdf(instances):
    # ECDF
    sample = np.hstack(instances)
    ecdf = ECDF(sample[:, 1])
    return ecdf

def show_standardized(std):
    # Plot the standard deviation
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for Borg Adaptative algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(list(std.keys()), list(std.values()), label="Standard deviation")
    plt.show()

def show_instances(instances):
    # Plot the data
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for Borg Adaptative algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    for i, instance in enumerate(instances):
        ax.plot(list(instance.keys()), list(instance.values()), label=f"Instance {i+1}")
    ax.plot()
    ax.legend()
    plt.show()

def show_median(median):
    # Plot the medians
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for Borg Adaptative algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(list(median.keys()), list(median.values()), label="Median")
    plt.show()

def show_ecdf(ecdf):
    # Plot the ECDF
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for Borg Adaptative algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(ecdf.x, ecdf.y, label="ECDF")
    plt.show()

if __name__ == "__main__":
    main()
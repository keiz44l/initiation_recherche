import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np

def main():
    instances = []
    instance = {}
    # Read the data
    with open("./RM-MEDA_Auger_bbob-biobj/d02_d03_d10/1-separable_1-separable/bbob-biobj_f01_d02_hyp.tdat", "r") as file:
        for line in file:
            if line[0] == "%" and instance:
                instances.append(instance)
                instance = {}
            if line[0] == "%":
                continue
            line = line.split()
            instance[int(line[0])] = float(line[1])
        instances.append(instance)


    # Plot the data
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for RM-MEDA algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    for i, instance in enumerate(instances):
        ax.plot(list(instance.keys()), list(instance.values()), label=f"Instance {i+1}")
    ax.legend()
    plt.show()

    # convert to numpy
    for i, instance in enumerate(instances):
        instances[i] = np.array(list(instance.items()))

    # Do the median
    median = {}
    for instance in instances:
        for x, y in instance:
            if x not in median:
                median[x] = []
            median[x].append(y)
    for x in median:
        median[x] = np.median(median[x])

    # Ecart type
    std = {}
    for instance in instances:
        for x, y in instance:
            if x not in std:
                std[x] = []
            std[x].append(y)
    for x in std:
        std[x] = np.std(std[x])

    # ECDF
    sample = np.hstack(instances)
    ecdf = ECDF(sample[:, 1])


    # Plot the median
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for RM-MEDA algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(list(median.keys()), list(median.values()), label="Median")
    plt.show()

    # Plot the standard deviation
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for RM-MEDA algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(list(std.keys()), list(std.values()), label="Standard deviation")
    plt.show()

    # Plot the ECDF
    fig, ax = plt.subplots()
    ax.set_title("Quality based on number of evaluations for RM-MEDA algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(ecdf.x, ecdf.y, label="ECDF")
    plt.show()


if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
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
    ax.set_title("Quality based on number of evaluations for Borg Adaptative algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    for i, instance in enumerate(instances):
        ax.plot(list(instance.keys()), list(instance.values()), label=f"Instance {i+1}")
    ax.legend()
    plt.show()

    # Do the median
    median = {}
    for instance in instances:
        for key, value in instance.items():
            if key in median:
                median[key].append(value)
            else:
                median[key] = [value]
    for key, value in median.items():
        median[key] = np.median(value)

    # Plot the median
    fig, ax = plt.subplots()
    ax.set_title("Median quality based on number of evaluations for Borg Adaptative algorithm on separable functions")
    ax.set_xlabel("Number of evaluations")
    ax.set_ylabel("Quality")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(list(median.keys()), list(median.values()))
    plt.show()

    myList = instances[0].items()
    myList = sorted(myList)
    x, y = zip(*myList)

    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()
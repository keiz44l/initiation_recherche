import matplotlib.pyplot as plt

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
            instance[int(line[0])]=float(line[1])
        instances.append(instance) 
    print(instances)

    myList = instances[0].items()
    myList = sorted(myList)
    x, y = zip(*myList)

    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()
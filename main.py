import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    instances = []
    instance = {}
    # Read the data
    with open("bbob-biobj_f01_d02_hyp.tdat", "r") as file:
        for line in file:
            if line[0] == "%" and instance:
                instances.append(instance)
                instance = {}
            if line[0] == "%":
                continue
            line = line.split()
            print(line)



if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np

# RANDOMSEARCH5 instances : Génération des graphiques pour les instances de Borg ( Non utilisé dans le rapport )

instancesNbr = ["01","11","20","28","35","41","46","50","53","55"]
instancesType = ["sphere/sphere","ellipsoide separable/ellipsoide separable","attractive sector/attractive sector",
                 "rosenbrock original/rosenbrock original","sharp ridge/sharp ridge","sum of different powers/sum of different powers",
                 "rastrigin/rastrigin","schaffer F7 (condition 10)/schaffer F7 (condition 10)","schwefel x*sin(x)/schwefel x*sin(x)",
                 "gallagher 101 peaks/gallagher 101 peaks"]
instancesD = ["02","10","20"]
    
for k in range(len(instancesNbr)):
    for j in range(len(instancesD)):
        
        type = instancesType[k]
        name = "Random-Search5"
        picName = "rs5"
        dirName = "RANDOM-SEARCH5"
        
        instances = []
        instance = {}
        
        # Read the data
        with open(dirName+"/Data/bbob-biobj_f"+instancesNbr[k]+"_d"+instancesD[j]+"_hyp.tdat", "r") as file:
            for line in file:
                if line[0] == "%" and instance:
                    instances.append(instance)
                    instance = {}
                if line[0] == "%":
                    continue
                line = line.split()
                instance[int(line[0])] = float(line[1])
            instances.append(instance)
        
        """# Plot one instance
        fig, ax = plt.subplots()
        ax.set_title("Quality based on number of evaluations for " + name + " algorithm\n on " + type + " functions for a single instance")
        ax.set_xlabel("Number of evaluations (log scale)")
        ax.set_ylabel("Quality (log scale)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.plot(list(instances[0].keys()), list(instances[0].values()), label=f"Instance 1")
        ax.plot()
        ax.legend()
        plt.plot()"""
        
        # Plot the data
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 10)
        ax.set_title("Quality based on number of evaluations for " + name + " algorithm on " + type + " functions for all instances")
        ax.set_xlabel("Number of evaluations (log scale)")
        ax.set_ylabel("Quality (log scale)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        for i, instance in enumerate(instances):
            ax.plot(list(instance.keys()), list(instance.values()), label=f"Instance {i+1}")
        ax.plot()
        ax.legend(loc='lower left')
        plt.savefig(dirName+"/Instances/"+picName+"_f"+instancesNbr[k]+"_d"+instancesD[j]+"_instances.png")
        plt.close()
        
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
            
        # Plot the medians
        fig, ax = plt.subplots()
        ax.set_title("Median quality based on number of evaluations for " + name + " algorithm\n on " + type + " functions")
        ax.set_xlabel("Number of evaluations (log scale)")
        ax.set_ylabel("Quality (log scale)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.plot(list(median.keys()), list(median.values()), label="Median")
        plt.savefig(dirName+"/Median/"+picName+"_f"+instancesNbr[k]+"_d"+instancesD[j]+"_median.png")
        plt.close()
        
        # Ecart type
        std = {}
        for instance in instances:
            for x, y in instance:
                if x not in std:
                    std[x] = []
                std[x].append(y)
        for x in std:
            std[x] = np.std(std[x])
            
        """# Plot the standard deviation
        fig, ax = plt.subplots()
        ax.set_title("Standard deviation of quality based on number of evaluations\n for " + name + " algorithm on " + type + " functions")
        ax.set_xlabel("Number of evaluations (log scale)")
        ax.set_ylabel("Quality (log scale)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.plot(list(std.keys()), list(std.values()), label="Standard deviation")
        plt.show()"""
        
        # ECDF
        sample = np.hstack(instances)
        ecdf = ECDF(sample[:, 1])
        
        # Plot the ECDF
        fig, ax = plt.subplots()
        ax.set_title("Empirical Cumulative Distribution Function of quality based on number of evaluations\n for " + name + " algorithm on " + type + " functions")
        ax.set_xlabel("Number of evaluations (log scale)")
        ax.set_ylabel("Quality (log scale)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.plot(ecdf.x, ecdf.y, label="ECDF")
        plt.savefig(dirName+"/ECDF/"+picName+"_f"+instancesNbr[k]+"_d"+instancesD[j]+"_ecdf.png")
        plt.close()
        
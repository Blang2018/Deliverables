import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as inter
from scipy.interpolate import BSpline
import seaborn as sns
import itertools

samples_dir = "../data/annualTemps-out/samples"
rvar_name = "states"
num_samples = 1000
sequence_length = 4
initial_dist = [0.6, 0.4]

file = pd.read_csv(samples_dir+"/"+rvar_name+".csv")
vals = file['value'].values

vals = np.reshape(vals, (num_samples, sequence_length))
vals = vals.T

states = [(vals[0][j], vals[1][j], vals[2][j], vals[3][j]) for j in range(1000)]
combs = [(0,0,0,0), (0,0,0,1), (0,0,1,0), (0,0,1,1), (0,1,0,0), (0,1,0,1), (0,1,1,0), (0,1,1,1), (1,0,0,0), (1,0,0,1), (1,0,1,0), (1,0,1,1), (1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1)]

counts = np.ones(16)

for i in states:
    for j in range(16):
        if i == combs[j]:
            counts[j] += 1


labels = [str(combs[i]) for i in range(len(combs))]
probs = counts/len(states)
print(probs)


fig = plt.figure(figsize=(15,10))
bar = plt.bar(x=range(1,17), height=probs, align='center', color='orange', tick_label=labels)

plt.title("Distribution of State Sequences given Observation Sequence {S,M,S,L} \n 0: 'Hot Average Temp'  1: 'Cold Average Temp'")
plt.xlabel("State Sequences")
plt.ylabel("Probability of State Sequence")
plt.show()

fig.savefig("../figs/states_dist.pdf")


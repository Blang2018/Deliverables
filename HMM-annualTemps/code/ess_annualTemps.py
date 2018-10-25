import pandas as pd
import numpy as np

org_file = pd.read_csv("../data/annualTemps-out/samples/states.csv")

print(org_file.head())

sample_idx = org_file['sample']
vals_idx = org_file['value']
print(sample_idx.size)
curr = 0
for i in range(1000):
    sample_num = curr % 4
    seq = sample_idx == sample_num

final = np.ones((1000, 2))

for i in range(1000):
    final[i] = i
    final[i, 1] = np.sum(vals_idx[(i*4):(i*4)+4])

index = range(1000)
new_file = pd.DataFrame(data=final, columns=['sample', 'value'])

print(new_file)

new_file.to_csv("../data/annualTemps-out/samples/ess_states_data.csv", header=True)

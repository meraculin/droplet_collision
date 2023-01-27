import numpy as np
import itertools
from matplotlib import pyplot as plt

# Starting point of the fitted line
startPoint = int(266)
# Threshold for collision detection
ratio = float(0.98)

#Read roiNumbering.txt
with open('data/roiNumbering.txt', 'r') as file:
    x = []
    for line in file:
        values = line.strip().split('\t')
        x.append(int(values[0]))

# Read the LocalMinima.txt result
with open('data/localMinima.txt', 'r') as file:
    # initialize empty lists to store the data
    minima = []
    for line in file:
            values = line.strip().split('\t')
            minima.append(int(values[0])+startPoint)

# Read the x and localMinima to match the index
temp = []
for i in x:
    temp.append(minima[i])
minima = temp

# Read the result of analyze particle; aParticle.txt
with open('data/aParticle.txt', 'r') as file:
    # Read the first line (the header) and split it on the tab character
    header = file.readline().strip().split('\t')
    # initialize empty lists to store the data
    area = []
    # iterate over each line in the file
    for line in file:
        # split the line by the tab character
        values = line.strip().split('\t')
        # add the values to the appropriate list
        area.append(round(float(values[1])))

reference_area = float(area[0])
threshold = ratio * reference_area

nonCollision, collision = [], []
ndata = len(area)

for i in range(ndata):
    if area[i] >= threshold:
        nonCollision.append(minima[i])
    else:
        nonCollision.append('')

for i in range(ndata):
    if area[i] <= threshold:
        collision.append(minima[i])
    else:
        collision.append('')

# Saves the result into one single list
result = []
for i in range(0, ndata):
    result.append([])
    result[i].append(x[i])
    result[i].append(minima[i])
    result[i].append(nonCollision[i])
    result[i].append(collision[i])

# Saves the result into a .txt file
with open("data/Collision.txt", "w") as file:
    for row in result:
        file.write('\t'.join(map(str,row))+'\n')

print("Data saved to Collision.txt")
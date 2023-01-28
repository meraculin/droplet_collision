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
        nonCollision.append(i)
    else:
        nonCollision.append("")

for i in range(ndata):
    if area[i] <= threshold:
        collision.append(i)
    else:
        collision.append("")

def group_and_slice(data, threshold, percentage):
    """
    Group and slice the input data.
    
    Parameters:
    data (list): The input data to be processed
    threshold (int): The threshold value to group the data
    percentage (float): The percentage of each group to retain
    
    Returns:
    list: The processed data
    """
    groups = []
    current_group = [data[0]]
    for i in range(1, len(data)):
        if isinstance(data[i], int) and isinstance(data[i-1], int) and data[i] - data[i-1] <= threshold:
            current_group.append(data[i])
        else:
            groups.append(current_group)
            current_group = [data[i]]
    groups.append(current_group)
    
    new_data = []
    for group in groups:
        slice_count = int(percentage * len(group) / 100)
        new_data.extend(group[:slice_count])
        new_data.extend([''] * (len(group) - slice_count))
    return new_data

threshold, percentage = 30, 90
collision, nonCollision = group_and_slice(collision,threshold,percentage), group_and_slice(nonCollision,threshold,percentage)

# Saves the result into one single list
result = []
def saveCollision():
    for i in range(0, ndata):
        result.append([])
        result[i].append(x[i])
        result[i].append(minima[i])
        if nonCollision[i]!= '':
            result[i].append(minima[int(nonCollision[i])])
        else:
            result[i].append(nonCollision[i])
        if collision[i]!= '':
            result[i].append(minima[int(collision[i])])
        else:
            result[i].append(collision[i])

    # Saves the result into a .txt file
    with open("data/collisionResult.txt", "w") as file:
        for row in result:
            file.write('\t'.join(map(str,row))+'\n')

    print("Data saved to collisionResult.txt")

saveCollision()
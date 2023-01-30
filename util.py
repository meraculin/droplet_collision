def openFiles(startPoint,path):
    '''
    roi = 'data/roiNumbering.txt'
    minima = 'data/localMinima.txt'
    analyze_particle = 'data/aParticle.txt'
    '''
    roi = f'data/roi_numbering/{path}.txt'
    minima = f'data/localminima/{path}.txt'
    analyze_particle = f'data/analyze_particle/{path}.txt'
    #Read roiNumbering.txt
    with open(roi, 'r') as file:
        x = []
        for line in file:
            values = line.strip().split('\t')
            x.append(int(values[0]))

    # Read the LocalMinima.txt result
    with open(minima, 'r') as file:
        # initialize empty lists to store the data
        header = file.readline().strip().split('\t')
        minima = []
        for line in file:
                values = line.strip().split('\t')
                minima.append(int(values[0])+startPoint)
    # Read the x and localMinima to match the index
    temp = []
    for i in x:
        temp.append(minima[i-1])
    minima = temp

    # Read the result of analyze particle; aParticle.txt
    with open(analyze_particle, 'r') as file:
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
    return (x, minima, area)

def empty_list(length):
    return ['']*length

def match_data(data, source, destination):
    '''
    data = data_collision
    source = minima
    destination = collision
    '''
    for i in range(len(source)):
        if i in data:
            destination[i] = i

def saveCollision(x, minima, nonCollision, collision, initial, ndata, path):
    result = []
    for i in range(0, ndata):
        result.append([])
        result[i].append(x[i])
        result[i].append(minima[i])
        result[i].append(nonCollision[i])
        result[i].append(collision[i])
        if i <= len(initial):
            result[i].append(initial[i])
        else:
            result[i].append('')

    # Saves the result into a .txt file
    with open(f"data/collision_result/{path}.txt", "w") as file:
        for row in result:
            file.write('\t'.join(map(str,row))+'\n')

    print(f"Data saved to data/collision_result/{path}.txt")

def average(lst):
    return sum(lst)/len(lst)

def convert_data(data, source):    
    '''
    Converts the data comprised of index into the actual grey value.

    Parameters:
    data (list): The input data to be processed, usually 'collision'
    source (list): The reference data comprised of grey value

    Returns:
    temp(list): The converted list with grey value
    '''
    temp = []
    for item in data:
        if item != '':
            temp.append(source[item])
        else:
            temp.append('')
    return temp

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
        if abs(data[i] - current_group[-1]) <= threshold:
            current_group.append(data[i])
        else:
            groups.append(current_group)
            current_group = [data[i]]
    groups.append(current_group)

    new_data =[]
    for group in groups:
        slice_count = int(percentage * len(group) / 100)
        middle = int(len(group)/2)
        front_slice = middle - int(slice_count/2)
        back_slice = middle + int(slice_count/2)

        new_data.extend(group[front_slice:back_slice+1])
    
    return new_data        
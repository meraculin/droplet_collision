def openFiles(startPoint,roi, minima, analyze_particle):
    '''
    roi = 'data/roiNumbering.txt'
    minima = 'data/localMinima.txt'
    analyze_particle = 'data/aParticle.txt'
    '''

    #Read roiNumbering.txt
    with open(roi, 'r') as file:
        x = []
        for line in file:
            values = line.strip().split('\t')
            x.append(int(values[0]))

    # Read the LocalMinima.txt result
    with open(minima, 'r') as file:
        # initialize empty lists to store the data
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

def saveCollision(x, minima, nonCollision, collision, ndata, result):
    for i in range(0, ndata):
        result.append([])
        result[i].append(x[i])
        result[i].append(minima[i])
        result[i].append(nonCollision[i])
        result[i].append(collision[i])

    # Saves the result into a .txt file
    with open("data/collisionResult.txt", "w") as file:
        for row in result:
            file.write('\t'.join(map(str,row))+'\n')

    print("Data saved to collisionResult.txt")

def average(lst):
    return sum(lst)/len(lst)

def convert_data(data, source):    
    temp = []
    for item in data:
        temp.append(source[item])
    return temp
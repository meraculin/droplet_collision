import itertools
import numpy as np

from matplotlib import pyplot as plt
def get_local_minima(path):
    ''' Get local minima from the line plot result'''
    local_minima = f'data/lineplot/{path}.txt'
    with open(local_minima, 'r') as file:
        # Read the first line (the header) and split it on the tab character
        header = file.readline().strip().split('\t')
        # Create empty lists to store the x and y values
        x = []
        y = []
        nColumn = len(header)
        for i in range(nColumn):
            y.append([])
        # Iterate over the remaining lines in the file
        for row in file:
            # Split the line on the tab character and store the resulting values in the x and y lists
            values = row.strip().split('\t')
            x.append(float(values[0]))
            for i in range(0, nColumn):
                y[i].append(float(values[i+1]))
        result = []
        for i in range(nColumn):
            temp = FindMinima(x,y[i])
            a, b = temp
            result.append([a])

        with open(f"data/localminima/{path}.txt", "w") as f:
            for item in result:
                temp = "\t".join(map(str,list(itertools.chain(*item))))
                f.write(str(temp) + "\n")
        return x,y

def FindMinima(x,y):
    '''The function that actually finds the minima'''
    # Does a single calculation to find the local minima of the data
    y = np.array(y)
    nPeaks = len(x)
    middle = nPeaks//2

    # Find the minimum point at the left side
    minimum = []
    temp = 0
    for i in range(middle):
        if i == 0:
            temp = i
        elif y[i] < y[temp]:
            temp = i

    minimum.append(temp)

    #Find the maximum point at the right side
    maximum = []
    temp = middle
    for i in range(middle, nPeaks):
        if i == middle:
            temp = i
        elif y[i] > y[temp]:
            temp = i
    maximum.append(temp)

    return(minimum, maximum)

def PlotMinima (x,y):
    ''' Plot a single line plot result'''
    # Plot a single data
    result = FindMinima(y)
    y = np.array(y)
    minima = result
    print(minima)
    # Plotting the graph
    plt.plot(x,y)
    plt.plot(x[minima[0]],y[minima[0]], "o")
    plt.show()
    

def CheckPlot(y,i):
    '''Goes through PlotMinima'''
    PlotMinima(y[i-1])
    # Plot the graph so that its window only opens for 6 seconds
    plt.show()


def PlotEverything(nColumn):
    '''As the name says, plot everything!'''
    # Plot every available data entry
    for i in range(0,nColumn,1):
        CheckPlot(i)

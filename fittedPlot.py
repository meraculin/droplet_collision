import numpy as np
rectangle = input("Input rectangle equation: ")
# makeRectangle(266, 192, 139, 106);
# makeRectangle(x, y, width, height)
if rectangle[:5] == 'makeR':
    rectangle = rectangle.replace("makeRectangle","")
    rectangle = rectangle.replace(";","")
    rct = rectangle.strip("()").split(", ")
    rct = [int(x) for x in rct]
    width, height = rct[2], rct[3]

    # Write a code to remove "makeRectangle from this take": makeRectangle(266, 192, 139, 106)
    with open('data/aParticle.txt', 'r') as file:
        # Read the first line (the header) and split it on the tab character
        header = file.readline().strip().split('\t')
        # initialize empty lists to store the data
        x = []
        y = []
        # iterate over each line in the file
        for line in file:
            # split the line by the tab character
            values = line.strip().split('\t')
            # add the values to the appropriate list
            x.append(round(float(values[5])))
            y.append(round(float(values[6])))

    x = np.array(x)
    y = np.array(y)

    # calculate polynomial 
    z = np.polyfit(x, y, 1) 
    f = np.poly1d(z) 
    
    # calculate new x's and y's 
    x_new = np.linspace(x[0], x[-1], 50) 
    y_new = f(x_new)  

    b = round(z[0],2)
    a = round(z[1],2)

    # Equation of fitted line 
    print("Equation of fitted line: y=", b,"x +", a)

    # Parameters for makeLine
    x1 = float(rct[0])
    y1 =  x1*b + a
    x2 = x1 + width
    y2 = x2*b + a

    print(f'makeLine({x1},{y1},{x2},{y2});')
else:
    print("Wrong equation!")

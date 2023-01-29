def roiNumbering():
    with open('data/roiFile.txt', 'r') as file:
        header = file.readline().strip().split('\t')
        # initialize empty lists to store the data
        data = []
        # iterate over each line in the file
        for line in file:
            # split the line by the tab character
            values = line.strip().split('\t')
            temp = values[1]
            data.append(int(temp[:4]))
    
    with open("data/roiNumbering.txt", "w") as file:
        for item in data:
            file.write(str(item)+"\n")
    return(header)


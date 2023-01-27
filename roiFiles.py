import itertools

with open('data/roiFile.txt', 'r') as file:
    # initialize empty lists to store the data
    data = []
    # iterate over each line in the file
    for line in file:
        # split the line by the tab character
        temp = line[:4]
        data.append(int(temp))

with open("data/roiNumbering.txt", "w") as file:
    for item in data:
        file.write(str(item)+"\n")
print("--== RoiNumbering Finished ==--")
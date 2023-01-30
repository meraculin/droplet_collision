import util
import roiFiles
import localminima

path = str(input("Please enter file name: "))
roiFiles.roiNumbering(path)
localminima.get_local_minima(path)
# Initial values
startPoint = int(260)
x, minima, area = util.openFiles(startPoint, path)

# Threshold for collision detecti20230123_142810*  on
ratio = float(0.99)
reference_area = float(area[0])
area_threshold = ratio * reference_area
ndata = len(area)

# Threshold and percentage of slicing
threshold, percentage = 20, 60

data_nonCollision, data_collision = [], []

for i in range(ndata):
    if area[i] >= area_threshold:
        data_nonCollision.append(i)
    else: 
        data_collision.append(i)

# Data of index of NC and C without the space (''), grouped and sliced
data_collision = util.group_and_slice(data_collision,threshold,percentage)

# Creates data of NC and C with the space ('')
collision, nonCollision = util.empty_list(len(minima)), util.empty_list(len(minima))

# Matches the index of sliced NC and C with the space
util.match_data(data_collision,minima,collision)
util.match_data(data_nonCollision,minima,nonCollision)

# Save the result of calculation

initialState = []
for index in range(ndata):
    initialState.append(minima[index])
    avg = util.average(initialState)
    if minima[index] <= avg * 1.05 or  minima[index] >= avg * 0.95:
        continue
    else:
        break

# Convert all data into grey value
realdata_collision = util.convert_data(data_collision, minima)    
collision = util.convert_data(collision, minima)
nonCollision = util.convert_data(nonCollision, minima)

mean_collision = util.average(realdata_collision)
mean_initialstate = util.average(initialState)
deltaX = abs(mean_collision-mean_initialstate)

util.saveCollision(x, minima, nonCollision, collision, initialState, ndata, path)

print("Average collision:", mean_collision)
print("verage intial state: ",mean_initialstate,"\ndeltaX:",deltaX)
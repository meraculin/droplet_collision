import util
import roiFiles
roiFiles.roiNumbering()
# Initial values
startPoint = int(260)
x, minima, area = util.openFiles(startPoint, 'data/roiNumbering.txt','data/localMinima.txt','data/aParticle.txt')

# Threshold for collision detection
ratio = float(0.98)
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

data_nonCollision, data_collision = util.group_and_slice(data_nonCollision,threshold,percentage), util.group_and_slice(data_collision,threshold,percentage)

collision, nonCollision = util.empty_list(len(minima)), util.empty_list(len(minima))

util.match_data(data_collision,minima,collision)
util.match_data(data_nonCollision,minima,nonCollision)

# Save the result of calculation
result = []
util.saveCollision(x, minima, nonCollision, collision, ndata, result)

initialState = []
for index in range(ndata):
    initialState.append(minima[index])
    avg = util.average(initialState)
    if minima[index] <= avg * 1.1 or  minima[index] >= avg * 0.9:
        continue
    else:
        break

realdata_collision = util.convert_data(data_collision, minima)    
mean_collision = util.average(realdata_collision)
mean_initialstate = util.average(initialState)
deltaX = abs(mean_collision-mean_initialstate)
print("Average collision:", mean_collision,"\nAverage intial state: ",mean_initialstate,"\ndeltaX:",deltaX)

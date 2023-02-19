import re
import pyperclip
import util



path = str(pyperclip.paste())
print(f"Path copied from cliploard, {path}")

# The rectangle used to analyze the particle.
rectangle = 'makeRectangle(229, 186, 140, 115);'

# Get the line for collision by fitting a line from droplet center coordinates
util.fit_plot(path,rectangle)
status = str(input("Did you finish the fitted plot at ImageJ? (Y/N) "))
# Get the left boundary of droplet
util.get_local_minima(path)

# Get the frame numbering from analyze particle
util.roi_numbering(path)

# Initial values
temp = re.search(r'\d+',rectangle)
startLine = int(temp.group(0))

x, minima, center_x_coordinate = util.openFiles(startLine, path)
#Detect the initial state (in frame number) and then base that for the initial point of the wave function

fitted_minima = []
# Read the x and localMinima to match the index
for i in x:
    fitted_minima.append(minima[i-1])

# The period of the oscillation based on the stage movement


ndata = len(x)
# The threshold percentage to detect collision state
threshold = 1.

# The percentage change average of the 5 data adjacent to a data.
data_5_adj = util.average_5_adj(fitted_minima)

# Find the extreme change of that data depending on the set threshold, starting from 0.
start_point = util.find_extreme_change(data_5_adj,0, threshold, x)

wave_period = 360

initial_state = x[:start_point]
initial_state = util.convert_data(initial_state, minima)
mean_initialstate = util.average(initial_state)

data_collision = util.find_data_collision(data_5_adj, start_point, threshold, x)

check = True
if data_collision[0] == []:
    check = False
    print ("\nCollision is too short, deltaX cannot be detected! Trying lower threshold\n")
    threshold = threshold * 0.5
    data_collision = util.find_data_collision(data_collision, start_point, threshold, x)

if data_collision[0] != []:
    check = True

if check == True:
    while data_collision[-1] == []:
        data_collision.remove([])
    
    n_collision = len(data_collision)
    
    # Percentage of the data cut
    percentage = 75

    data_collision = util.slice_data(data_collision, percentage)
    collision = util.data_with_empty_list(data_collision, x)
    realdata_collision = util.convert_data(data_collision, minima)    
    collision = util.convert_data(collision, minima)
    
    mean_collision = util.average(realdata_collision)
    deltaX = mean_collision-mean_initialstate

    print(f"length of x, fitted_minima, collision, initial state= {len(x)}, {len(fitted_minima)}, {len(collision)}, {len(initial_state)}")
    util.save_for_graph(x, fitted_minima, collision, initial_state, ndata, path)
    radius_initial_state = []
    for i in range(len(initial_state)):
        radius_initial_state.append(center_x_coordinate[i]-initial_state[i])
    
    mean_radius_initial_state = util.average(radius_initial_state)

    # Checking if fusion happens
    fusion_check = False

    result = [path, fusion_check, n_collision, mean_radius_initial_state, mean_collision, mean_initialstate]
    util.save_data_to_excel(result)
else:
    print ("\nLower threshold does not work, delta X cannot be detected!\n")
    collision = util.data_with_empty_list(data_collision, fitted_minima)
    util.save_for_graph(x, fitted_minima, collision, initial_state, ndata, path)
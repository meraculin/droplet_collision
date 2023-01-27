import os

# Set the directory where the files are located
# Make sure to specify the correct path to the directory
directory = '/Volumes/LaCie/Data/20230123/'

# Check if the directory exists
if not os.path.isdir(directory):
  print('Error: the directory does not exist')
  exit()

# Get the list of files in the directory
files = os.listdir(directory)

# Iterate over the files and rename them
for i, file in enumerate(files):
    if file.endswith('.avi') and not file.startswith("."):
        os.rename(directory + file, directory + str(i+1) + '_' + file)

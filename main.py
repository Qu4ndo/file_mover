import os
import time
import json

# get time tick
tick = int(time.time())

# Check what is in the dir
# listdir need a variable path -> current = os.getcwd()
print("Output List:")
array = os.listdir(os.getcwd())
print(array)

# open checking file (json?)
# look for new files (for loop)
# if new file - move to second folder and get timestamp for new index (json file)
# remove all old files from directory (for loop)


#test dumping to json with timestamp
print("\nOutput List inkl. Timestamps:")

output = dict()

for item in array:
    output[item] = tick

print output


# test convert output to json
json_string = json.dumps(output)
print(json_string)

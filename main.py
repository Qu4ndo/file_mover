import os
import time
import json

"""
Things to do before use:
- edit remove_list
- edit home_directory
- edit directory
- edit min_time (seconds)

"""


#ignore following items (modify if needed)
remove_list = ['LICENSE', 'main.py', '.git', 'data.json', 'README.md', 'test']

#home directory
home_directory = "./"

#move directory
directory = "./test/"

# check what is in the dir
    # listdir need a directory path -> current = os.getcwd()
array = os.listdir(home_directory)
# ignore remove_list items
array = list(set(array).difference(set(remove_list)))
print("All Files in Directory:")
print(array)

# open data.json file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# scan if new files appeared
item_not_in_data = []

for item in array:
    if item not in data:
        item_not_in_data.append(item)
print("\nNew Files:")
print(item_not_in_data)
print("\n")


# move new files
for item in item_not_in_data:
    os.system("cp " + "\"" + home_directory + item + "\"" + " " + "\"" + directory + item + "\"")

# get time tick
tick = int(time.time())

# get minimum tick (604800 = 7 Days)
min_tick = tick - 604800

# remove old files (outdated)
converted_data = data
converted_data = converted_data.items()
for item in converted_data:
    if item[1] < min_tick:
        print("Remove - " + item[0])
        os.system("rm " + "\"" + home_directory + item[0] + "\"")

#adding timestamp to dict
output = dict()

for item in item_not_in_data:
    output[item] = tick

#add new files dictionary to output dictionary (json)
data.update(output)

# save new files to data.json
with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("\nJob finished! Ready for a new run?")

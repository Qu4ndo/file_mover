import os
import time
import json

#ignore following items (modify if needed)
remove_list = ['LICENSE', 'main.py', '.git', 'data.json', 'README.md']

# check what is in the dir
    # listdir need a directory path -> current = os.getcwd()
array = os.listdir(os.getcwd())
# ignore remove_list items
array = list(set(array).difference(set(remove_list)))
print("Files in Directory:")
print(array)

# open data.json file
with open('data.json') as json_file:
    data = json.load(json_file)

# scan if new files appeared
item_not_in_data = []

for item in array:
    if item not in data:
        item_not_in_data.append(item)
print("\nNew Files:")
print(item_not_in_data)


# move new files
# remove old files (outdated)


# get time tick
tick = int(time.time())

#adding timestamp to dict
output = dict()

for item in item_not_in_data:
    output[item] = tick

#add new files dictionary to output dictionary (json)
data.update(output)

# save new files to data.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("\nJob finished! Ready for a new run?")

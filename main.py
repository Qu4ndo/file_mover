import os
import time
import json

#ignore following items (modify if needed)
remove_list = ['LICENSE', 'main.py', '.git', 'data.json', 'README.md']

# get time tick
tick = int(time.time())

# check what is in the dir
    # listdir need a directory path -> current = os.getcwd()
print("Output List:")
array = os.listdir(os.getcwd())
# ignore remove_list items
array = list(set(array).difference(set(remove_list)))
print(array)


# open data.json file
with open('data.json') as json_file:
    data = json.load(json_file)

    # scan if new files appeared
    print("\nData opened from json file")
    for items in data:
        print(items)


# move new files
# remove old files (outdated)

#adding timestamp to dict
print("\nOutput List inkl. Timestamps:")

output = dict()

for item in array:
    output[item] = tick

print(output)

"""
#maybe not needed
# test convert output to json
json_string = json.dumps(output)
print(json_string)
"""


# save new files to data.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
print("\nData dumped to json file")

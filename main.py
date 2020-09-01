import os

# Check what is in the dir
# listdir need a variable path -> current = os.getcwd()
arr = os.listdir(os.getcwd())
print(arr)

for ar in arr:
    print(ar)

# open checking file (json?)
# look for new files (for loop)
# if new file - move to second folder and get timestamp for new index (json file)
# remove all old files from directory (for loop)


#test dumping to json with timestamp

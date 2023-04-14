import os
count = len(os.listdir("dataset"))

while(count!=0):
    os.remove(os.listdir("dataset")[count - 1])
    count = len(os.listdir("dataset"))
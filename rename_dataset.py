import os

dataset_list = os.listdir("dataset")
count = len(dataset_list)

for i in range(len(dataset_list)):
    source = "dataset/"+dataset_list[i]
    destination = "dataset/"+str(i+count)+".jpg"
    if(destination not in dataset_list):
        os.rename(source, destination)

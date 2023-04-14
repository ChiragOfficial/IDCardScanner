import os

# dataset_list = os.listdir("dataset")
# count = len(dataset_list)

# for i in range(len(dataset_list)):
#     source = "dataset/"+dataset_list[i]
#     destination = "dataset/"+str(i+count)+".jpg"
#     if(destination not in dataset_list):
#         os.rename(source, destination)

dataset_path = "/Dataset_annotated"
for i in range(0, 223):
    previous_img_path = (str)i+".xml"+".txt"
    new_img_path = (str)i+".txt"
    os.rename(previous_img_path, new_img_path)
import shutil
import os

from_dir="C:\\Users\\satis\\Downloads"
to_dir="F:\\game\\Python\\class activity\\class 102"

list_of_file=os.listdir(from_dir)
#print(list_of_file)

for i in list_of_file:
    root,ext=os.path.splitext(i)
    #print(root)
    #print(ext)
    if(ext==""):
        continue
    if(ext in [".gif",".png",".jfif",".jpeg",".jpg"]):
        path1=from_dir+"/"+ i
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+ i

        if(os.path.exists(path2)):
            print("Moving"+i)
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving"+i)
            shutil.move(path1,path3)
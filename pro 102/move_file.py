import os 
import shutil
from dir="c:\Users\prade\Downloads"
to dir="c:\Users\prade\OneDrive\Desktop\document_files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    if extention=='':
        continue
    if extention in ['.gif','.png','.jpg']:
        path1=from_directory+'/'+file_name
        path2=to_dir+'/'+"image_files"+'/'+file_name
        if os.path.exists(path2):
            print("moving"+file_name+".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+".....")
            shutil.move (path1,path3)
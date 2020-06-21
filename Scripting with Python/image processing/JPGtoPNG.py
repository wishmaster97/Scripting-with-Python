import sys
import os
from PIL import Image

#take first and second argument
arg1 = sys.argv[1]
arg2 = sys.argv[2]

#see if the second arg - file is present or not, if not then create it


destination_directory = arg2

path = os.path.join("./", destination_directory)
try: 
    os.makedirs(path, exist_ok = True) 
    print("Directory '%s' created successfully" % destination_directory) 
except OSError as error: 
    print("Directory '%s' can not be created (May already exist)" % destination_directory) 



#see if the first argument folder is present or not, if not then return false stmt
source_directory = arg1

path2 = os.path.join("./", source_directory)
try:
    if os.path.isdir(path2):
    #loop through pokedox, #convert JPG into PNG, #save all the images in second arg folder
        for filename in os.listdir(path2):
            if filename.endswith(".jpg"): 
                #print(os.path.join(path2, filename))
                print(f'Trying to convert file - {filename}')
                file_path = os.path.join(path2, filename)
                convert_img = Image.open(file_path)
                new_destination = "./"+destination_directory+"/"+filename[:-4]+".png"
                print("*****Saving to New Destination*****")
                convert_img.save(new_destination, "png")

            else:
                continue

except OSError as error:
    print(error)




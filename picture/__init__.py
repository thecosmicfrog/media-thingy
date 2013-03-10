import os
from models import Picture
from MediaThingy.settings import MEDIA_ROOT

image_list = []

def add_to_db(image_files):
    for image_file in image_files:
        image_name = image_file.rsplit('/', 1)[1] # Get filename
        
        if not Picture.objects.filter(name=image_name).exists():
            pic1 = Picture(name=image_name, url=image_file)
            pic1.save()
            
            print 'Added to DB: ' + image_name

def process_file(curr_dir):
    curr_dir = os.path.abspath(curr_dir)
 
    # Get a list of files in curr_dir
    curr_dir_files = os.listdir(curr_dir)
 
    # Traverse through all files
    for curr_dir_file in curr_dir_files:
        curr_file = os.path.join(curr_dir, curr_dir_file)
 
        # If file is not a directory, get its extension.
        if os.path.isfile(curr_file):
            file_ext = os.path.splitext(curr_file)[1]
 
            # If file is a compatible image file, print its name.
            if file_ext in ['.jpg']:
                image_list.append(curr_file)
        else: # File is directory. Recursively run function.
            process_file(curr_file)
    
    return image_list

add_to_db(process_file(MEDIA_ROOT + 'pictures/'))

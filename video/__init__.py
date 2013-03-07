import os
from models import Video
from MediaThingy.settings import MEDIA_ROOT

video_list = []

def add_to_db(video_files):
    for video_file in video_files:
        
        video_title = video_file.rsplit('/', 1)[1] # Get filename
        
        if not Video.objects.filter(title=video_title).exists():
            vid1 = Video(title=video_title, url=video_file)
            vid1.save()
    
            print 'Added to DB: ' + video_title

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
 
            # If file is a compatible video file, print its name.
            if file_ext in ['.mp4']:
                video_list.append(curr_file)
        # File is directory. Recursively run function.
        else:
            process_file(curr_file)
    
    return video_list

add_to_db(process_file(MEDIA_ROOT + 'videos/'))

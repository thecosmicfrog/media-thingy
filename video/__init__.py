import os
from models import Video
from MediaThingy.settings import MEDIA_ROOT, MEDIA_URL

video_list = []

def add_to_db(video_files):
    for video_file in video_files:
        video_filename = video_file.rsplit('/', 1)[1] # Get filename
        
        if not Video.objects.filter(filename=video_filename).exists():
            vid1 = Video(title=os.path.splitext(video_filename)[0], \
                         filename=video_filename, \
                         fspath=video_file, \
                         media_url=MEDIA_URL + video_file.split(MEDIA_ROOT)[1])
            vid1.save()
    
            print 'Added to DB: ' + video_filename

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
        else: # File is directory. Recursively run function.
            process_file(curr_file)
    
    return video_list

add_to_db(process_file(MEDIA_ROOT + 'videos/'))

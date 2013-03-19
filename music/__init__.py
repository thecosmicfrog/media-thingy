import eyed3
import os
from models import Album, Artist, Track
from MediaThingy.settings import MEDIA_ROOT, MEDIA_URL, SITE_ROOT

audio_list = []

def add_to_db(audio_files):
    for audio_file in audio_files:
        audio_file_id3 = eyed3.load(audio_file)
        
        try:
            if not Artist.objects.filter(name=audio_file_id3.tag.artist).exists():
                ar1 = Artist(name=audio_file_id3.tag.artist)
                ar1.save()
        
            if not Album.objects.filter(title=audio_file_id3.tag.album).exists():
                al1 = Album(title=audio_file_id3.tag.album, artist=ar1)
                al1.save()
            
            if not Track.objects.filter(title=audio_file_id3.tag.title).exists():
                t1 = Track(title=audio_file_id3.tag.title, \
                           album=al1, \
                           artist=ar1, \
                           fspath=audio_file, \
                           media_url=MEDIA_URL + audio_file.split(MEDIA_ROOT)[1])
                t1.save()
                print 'Added to DB: ' + audio_file_id3.tag.title
        except Exception as e:
            print e

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
 
            # If file is a compatible audio file, print its name.
            if file_ext in ['.mp3']:
                audio_list.append(curr_file)
        else: # File is directory. Recursively run function.
            process_file(curr_file)
    
    return audio_list

os.system('bash ' + SITE_ROOT + '/../setup_media.sh') # Clear down and sync DB
add_to_db(process_file(MEDIA_ROOT + 'music/'))

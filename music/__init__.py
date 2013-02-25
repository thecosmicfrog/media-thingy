import eyed3
from MediaThingy.settings import STATIC_ROOT

audiofile = eyed3.load(STATIC_ROOT + 'music/Weezer/The Blue Album/My Name Is Jonas.mp3')

print audiofile.tag.title
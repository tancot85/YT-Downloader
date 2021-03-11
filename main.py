import pafy 
import pprint

URL = input('enter the video url: ')

video = pafy.new(URL)

print(video.title)

pprint.pprint(video.allstreams)
import pafy 
import pprint

URL = input('enter the video url: ')

video = pafy.new(URL)
all_streams = video.allstreams
# print(video.title)
# pprint.pprint(video.allstreams)
 
def get_stream(video):
    for i in all_streams:
        print(all_streams.index(i), ". ", i)
    option = int(input('enter the index of the quality you want: '))

    return all_streams[option]

def download_stream(video):
    get_stream_video = get_stream(video)
    downloading_video_index = all_streams.index(get_stream_video) 
    print('video name: ',video.title,' by: ',video.author)
    print('size: ',video.allstreams[downloading_video_index].get_filesize()/1000000 , 'mb')
    video.allstreams[downloading_video_index].download()

# download_stream(video)

download_stream(video)
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
import ijson
import os

home_directory = os.path.expanduser( '~' )

print("Hello There!  What would you like to watch/download?")
search = input ("Enter your search term: ")

if search == "exit":
    print("Goodbye!")
    exit()

videosSearch = VideosSearch(search, limit = 21)

source = videosSearch.result()

#iterate through source and print the title and id of each video
count = 0

videoID = [0]

for item in source['result']: 
    print(count, ": ", item['title'], " by " , item['channel']['name'])
    video = item['id']
    if videoID == [0]:
        videoID[0] = video
    else:
        videoID.append(video)

    count += 1


con = 0

DownloadID = [0]

while True: 
    prompt = input("Enter the number of the video you want to download: (type \"exit\" to quit.) ")
    if prompt == "exit":
        break
    
    try:
        convert = int(prompt)
    except ValueError:
        print("That's not an number! Please Try Again!")
        continue
    
    if convert == int(convert):
        if convert > count:
            print(convert, "is out of range or invalid number.  Please try again.")
            continue
        elif convert < 0:
            print(convert, "should be a positive number.  Please try again.")
            continue
        if DownloadID == [0]:
            DownloadID[0] = convert
        else:
            DownloadID.append(convert)
        break
        

    if prompt != int(prompt):
        print("That is not a number.  Please try again. :(")
        continue

if prompt == "exit":
    print("Goodbye!")
    exit()

def download(DownloadID):
    length = len(DownloadID)
    if length > 0:
        for ytvid in DownloadID:
            con = ytvid
            vid = videoID[con]
            videostr = str(vid)
            print("Downloaded: ", videostr)
            # ydl.download(videostr)
            downloadTo = home_directory+'\Videos\\'

            ydl_opts = {
                'format': 'best',
                'outtmpl': downloadTo+'%(title)s'+'.mp4',
                'noplaylist': True,
                'extract-audio': True,
            }
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(videostr, download=True)
                video_url = info_dict.get("url", None)
                video_title = info_dict.get('title', None)
                video_length = info_dict.get('duration')
    else:
        print("Goodbye!")
        exit()

download(DownloadID)




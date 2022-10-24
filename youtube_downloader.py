from pytube import YouTube
from sys import argv

"Enter the path to the folder where you wish the video to be downloaded to"
download_path = ''

link = input("Enter video link: \n")
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"Views: {yt.views}")
print(f"Published: {yt.publish_date}")

yd = yt.streams.get_highest_resolution()
yd.download(download_path)

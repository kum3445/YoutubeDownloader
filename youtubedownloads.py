from tkinter import *
from pytube import YouTube
url= input("Enter the Youtube Video Link Here\n")
youtube=YouTube(url)
video=youtube.streams.get_by_itag(22)
video.download('D:/Youtube_videos')
print("your video is downloaded")
#https://www.youtube.com/watch?v=ZihywtixUYo

#https://www.youtube.com/watch?v=Bg8Yb9zGYyA
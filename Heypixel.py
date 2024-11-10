import os,requests,webbrowser
from tkinter.ttk import *
def download_file(url, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url, stream=True)
    response.raise_for_status() 
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return True
def HeypixelSongPart1():
    # P1 Song:https://livefile.xesimg.com/programme/python_assets/857843aa118affb0b48b4ca5c970f7ba.mp3
    # P1 Video:https://www.bilibili.com/video/BV1AbYceUE35/
    download_file("https://livefile.xesimg.com/programme/python_assets/857843aa118affb0b48b4ca5c970f7ba.mp3",r"C:\HeypixelSongPart1.mp3")
    os.startfile(r"C:\HeypixelSongPart1.mp3")
    webbrowser.open("https://www.bilibili.com/video/BV1AbYceUE35/")
    # pass
def HeypixelSongPart2():
    # P2 Song:https://livefile.xesimg.com/programme/python_assets/5ea2a8aac4608b56d019ad6b2c04f605.mp3
    # P2 Video:https://www.bilibili.com/video/BV17uYTedE3Q/
    download_file("https://livefile.xesimg.com/programme/python_assets/5ea2a8aac4608b56d019ad6b2c04f605.mp3",r"C:\HeypixelSongPart2.mp3")
    os.startfile(r"C:\HeypixelSongPart2.mp3")
    webbrowser.open("https://www.bilibili.com/video/BV17uYTedE3Q/")
def HeypixelSongPart3():
    # P3 Song:https://livefile.xesimg.com/programme/python_assets/17699308303ec801f9d956cbfdae782c.mp3
    # P3 Video:https://www.bilibili.com/video/BV1eMYxeuE2f/
    download_file("https://livefile.xesimg.com/programme/python_assets/17699308303ec801f9d956cbfdae782c.mp3",r"C:\HeypixelSongPart3.mp3")
    os.startfile(r"C:\HeypixelSongPart3.mp3")
    webbrowser.open("https://www.bilibili.com/video/BV1eMYxeuE2f/")
# HeypixelSongPart1()
# HeypixelSongPart2()
# HeypixelSongPart3()
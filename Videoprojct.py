from pytube import YouTube
from tkinter import *
root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("Rabia's Video Downloader")
Label(root,text = 'Video Downloader for YouTube', font ='arial 20 bold').pack()
link = StringVar()
path = StringVar()
Label(root, text = 'Paste Link Here', font = 'algerian 15 bold').place(x= 150 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
Label(root, text = 'Paste Path Here', font = 'algerian 15 bold').place(x= 150 , y = 130)
path_enter = Entry(root, width = 70,textvariable = path).place(x = 32, y = 160)
def Downloader():     
    url = YouTube(str(link.get()))
    url.streams.get_highest_resolution().download('D:\youtube')
    Label(root, text = 'DOWNLOADED to D:\youtube', font = 'algerian 15').place(x= 150 , y = 230)  
Button(root,text = 'DOWNLOAD', font = 'algerian 15 bold' ,bg = 'skyblue', padx = 2, command = Downloader).place(x=210 ,y = 190)
root.mainloop()
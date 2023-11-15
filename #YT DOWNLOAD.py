#YT DONWLOAD test

from pytube import YouTube
from ctypes.wintypes import FLOAT
from tkinter import *
from tkinter.messagebox import *
import os


# window 
window = Tk()
window.title('YouTube Vidéos Downloader')
window.geometry('430x100')
window.attributes('-topmost', 1) #app toujours au dessus des autres pages
#window.resizable(False, False)



def Download():
    url = link.get()
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    yd = yt.streams.get_highest_resolution()

    # Create Downloads folder if it doesn't already exist
    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")

    # Download video to Downloads folder
    yd.download(os.path.join(os.getcwd(), "Downloads"))


# frame
frame = Frame(window)

# field options
options = {'padx': 5, 'pady': 5}

# URL label
download_label = Label(frame, text='URL de la vidéo YouTube :')
download_label.grid(column=0, row=0, sticky='W', **options)

# URL entry
link = StringVar()
link_entry = Entry(frame, textvariable=link)
link_entry.grid(column=1, row=0, **options)
link_entry.focus()




# Buttons
download_button = Button(frame, text='Download', fg='green')
download_button.grid(column=2, row=0, sticky='W', **options)
download_button.configure(command=Download)

exit_button = Button(frame, text='Exit',  fg='red', command=lambda: frame.quit())
exit_button.grid(column=3, row=1, sticky='W', **options)


# result label
result_label = Label(frame)
result_label.grid(row=1, columnspan=3, **options)


# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# Start the app
window.mainloop()
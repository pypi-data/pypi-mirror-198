import tkinter
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import Image, ImageTk
import threading
import os
import time
import pygame
import pygame.mixer as mixer
class MusicBar(Frame):
    def __init__(self, parent=None, bg="white", fg="black", width=200, height=20, **kwargs):
        Frame.__init__(self, parent, bg=bg, width=width, height=height, **kwargs)
        self.configure(highlightthickness=1, highlightbackground="gray")
        self.track_length = width
        self.progress_bar = Canvas(self, width=0, height=height, bg=fg, highlightthickness=0)
        self.progress_bar.pack(side=LEFT)
        self.pack_propagate(False)
    def update_progress(self, progress):
        progress_width = int(progress * self.track_length)
        self.progress_bar.configure(width=progress_width)

root = Tk()
root.title('Music Player')
root.geometry("400x500")

pygame.mixer.init()

menubar= Menu(root)
root.config(menu=menubar)


songs= []
current_song = ''
paused = False

def load_music():
    global  current_song
    songs.clear()
    songList.delete(0, END)
    try:
        root.directory = filedialog.askdirectory()
        for song in os.listdir(root.directory):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                songs.append(song)

        for song in songs:
            songList.insert("end",song)

        songList.select_set(0)
        current_song = songs[songList.curselection()[0]]
    except IndexError:
        messagebox.showinfo("Alert", "Thu muc nay khong co bai hat")

def cal_songLength(length):
    duration_minutes = length / 60
    total_seconds = int(duration_minutes * 60)
    minutes, seconds = divmod(total_seconds, 60)
    time_label_end.config(text=f"{minutes}:{seconds:02d}")

def play_music():
    global current_song, paused, song_length

    try:
        if not paused:
            pygame.mixer.music.load(os.path.join(root.directory, current_song))
            song_length = pygame.mixer.Sound(os.path.join(root.directory, current_song)).get_length()
            cal_songLength(song_length)
            pygame.mixer.music.play()

            # Create a new thread to update the progress bar

            play_btn.grid_forget()
            pause_btn.grid(row=0, column=1, padx=7, pady=10)
        else:
            play_btn.grid_forget()
            pause_btn.grid(row=0, column=1, padx=7, pady=10)
            pygame.mixer.music.unpause()
            paused = False
        progress_thread = threading.Thread(target=update_progress)
        progress_thread.start()
    except (AttributeError, IndexError):
        messagebox.showinfo("Alert", "Chon thu muc co chua bai hat")
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused =TRUE

    pause_btn.grid_forget()
    play_btn.grid(row=0, column=1, padx=7, pady=10)

def next_music():
    global current_song,paused
    try:
        songList.select_clear(0,END)
        songList.select_set(songs.index(current_song) + 1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except:
        pass
def prev_music():
    global current_song, paused
    try :
        songList.select_clear(0, END)
        songList.select_set(songs.index(current_song) - 1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except :
        pass
def on_select(event):
    global current_song,paused
    selection = songList.curselection()

    if selection :
        if paused :
            paused=FALSE
            current_song = songs[selection[0]]
            play_music()
        else:
            current_song = songs[selection[0]]
            play_music()
    else :
        print("Nothing is selected")

def update_progress():
    # Get the total length of the music in milliseconds
    total_length = song_length * 1000

    # Update the music progress bar while music is playing
    while pygame.mixer.music.get_busy():
        # Get the current position of the music in milliseconds
        current_position = pygame.mixer.music.get_pos()
        current_time = time.strftime("%M:%S", time.gmtime(current_position // 1000))
        # Calculate the progress of the music as a percentage
        progress_percent = current_position / total_length

        # Update the value of the music progress bar
        music_bar.update_progress(progress_percent)
        time_label_start.config(text=current_time)

        # Wait for a short period of time before updating again
        pygame.time.delay(1000)


organise_menu = Menu(menubar,tearoff = False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise',menu=organise_menu)


songList=Listbox(root,bg='black',fg='white',width=100,height=15)
songList.pack()
songList.bind("<<ListboxSelect>>", on_select)

play_btn_image = PhotoImage(file='img/play-button-circled.png')
pause_btn_image = PhotoImage(file='img/circled-pause.png')
next_btn_image = PhotoImage(file='img/end.png')

image = Image.open('img/end.png')
overturned_img= image.transpose(method=Image.FLIP_LEFT_RIGHT)
previous_btn_image=ImageTk.PhotoImage(overturned_img)


control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame,image=play_btn_image,borderwidth=0,command=play_music)
pause_btn = Button(control_frame,image=pause_btn_image,borderwidth=0,command=pause_music)
next_btn = Button(control_frame,image=next_btn_image,borderwidth=0,command=next_music)
prev_btn = Button(control_frame,image=previous_btn_image,borderwidth=0,command=prev_music)

play_btn.grid(row=0,column=1,padx=7,pady=10)
next_btn.grid(row=0,column=3,padx=7,pady=10)
prev_btn.grid(row=0,column=0,padx=7,pady=10)

musicbar_frame = Frame(root)
musicbar_frame.pack()

music_bar = MusicBar(musicbar_frame, bg="white", fg="blue", width=300, height=10)
music_bar.update_progress(0.01)

time_label_start = tkinter.Label(musicbar_frame, text="0:00")
time_label_end = tkinter.Label(musicbar_frame, text="0:00")

music_bar.grid(row=0,column=1,padx=7,pady=10)
time_label_start.grid(row=0,column=0,padx=7,pady=10)
time_label_end.grid(row=0,column=2,padx=7,pady=10)

root.mainloop()
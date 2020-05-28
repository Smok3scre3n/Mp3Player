"""
My program is an Mp3 player that allows you to play ,unpause,exit and change songs
"""

"""
Importing Modules
"""
import pygame
import tkinter as tkr
import os


def main():
    """
Creating Window
"""


Player = tkr.Tk()

"""
Edit Window
"""
Player.title("Lisa's Audio Player")
Player.geometry("250x450")

"""
Playlist Register
"""
os.chdir(r"C:\Users\Smok3scre3n\Documents\Code in Place Stanford\FinalProject\Playlist")
print(os.getcwd)
Song_list = os.listdir

"""
Volume Input
"""
Volume_level = tkr.Scale(Player, from_=0.0, to_=1.0, orient=tkr.HORIZONTAL, resolution=0)

"""
Playlist Input
"""
Playlist = tkr.Listbox(Player, highlightcolor="blue", selectmode=tkr.SINGLE)
print(Song_list)
for item in Song_list():
    Position = 0
    Playlist.insert(Position, item)
    Position = Position + 1

"""
Pygame initializer
"""
pygame.init()
pygame.mixer.init()

"""
Action Event
"""


def Play():
    pygame.mixer.music.load(Playlist.get(tkr.ACTIVE))
    var.set(Playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(Volume_level.get())
    print(pygame.mixer.music.get_volume())
    print(Volume_level.get())


def ExitPlayer():
    pygame.mixer.music.stop()


def Pause():
    pygame.mixer.music.pause()


def Unpause():
    pygame.mixer.music.unpause()


def Rewind():
    pygame.mixer.music.rewind()


"""
Register Buttons
"""
Button_1 = tkr.Button(Player, width=5, height=3, text="PLAY", command=Play)
Button_2 = tkr.Button(Player, width=5, height=3, text="STOP", command=ExitPlayer)
Button_3 = tkr.Button(Player, width=5, height=3, text="PAUSE", command=Pause)
Button_4 = tkr.Button(Player, width=5, height=3, text="UNPAUSE", command=Unpause)
Button_5 = tkr.Button(Player, width=5, height=3, text="REWIND", command=Rewind)

"""
Song Name
"""
var = tkr.StringVar()
Song_title = tkr.Label(Player, textvariable=var)

"""
Place Widgets
"""
Button_1.pack(fill="x")
Button_2.pack(fill="x")
Button_3.pack(fill="x")
Button_4.pack(fill="x")
Button_5.pack(fill="x")
Volume_level.pack(fill="x")
Song_title.pack()
Playlist.pack(fill="both", expand=True)

"""
Activate
"""
Player.mainloop()

if __name__ == '__main__':
    main()

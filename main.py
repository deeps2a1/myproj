import pygame as PG
import GridModule as GM
import GameModules as GMS
import random as RD
from copy import copy, deepcopy

# Declare Variables
PG.init()
x = 2
y = 2
perc = 0.6
xmax = 500
ymax = 500
box_size = 48
vRed = (255,0,0)
vtime = 0
vGreen = (46,204,113)
vGrey = (180,180,180)
mouse = [[0,0], 0, 0, 0, 0, 0, 0]
screen = PG.display.set_mode((ymax,xmax))
icon = PG.image.load('icon.png')
play = PG.image.load('Play.png')
playbutton = PG.image.load('PlayButton.png')
Box = PG.image.load('Box.png')
BoxFilled = PG.image.load('BoxFilled.png')

# Title and Icon
PG.display.set_caption("MINDOTS")
PG.display.set_icon(icon)

# Game Loop
running = True
playagain = True
PlayLevel = True

# Start Page
while running:
    screen.fill((255,255,255))
    for event in PG.event.get():
        if event.type == PG.QUIT:
            running = False
            playagain = False
            PlayLevel = False
        elif event.type == PG.MOUSEBUTTONDOWN:
            mouse = GMS.setMouse(PG,event)
            if mouse[1] == 1 and mouse[0][0] >= 200 and mouse[0][0] <= 300 and mouse[0][1] >= 220 and mouse[0][1] <= 300:
                running = False
    GMS.Display_Text(PG,"Mind-Dots",30,vGreen,190,130,screen)
    GMS.Display_Text(PG,"- By Deepak Rawat",12,vRed,220,160,screen)
    # PG.draw.rect(screen,vGrey,(200,220,100,80))
    GM.Show_Box(playbutton,200,210,screen)
    PG.display.update()

running = True

while PlayLevel:
    
    Grid_Cordinates = []
    Grid_List = []
    Grid_Cordinates = GM.SetGrid_Cord(x,y,xmax,ymax,box_size,Grid_Cordinates)
    Grid_List = GM.SetGrid_List(x,y,Grid_List)
    Grid_Final = deepcopy(Grid_List)
    Grid_Final = GM.SetGrid_Final(Grid_Final,x,y,perc,RD)
    print(Grid_Final)
    starttime = PG.time.get_ticks()
    while running:    
        screen.fill((255,255,255))
        vtime += PG.time.get_ticks() - starttime
        starttime = PG.time.get_ticks()
        GMS.Display_Text(PG,"Time :",30,vGreen,10,10,screen)
        GMS.Display_Text(PG,str(vtime/1000),30,vGreen,90,10,screen)
        for event in PG.event.get():
            if event.type == PG.QUIT:
                running = False
                playagain = False
                PlayLevel = False
            elif event.type == PG.MOUSEBUTTONDOWN:
                mouse = GMS.setMouse(PG,event)
                if mouse[1] == 1:
                    Grid_List = GM.UpdateGrid_List(Grid_Cordinates,Grid_List,mouse)
        # GMS.Display_Text(PG,"2",40,vRed,5,10,screen)
        GMS.DisplayNumbers(PG,Grid_Final,Grid_List,Grid_Cordinates,x,y,screen,vRed,vGreen)
        GM.Show_Grid(Grid_Cordinates,Box,screen)
        GM.Show_Grid_Filled(BoxFilled,Grid_Cordinates,Grid_List,screen)
        PG.display.update()
        # Check if Won
        if GM.CheckWon(x,y,Grid_Final,Grid_List) == True:
            print("You Won!")
            running = False

    # Show You Won Message
    
    while playagain:
        screen.fill((255,255,255))
        PG.draw.rect(screen,vGrey,(125,205,235,75))
        GMS.Display_Text(PG,"You Won!",40,vGreen,190,160,screen)
        GM.Show_Box(play,130,210,screen)
        GMS.Display_Text(PG,"Next Level",30,vRed,210,222,screen)
        for event in PG.event.get():
            if event.type == PG.QUIT:
                playagain = False
                PlayLevel = False
            elif event.type == PG.MOUSEBUTTONDOWN:
                mouse = GMS.setMouse(PG,event)
                if mouse[1] == 1 and mouse[0][0] >= 125 and mouse[0][0] <= (125+235) and mouse[0][1] >= 205 and mouse[0][1] <= (205+75):
                    running = True
                    PlayLevel = True
                    playagain = False
                    x += 1
                    y += 1
        PG.display.update()
    playagain = True
    

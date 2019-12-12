
# Set Mouse
def setMouse(pygame,event):
    mouse = [[0,0], 0, 0, 0, 0, 0, 0]
    chkButton = pygame.mouse.get_pressed()
    mouse[0] = event.pos
    mouse[1] = chkButton[0]
    mouse[2] = chkButton[1]
    mouse[3] = chkButton[2]
    return mouse

def Display_Text(pygame,msg,size,color,x,y,screen):
    sys_font = pygame.font.SysFont("Arial",size)
    screen.blit(sys_font.render(msg,0,color),(x,y))

def DisplayNumbers(Pygame,FinalGrid,GridList,GridCord,x,y,screen,vred,vgreen):
# Displaying X cordinates numbers
    for i in range(x):
        posx = GridCord[0][i][0] + 18
        posy = GridCord[0][0][1] - 35
        countf = 0
        counti = 0
        for j in range(y):
            countf = countf + FinalGrid[j][i]
            counti = counti + GridList[j][i]
        if countf == counti:
            vcol = vgreen
        else:
            vcol = vred
        Display_Text(Pygame,str(countf),30,vcol,posx,posy,screen)
    
    # Displaying Y cordinates numbers
    for j in range(y):
        posx = GridCord[0][0][0] - 35
        posy = GridCord[j][0][1] + 10
        countf = sum(FinalGrid[j])
        counti = sum(GridList[j])
        if countf == counti:
            vcol = vgreen
        else:
            vcol = vred
        Display_Text(Pygame,str(countf),30,vcol,posx,posy,screen)
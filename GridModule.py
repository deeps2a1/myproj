# showbox function
def Show_Box(Img,x,y,screen):
    screen.blit(Img,(x,y))

# Display Grid
def Show_Grid(Grid_Cord,Box,screen):
    for i in Grid_Cord:
        for j in i:
            Show_Box(Box,j[0],j[1],screen)

# Display Grid Filled
def Show_Grid_Filled(BoxFilled,Grid_Cord,Grid_List,screen):
    for i in range(len(Grid_Cord)):
        for j in range(len(Grid_Cord[i])):
            if Grid_List[i][j] == 1 :
                Show_Box(BoxFilled,Grid_Cord[i][j][0],Grid_Cord[i][j][1],screen)

# Set Grid Cordinates
def SetGrid_Cord(x,y,xmax,ymax,box_size,Grid_Cordinates):
    initx = (xmax-(x*box_size))/2
    inity = (ymax-(y*box_size))/2
    for i in range(y):
        Blank_List=[]
        Grid_Cordinates.append(Blank_List)
        # print(Grid_Cordinates)
        for j in range(x):
            Grid_Cordinates[i].append([0,0,0,0])
            Grid_Cordinates[i][j][0] = initx + (j * box_size)
            Grid_Cordinates[i][j][1] = inity + (i * box_size)
            Grid_Cordinates[i][j][2] = Grid_Cordinates[i][j][0]+box_size
            Grid_Cordinates[i][j][3] = Grid_Cordinates[i][j][1]+box_size
            # print(Grid_Cordinates)
    return Grid_Cordinates

# Set Grid list
def SetGrid_List(x,y,Grid_List):
    for i in range(y):
        Blank_List=[]
        Grid_List.append(Blank_List)
        # print(Grid_List)
        for j in range(x):
            j = j*1
            Grid_List[i].append(0)
            # print(Grid_List)
    return Grid_List

# Update Grid
def UpdateGrid_List(Grid_Cord,Grid_List,mouse):
    for i in range(len(Grid_Cord)):
        for j in range(len(Grid_Cord[i])):
            if mouse[0][0] >= Grid_Cord[i][j][0] and mouse[0][0] < Grid_Cord[i][j][2] and mouse[0][1] >= Grid_Cord[i][j][1] and mouse[0][1] < Grid_Cord[i][j][3]:
                if Grid_List[i][j] == 0:
                    Grid_List[i][j] = 1
                else:
                    Grid_List[i][j] = 0
    return Grid_List

# Set Grid Final
def SetGrid_Final(Grid_Final,x,y,perc,RD):
    DotNumbers = int(x * y * perc)
    for i in range(DotNumbers):
        i *= 1
        BlankNotFound = True
        while BlankNotFound:
            rnum = RD.randint(1,x*y) - 1
            posx = (rnum % x)
            posy = int(rnum / x)
            if Grid_Final[posy][posx] == 0:
                Grid_Final[posy][posx] = 1
                BlankNotFound = False
    return Grid_Final

# Check if Won
def CheckWon(x,y,gridfinal,gridlist):
    won = True
    # check by row
    for i in range(y):
        if(sum(gridfinal[i]) != sum(gridlist[i])):
            won = False
            break

    for i in range(x):
        countf = 0
        counti = 0
        for j in range(y):
            countf += gridfinal[j][i]
            counti += gridlist[j][i]
        if countf != counti:
            won = False
            break
        
    return won
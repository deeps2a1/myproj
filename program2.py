# def SetGrid_Final(Grid_List,x,y,perc,RD):
#     Grid_Final = Grid_List
#     DotNumbers = int(x * y * perc)
#     print(DotNumbers)

#     for i in range(DotNumbers):
#         BlankNotFound = True
#         while BlankNotFound:
#             rnum = RD.randint(1,x*y) - 1
#             posx = (rnum % 4)
#             posy = int(rnum / 4)
#             if Grid_Final[posy][posx] == 0:
#                 Grid_Final[posy][posx] = 1
#                 BlankNotFound = False
#     return Grid_Final

list1 = [0,1,2,0]
print(sum(list1))


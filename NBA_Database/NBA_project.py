import xlrd # Read from excel 
from xlrd import open_workbook

import xlwt
from xlwt import Workbook
from xlutils.copy import copy

def printTeam(x):
    for i in range(x.nrows):
        for j in range(x.ncols):
            print(sheet.cell_value(i,j), end=" | ")
        print()

def EditPlayer(x):
    playerEdit = int(input("Choose a player to edit (Enter rank): "))
    statEdit = input("What stat would you like to edit? ")
    statEdit = statEdit.upper() #convert string to caps for ease of finding stat
    if (statEdit == "TRB"):
        sEdit = 2
    elif (statEdit == "AST"):
        sEdit = 3
    elif (statEdit == "STL"):
        sEdit = 4
    elif (statEdit == "BLK"):
        sEdit = 5
    elif (statEdit == "TOV"):
        sEdit = 6
    elif (statEdit == "PTS/G"):
        sEdit = 7
    else:
        print("Error. Not a valid stat.")
        return

    nEdit = float(input("Enter new stat: ")) 
    x.write(playerEdit,sEdit, nEdit)

def removePlayer(x, r):
    remove = int(input("Choose a player to remove (Enter rank): "))
    if (remove == r):
        for i in range(8):
            x.write(remove,i,"")
    else:
        for i in range(8):
            

def showMenu():
    print("\nWhat would you like to do? \n1. Add Player \n2. Edit Player \n3. Remove Player \n4. Back To Main Menu")
    
#location of file
loc = "C:\\Users\\micha\\OneDrive\\Desktop\\Central.xls"

rb = xlrd.open_workbook(loc) # open excel file

wb = copy(rb) # make writable copy of excel file

# read the sheet to write to within the writable copy
sheet = wb.get_sheet(0) # For central 0 = Bucks, 1 = Bulls, 2 = Cavs, 3 = Pacers, 4 = Pistons

#print information
print("Milwaukee Bucks Player Stats")
# printTeam(rb)


showMenu()
c = int(input("Select an option: "))

if (c == 2):
    EditPlayer(sheet)
    wb.save(loc)
elif (c == 3):
    numRows = rb.nrows
    removePlayer(sheet, numRows)
    wb.save(loc)


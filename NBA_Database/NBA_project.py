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

#location of file
loc = "C:\\Users\\micha\\OneDrive\\Desktop\\Central.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0) # For central 0 = Bucks, 1 = Bulls, 2 = Cavs, 3 = Pacers, 4 = Pistons

#print information
print("Milwaukee Bucks Player Stats")
printTeam(sheet)

print("\nWhat would you like to do? \n1. Add Player \n2. Edit Player \n3. Remove Player \n4. Back To Main Menu")
c = input("Select an option: ")

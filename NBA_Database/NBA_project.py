import xlrd # Read from excel 
from xlrd import open_workbook

import xlwt
from xlwt import Workbook
from xlutils.copy import copy

#location of file
loc = "C:\\Users\\micha\\OneDrive\\Desktop\\Detroit.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0,0)


#print information
print("Detroit Pistons Player Stats")
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell_value(i,j), end=" | ")
    print()

print("\nWhat would you like to do? \n1. Add Player \n2. Edit Player \n3. Remove Player \n4. Back To Main Menu")
c = input("Select an option: ")
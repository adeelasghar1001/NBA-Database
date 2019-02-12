import os
import xlrd

def printTeam(team, loc):
    workbook = xlrd.open_workbook(loc)
    sheet = workbook.sheet_by_index(0)

    #print(sheet.cell_value(0,0))

    print('\n')
    print(team + " 2017-2018 Team")
    print('----------------------------------------------')
    print("What would you like to do?")
    print('1. Add player')
    print('2. Edit player')
    print('3. Remove player')
    print('4. Back to main menu')
    option = int(input('Select a option(number):'))
    
  

    return


while True:

    print('NBA Database Application: 2017-2018 Season')
    print('----------------------------------------------')
    team = str(input('Enter a team name: '))

    if team == 'Pistons':
        loc='C:\\Users\\Adeel Asghar\\Desktop\\Book1.xlsx'
        printTeam(team, loc)

    elif team == 'Bucks':
        loc='C:\\Users\\Adeel Asghar\\Desktop\\pistons.xlsx'
        printTeam(team, loc)
      

    elif team == 'Bulls':
        loc='C:\\Users\\Adeel Asghar\\Desktop\\pistons.xlsx'
        printTeam(team, loc)

    elif team == 'Pacers':
        loc='C:\\Users\\Adeel Asghar\\Desktop\\pistons.xlsx'
        printTeam(team, loc)

    elif team == 'Cavaliers':
        loc='C:\\Users\\Adeel Asghar\\Desktop\\pistons.xlsx' 
        printTeam(team, loc)

    else:
        print('Please enter valid team name!')





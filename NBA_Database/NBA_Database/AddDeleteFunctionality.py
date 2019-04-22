
# for display
import pandas as pd
df = pd.read_excel("C:\\Users\\basha\\Desktop\\Python\\northwest.xlsx", sheet_name = "Denver")
print("Welcome to the Denver Nuggest roster!")
print("")
print(df)
print("")

menu = str(input("Press A to add, or D to delete | Press q to exit | : "))
rk = 10

#Delete Functionality
if (menu == 'D'):
   

    while menu != 'q':
        choose = str(input("Please enter a Rank Number to select player with corresponding rank | Press q to exit | : ")) #player name
        if(choose != 'q'):
            if(choose == '0'):
                   df = df.drop([0])
                   print("Jamal Murray has been deleted!")
                   print(df)

            if(choose == '1'):
                   df = df.drop([1])
                   print("Nikola Jokic has been Deleted!")
                   print(df)

            if(choose == '2'):
                   df = df.drop([2])
                   print("Gary Harris has been Deleted!")
                   print(df)

            if(choose == '3'):
                   df = df.drop([3])
                   print("Will Barton has been Deleted!")
                   print(df)

            if(choose == '4'):
                   df = df.drop([4])
                   print("Paul Millsap has been Deleted!")
                   print(df)

            if(choose == '5'):
                   df = df.drop([5])
                   print("Monte Morris has been Deleted!")
                   print(df)

            if(choose == '6'):
                   df = df.drop([6])
                   print("Malik Beasley has been Deleted!")
                   print(df)

            if(choose == '7'):
                   df = df.drop([7])
                   print("Mason Plumlee has been Deleted!")
                   print(df)

            if(choose == '8'):
                   df = df.drop([8])
                   print("Torrey Craig has been Deleted!")
                   print(df)

            if(choose == '9'):
                   df = df.drop([9])
                   print("Juan Hernangomez has been Deleted!")
                   print(df)

        if(choose == 'q'):
                print("GoodBye!")
                break

#Add functionality
if (menu == 'A'):
    
    while menu != 'q': 
        choose1 = str(input("Press y to add player | Press q to exit | : ")) #player name
        if(choose1 != 'q'):
            if(choose1 == 'y'):         
                i1 = str(input("Enter player name: "))
                i2 = float(input("What is their TRB: "))
                i3 = float(input("What is their AST: "))
                i4 = float(input("What is their STL: "))
                i5 = float(input("What is their BLK: "))
                i6 = float(input("What is their TOV: "))
                i7 = float(input("What is their PTS/G: "))
                df.loc[rk] = [rk, i1, i2, i3, i4, i5, i6, i7]
                rk = rk + 1
                print("New Player Added!")
                print(df)
        if(choose1 == 'q'):
           print("GoodBye!")
           
       
    
        
   

# for display
import pandas as pd
df = pd.read_excel("C:\\Users\\basha\\Desktop\\Python\\northwest.xlsx", sheet_name = "Denver")
print("Welcome to the Denver Nuggest roster!")
print("")
print(df)
print("")

#print(df.to_dict())


#if statements to select player
    #nested if statements to select what to edit
    #break


menu = str(input("Press anything to continue | Press q to exit | : "))



while menu != 'q':
    choose = str(input("Please enter a Rank Number to select player with corresponding rank | Press e to exit | : ")) #player name
    if(choose != 'q'):
        ch1 = str(input("Edit player or Delete player (Type e-(edit) or d-(delete): ")) #Edit or Delete

        if(choose == '0'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([0])
               print("Jamal Murray has been deleted!")
               print(df)
        if(choose == '1'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([1])
              # df = df[df.Name != 'Jamal Murry']
               print("Nikola Jokic has been Deleted!")
               print(df)
        if(choose == '2'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([2])
              # df = df[df.Name != 'Jamal Murry']
               print("Gary Harris has been Deleted!")
               print(df)

        if(choose == '3'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([3])
              # df = df[df.Name != 'Jamal Murry']
               print("Will Barton has been Deleted!")
               print(df)

        if(choose == '4'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([4])
              # df = df[df.Name != 'Jamal Murry']
               print("Paul Millsap has been Deleted!")
               print(df)

        if(choose == '5'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([5])
              # df = df[df.Name != 'Jamal Murry']
               print("Monte Morris has been Deleted!")
               print(df)

        if(choose == '6'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([6])
              # df = df[df.Name != 'Jamal Murry']
               print("Malik Beasley has been Deleted!")
               print(df)

        if(choose == '7'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([7])
              # df = df[df.Name != 'Jamal Murry']
               print("Mason Plumlee has been Deleted!")
               print(df)

        if(choose == '8'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([8])
              # df = df[df.Name != 'Jamal Murry']
               print("Torrey Craig has been Deleted!")
               print(df)

        if(choose == '9'):
            if (ch1 == "e"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="d"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([9])
              # df = df[df.Name != 'Jamal Murry']
               print("Juan Hernangomez has been Deleted!")
               print(df)



    if(choose == 'q'):
            print("GoodBye!")
            break
        
        
        
   
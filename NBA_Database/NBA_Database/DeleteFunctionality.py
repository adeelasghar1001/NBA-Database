
# for display
import pandas as pd
df = pd.read_excel("C:\\Users\\basha\\Desktop\\Python\\northwest.xlsx",sheet_name = "Denver")
print(df)

#print(df.to_dict())


#if statements to select player
    #nested if statements to select what to edit
    #break

print("Welcome to the Denver Nuggest roster!")
menu = str(input("Press anything to continue | Press e to exit | : "))



while menu != 'e':
    choose = str(input("Please enter a player name (Type Exact) | Press e to exit | : ")) #player name
    if(choose != 'e'):
        ch1 = str(input("Edit player or Delete player (Type edit or delete): ")) #Edit or Delete

        if(choose == 'Jamal Murray'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([0])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)
        if(choose == 'Nikola Jokic'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([1])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)
        if(choose == 'Gary Harris'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([2])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)

        if(choose == 'Will Barton'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([3])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)

        if(choose == 'Paul Millsap'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([4])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)

        if(choose == 'Monte Morris'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([5])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)

        if(choose == 'Malik Beasley'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([6])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)

        if(choose == 'Mason Plumlee'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([7])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)

        if(choose == 'Torrey Craig'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([8])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)

        if(choose == 'Juan Hernangomez'):
            if (ch1 == "edit"):
                print("Select a Category: points, rebounds, assists")
            if(ch1=="delete"):
                #add delete row logic
                #as well as save sheet
               df = df.drop([9])
              # df = df[df.Name != 'Jamal Murry']
               print(choose, " has been Deleted!")
               print(df)



    if(choose == 'e'):
            print("GoodBye!")
            break
        
        
        
   
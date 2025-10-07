###############################################################################
#  Program Name   : dynamicmenus.py
#  Author         : Rithvik Kandula
#  Task           : Create a Python program that allows a user to create their own list 
#                   (of names, fruits, countries, etc.), view that list as a numbered menu, and then interact with the list by:
#                   Selecting an item from the menu to display.
#                   Adding a new item to the list.
#                   Exiting the program.
###############################################################################

items = input("Enter indexes and items in the following format:\n'index 1': 'item 1', 'index 2': 'item 2', etc\n-> ")
split_items = items.split(",") #seperating between commas

iandi = []
for i in split_items: #removing additoinal spaces
    iandi.append(i.strip())

mydic = {}
for i in iandi: #seperating between semicolons
    mydic[i.split(":")[0].strip()] = i.split(":")[1].strip()


""" OLD WAY OF GATHERING ITEMS
#Asking for the inital items in the list
mydic = {input("Enter the index for the first item: "): input("Enter the first item: "), 
        input("Enter the index for the second item: "): input("Enter the second item: "), 
        input("Enter the index for the third item: "): input("Enter the third item: "), 
        input("Enter the index for the fourth item: "): input("Enter the fourth item: ")}
"""

print("\n", "-"*30, "\n")
while True:
    #printing the list
    for i in mydic:
        print(i, ":", mydic[i])
    
    choice = input("If you want to add an item, type 'A'\nIf you want to access an item from your dictionary, type the correspondign index \nIf you want to end the program, type '0'\n -> ")
    if choice == "A": #If users selects A to add a new index and item
        index = "A"
        item = "A"

        while index == "A" or index == "0": #Making sure the index is not A or 0
            index = input("Enter the new index(cannot be A or 0): ").strip()
        
        item = input("Enter the new item: ")
        mydic[index] = item.strip()
        print("\nItem added!\n", "-"*30)

    elif choice == "0": #If user selects 0 to end the program
        print("\n", "-"*30, "\nThank you, Goodbye!")
        break

    else: #If user wants to access an item
        inlist = False
        for n in mydic: #checking if the item that the user wants to access is in the list
            if n == choice:
                print("\n", "-"*30, "\nYour item is:", mydic[choice])
                inlist = True
        if not inlist: #If item is not in the list
            print("\n", "-"*30,"\nItem not in list")

    input("Continue:\n" + "-"*30)
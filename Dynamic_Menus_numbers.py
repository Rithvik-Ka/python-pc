###############################################################################
#  Program Name   : dynamicmenus.py
#  Author         : Rithvik Kandula
#  Task           : Create a Python program that allows a user to create their own list 
#                   (of names, fruits, countries, etc.), view that list as a numbered menu, and then interact with the list by:
#                   Selecting an item from the menu to display.
#                   Adding a new item to the list.
#                   Exiting the program.
###############################################################################
def is_num(s):
      try:
        int(s)  # or float(s) for decimals
        return True
      except ValueError:
        return False

valid_input = False
while not valid_input:
    items = input("Enter indexes and items in the following format:\n'index 1': 'number 1', 'index 2': 'number 2', etc\n-> ")
    split_items = items.split(",") #seperating between commas

    iandi = []
    for i in split_items: #removing additoinal spaces
        iandi.append(i.strip())

    valid_input = True
    mydic = {}
    for i in iandi: #seperating between semicolons
        mydic[i.split(":")[0].strip()] = i.split(":")[1].strip()
        if not is_num(i.split(":")[1].strip()):
            print("Your item nubmer is not a number!\n" + "-"*30 + "\n")
            valid_input = False
        if i.split(":")[0].strip() == 'A' or i.split(":")[0].strip() == '0' or i.split(":")[0].strip() == 'N':
            print("Your index cannot be A, 0, or N!\n" + "-"*30 + "\n")
            valid_input = False



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
    added_item = ""
    for i in mydic:
        print(i, ":", mydic[i])
        added_item += i + " : "+ mydic[i]+ "\n"
    
    choice = input("If you want to add an item, type 'N'\nIf you want to increase ro decrease one of the amounts, type 'A'\nIf you want to access an item from your dictionary, type the correspondign index \nIf you want to end the program, type '0'\n -> ")
    if choice == "N": #If users selects N to add a new index and item
        index = "N"
        while index == "N" or index == "0": #Making sure the index is not N or 0
            index = input("Enter the new index(cannot be N, A, 0): ").strip()
        
        item = "h"
        while not is_num(item):
            item = input("Enter the new number: ")
            mydic[index] = item.strip()
        print("\nItem added!\n", "-"*30)

    elif choice == "A":
        index_chan = input("What is the index you want to change?: ")
        num_chan = "h"
        while not is_num(num_chan):
            num_chan = input("How much do you want to add (5) or subtract (-5)")
        mydic[index_chan] = str(int(mydic[index_chan]) + int(num_chan))

    elif choice == "0": #If user selects 0 to end the program
        print("\n", "-"*30, "\nThank you, Goodbye!")
        with open("menu_output.txt", "w", encoding="utf-8") as f:
            f.write(added_item)
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
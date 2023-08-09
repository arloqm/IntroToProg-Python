# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Arlo Magpoc,August 7, 2023, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strTask = "" # A new task
strPriority = "" # Assigns task priority
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

try:
    objFile = open("ToDoList.txt", "r") # Opens and reads the data contained in text file
    for row in objFile: # For loop to go through the rows of data
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        print(dicRow["Task":] + "-|-" + dicRow["Priority"])
        lstTable.append(dicRow)
        print(lstTable)
        objFile.close()
except:
    print("File not found, will make a new one when you save it")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user

while (True):
    print(""" 
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):

        print("Your task/tasks so far is/are: ")
        print("*************************************")
        for row in lstTable: # For loop through the list table
            print(row["Task"] + "-|-" + row["Priority"]) # Displays Task and Priority to user
            print(row)
            print("*************************************")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        print("Enter a specific Task and its Priority to your To-Do List")
        strTask = input("Enter your task please: ") # Asks user to put in a new Task
        strPriority = input("What is the priority of this task?: ") # Asks user to put a priority on entered Task
        dicRow= {"Task":strTask, "Priority":strPriority} # The row of data
        lstTable.append (dicRow)
        print(lstTable) # Prints current progress of list
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):

        strData = input("Remove an existing Task: ") # Prompts user to remove a Task
        for row in lstTable: # For loop that loops through each dictionary in list
            if row["Task"].lower() == strData.lower():
                lstTable.remove(row) # Removes the row from table
                print (strData, "has been removed")
            else:
                print (strData, "was not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):

        while (True):
            strChoice = input("Would you like to save? ('y/n'): ") # Asks user to save data
            if (strChoice.lower() == "y"):
                objFile = open("ToDoList.txt", "w")  # Opens and writes into text file
                for row in lstTable:
                    objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")  # Saves Data
                objFile.close()
                print("Your file was saved!") # Lets user know the file was saved
                break
            elif (strChoice.lower() == "n"):
                print("Your file was not saved.") # Lets user know file was not saved
                break
            else:
                print("Please choose only 'y' or 'n'")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):

        strChoice = input ("Would you like to exit? ('y' or 'n'): ") # Prompts user to make a choice to exit or not
        if (strChoice.lower() == 'y'):
            break # Exits out of the program
        elif (strChoice.lower() == 'n'):
            continue # Keeps the program running
    else:
        print ("Choose only options '1, 2, 3, 4, or 5'") # Lets user know to choose only these numbers for options

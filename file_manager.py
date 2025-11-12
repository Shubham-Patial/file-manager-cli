import os
from pathlib import Path

def readfileandfolder():

    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")

def createfile():

    try:
        readfileandfolder()
        filename = input("Enter the name of the file to create: ")
        path = Path(filename)
        with open(path, 'x') as f:
            content = input("Enter content to add to the file: ")
            f.write(content)
            print(f"File '{path}' created successfully.\n")
    except FileExistsError:
        print(f"Error: File '{path}' already exists.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

def readfile():
    
    try:
        readfileandfolder()
        filename = input("Enter the name of the file to read: ")   
        path = Path(filename) 
        with open(path, 'r') as f:
            content = f.read()
            print(f"\nContent of '{path}':\n\n{content}\n")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

def updatefile():

    try:
        readfileandfolder()
        filename = input("Enter the name of the file to update: ")
        path = Path(filename)
        print("Press 1 for renaming your file ")
        print("Press 2 for overwriting the data of your file ")
        print("Press 3 for appending some content in your file ")
        opt = int(input("Choose your option :- "))

        if opt == 1:
            name = input("Enter the new name of the file ")
            renamed = Path(name)
            path.rename(renamed)
            print(f"File '{path}' name updated successfully.\n")
        if opt == 2:
            with open(path, 'w') as f:
                new_data = input("Write the new content in the file ")
                f.write(new_data)
                print(f"File '{path}' created from scratch successfully.\n")
        if opt == 3:
                with open(path, 'a') as fs:
                    content = input("Write the content you want in your new file :- ")
                    fs.write(" "+content)
                    print(f"File '{path}' updated successfully.\n")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

def deletefile():

    try:
        readfileandfolder()
        filename = input("Enter the name of the file to delete: ")
        path = Path(filename)
        os.remove(path)
        print(f"File '{path}' deleted successfully.\n")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")


try:
    while True:
        print("Press 1 to Create File.")
        print("Press 2 to Read File")
        print("Press 3 to Update File")
        print("Press 4 to Delete File")
        choice = int(input("Enter the option you want to select = "))

        match choice:

            case 1:
                createfile()
            
            case 2:
                readfile()

            case 3:
                updatefile()

            case 4:
                deletefile()

            case _:
                print("Please! Select one of the options mentioned above")

except ValueError:
    print("Invalid input. Please enter option from 1 to 4")
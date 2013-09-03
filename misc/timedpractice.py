# Filename: timedpractice.py
# Author: Gan Jing Ying
# Created: 20130903
# Modified: 20130903

import re
import datetime

# define functions
def menu():
    print("What would you like to do today?")
    print("[1] Search")
    print("[2] Add")
    print("[3] Update")
    print("[4] Delete")
    print("[0] Quit")

def validID(idnum):
    while len(idnum) != 4 or idnum[0] != 'E' or not idpattern.match(idnum[1:]):
        print("Error. Invalid ID.")

# open file
try:
    employ = open("EMPLOYEE.dat", "r+")
    menu() # opens the menu
    print()
    command = input("Enter a command: ")
    # validating the command
    while command != '0': # as long as the command is not to quit
        while not command.isdigit() or int(command) < 0 or int(command) > 4:
            print("Error. Command must be in digits of the range 0 - 4.")
            command = input("Enter a command: ")
        employ.seek(0)
        line = employ.readline()
        idpattern= re.compile("[0-5][0-9]{2}")
        
        if command == '1': # search
            idnum = input("Enter an employee's ID: ")
            validID(idnum) # runs validation tests
            while line != "": # while not end of file
                found = False
                if line[:4] == idnum: # record was found
                    found = True
                    print("Your record was found. Details of record are below.")
                    print()
                    # prints all the employee's information
                    print("ID no.: " + idnum)
                    print("Name: " + line[4:19])
                    print("Department: " + line[19:24])
                    print("Salary: " + line[24:])
                    break
                else:
                    line = employ.readline()
            if not found:
                print("Record was not found.")

            print()
            menu()
            print()
            command = input("Enter a command: ")
                        
        if command == '2': # add
            idnum = input("Enter an employee's ID: ")
            validID(idnum) # runs validation tests

            # finding the last ID in the file
            listID = []
            while line != "": # while not end of file
                listID.append(line[1:4])
                line = employ.readline()
            lastID = listID.pop()
            
            while idnum[1:] < lastID or idnum[1:] == lastID: # in the middle
                print("Error. ID must be greater than " + "E" + lastID +
                      " and cannot be an existent ID.")
                idnum = input("Enter an employee's ID: ")

            employ.close()
            try:
                employ = open("EMPLOYEE.dat", "a") # reopen the file for adding
                name = input("Enter name: ")
                while len(name) > 15: # length check for name
                    print("Name must be smaller than 15 characters long.")
                    name = input("Enter name: ")
                dep = input("Enter department: ")
                while len(dep) > 5: # length check for department
                    print("Department must be smaller than 5 characters long.")
                    dep = input("Enter department: ")
                salary = input("Enter salary: ")
                while len(salary) > 4 or not salary.isdigit(): # validation
                    print("Error. Salary must be integer between 1000 - 3000.")
                    salary = input("Enter salary: ")
                namespace = 15 - len(name)
                depspace = 5 - len(dep)
                
                # was supposed to be in one line
                data = idnum + name + namespace*" " + dep + depspace*" "
                data += salary + "\n"
                
                employ.write(data)
                successful = True
                employ.close()
                employ = open("EMPLOYEE.dat", "r+")
            except IOError:
                successful = False
                print("Error. 'EMPLOYEE.dat' cannot be opened.")
            if successful:
                log = open("LOG.dat", "a")
                log.write(str(datetime.datetime.now()) + "A" + data)
                log.close()
                print("Data has been added successfully.")

            print()
            menu()
            print()
            command = input("Enter a command: ")

        if command == '3': # update
            idnum = input("Enter an employee's ID: ")
            validID(idnum) # runs validation tests
            while line != "": # while not end of file
                found = False
                if line[:4] == idnum: # record was found
                    found = True

                    newsalary = input("Enter new salary: ")
                    # validation
                    while len(newsalary) > 4 or not newsalary.isdigit():
                        print("Error. Salary must be integer between"
                              " 1000 - 3000.")
                        newsalary = input("Enter salary: ")

                    # change data
                    employ.seek(0)
                    oldline = employ.readline()
                    alldata = '' # initialize the data lines
                    while oldline != line: # copy over all data until that line
                        alldata += oldline
                        oldline = employ.readline()
                    line = line[:-5] + newsalary + "\n"
                    alldata += line
                    oldline = employ.readline()
                    while oldline != "":
                        alldata += oldline
                        oldline = employ.readline()

                    # write everything into the file
                    employ.close()
                    try:
                        employ = open("EMPLOYEE.dat", "w")
                        employ.write(alldata)
                        successful = True
                        employ.close()
                        employ = open("EMPLOYEE.dat", "r+")
                    except IOError:
                        successful = False
                        print("Error. File 'EMPLOYEE.dat' cannot be read.")
                    if successful:
                        log = open("LOG.dat", "a")
                        log.write(str(datetime.datetime.now()) + "U" + line)
                        log.close()
                        print("Update successful.")
                    break
                else:
                    line = employ.readline()
            if not found:
                print("Record was not found.")

            print()
            menu()
            print()
            command = input("Enter a command: ")

        if command == '4':
            idnum = input("Enter an employee's ID: ")
            validID(idnum) # runs validation tests
            while line != "": # while not end of file
                found = False
                if line[:4] == idnum: # record was found
                    found = True
                    sure = input("Your record was found. Are you sure you "
                                 "want to delete it? (Y/N): ")
                    while sure != 'Y' and sure != 'N':
                        print("Error. Invalid command.")
                        sure = input("Are you sure you want to delete the"
                                     " record? (Y/N): ")
                    if sure == 'Y':
                        employ.seek(0)
                        oldline = employ.readline()
                        alldata = '' # initialize the data lines
                        while oldline != line: # copy over all data until that line
                            alldata += oldline
                            oldline = employ.readline()
                        data = line
                        line = '*' + line[1:]
                        alldata += line
                        oldline = employ.readline()
                        while oldline != "":
                            alldata += oldline
                            oldline = employ.readline()

                        # write everything into the file
                        employ.close()
                        try:
                            employ = open("EMPLOYEE.dat", "w")
                            employ.write(alldata)
                            successful = True
                            employ.close()
                            employ = open("EMPLOYEE.dat", "r+")
                        except IOError:
                            successful = False
                            print("Error. File 'EMPLOYEE.dat' cannot be read.")
                        if successful:
                            log = open("LOG.dat", "a")
                            log.write(str(datetime.datetime.now()) + "D" + data)
                            log.close()
                            print("Delete successful.")
                        break
                    elif sure == 'N':
                        print("Operation has been cancelled.")
                        break
                else:
                    line = employ.readline()

            if not found:
                print("Record was not found.")

            print()
            menu()
            print()
            command = input("Enter a command: ")
                    
    employ.close()
    print()
    print("Thank you for using this software.")
    
except IOError:
    print("Error. One of the files (or both) cannot be read.")

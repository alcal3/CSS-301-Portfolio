#Aleks Calderon
#6.10.2019
#contact list

import contacts

f = open("accountList.txt", "a+")


def addContact():
#prompts user to put in username first then the name of the contact
    add = str(input("Please type in the username: "))
#adds contact to the contact list
    con = open("contactList.txt", "r")

    for x in con:
        x = x.split()

        if contactList == x[1]:
            print("This person is already on your contact list.") 
#adds contact to existing list
        if contactList == x[0]:
            addCon = str(input("This person is not in your contact list. Would you like to add them?"))
            if (con == "yes" or con == "Yes"):
                con = open("contactList.txt", "a+")
                con.write(username + "\n")
                contactList[x] = 1
                print("This contact has been added to your list!")

def contactList():

    listcontacts = str(input("To list your contacts please type CONTACTS. To add a contact to your current list please type ADD: "))
    if (listcontacts == "CONTACTS"):
#opens file that has contact list and prints out the list
        f = open("contactList.txt", "a+")
        for w in f:
#splits line by line for contactlist
            w = w.split()
            contactList(w)
            print(f)
    else:
        addContact()

contactList()   

Contact = {}


def display_contact():
    print(Contact.items())
    print("Name\t\tContact Number")
    for key in Contact:
        print("{}\t\t{}".format(key,Contact.get(key)))


while True:
    choice = int(input(" 1. Add new contact \n "
                       "2. Search contact \n"
                       " 3.Display contact\n "
                       "4. Edit contact \n"
                       " 5. Delete contact\n"
                       " 6.Exit\n"
                       "\n Enter your choice It Should Be Number 1-6: "))
    if choice == 1:
        name = input("Contact Name:  ")
        phone = input("Phone Number: ")
        Contact[name] = phone


    elif choice == 2:
        ContactNo = input("Search Contact: ")
        if ContactNo in Contact:
            print(ContactNo," contact number is ",Contact[ContactNo])
        else:
            print("\n Not Found The Contact \n ")


    elif choice == 3:
        if not Contact:
            print("contact book is empty")
        else:
            display_contact()


    elif choice == 4:
        edit_contact = input("Edit Your Contact: ")
        if edit_contact in Contact:
            phone = input("enter mobile number: ")
            Contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")


    elif choice == 5:
        del_contact = input("What Do You Want To Delete: ")
        if del_contact in Contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='y' or confirm =='Y':
                Contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break
#phone directory using dictionary

def get_key(val):
    for key,value in directory.items():
        if val==value:
            return key


def call_by_choice(n):
   if(n==1):
       show_all()
   elif(n==2):
       add()
   elif(n==3):
       remove()
   elif(n==4):
       search_by_no()
   elif(n==5):
       search_by_initial()
   elif(n==6):
       phone=search_by_name()
       print("Name: ",directory[phone],"\tPhone: ",phone)
   """else:
       print("Input Error! Invalid value entered: ")
       exit()"""

def show_all():
    print("\n Telephone Numbers: \n\n")
    name_list=list()
    for name in directory.values():
        name_list.append(name)
    name_list.sort()
    for name in name_list:
            print("Name: ",name,"\tPhone: ",get_key(name))

def add():
    print("\n Add name and number: \n\n")
    name=input("Name: ")
    phone=input("Phone: ")
    directory[phone]=name

def remove():
    print("\nRemove entry from directory: \n\n")
    a=input("Do you know the number or want to search by name?(Y/N)")
    if(a=='Y' or a=='y'):
        phone=input("Enter phone: ")
    else:
        phone=search_by_name()
    if phone in directory:
        print("Deleting...")
        del directory[phone]
        print("Entry Deleted!")
    else:
        print("Error! Phone number not found")

def search_by_no():
    phone=input("\nEnter phone to search:")
    print("\nSearching...\n\n")
    if phone in directory:
         print("Name: ",directory[phone],"\tPhone: ",phone)
    else:
         print("Error! Phone number not found")

def search_by_initial():
    init=input("Enter first letter of name to search: ")
    if(len(init)==1):
        for name in directory.values():
            if(name[0]==init):
                 print("Name: ",name,"\tPhone: ",get_key(name))
    else:
        print("Invalid Input")

def search_by_name():
    print("\n Searching by name: ")
    phone_list=list()
    name=input("Enter a name to search in the directory: ")
    for phone in directory.keys():
        if directory[phone]==name:
           print("Name: ",name,"\tPhone: ",phone)
           phone_list.append(phone)
            
    if(len(phone_list)==0):
         print("\nNo entry by this name")
         return False
    elif(len(phone_list)==1):
         return phone_list[0]
    else:
        n=int(input("\nChoose which phone no to return: "))
        if(n<=len(phone_list)):
            return phone_list[n-1]
        else:
            return False

def print_menu():

   choice=0
   while(choice!=7):
     print("1. Print all phone numbers in directory")
     print("2. Add a phone number to the directory")
     print("3. Remove a phone number from directory")
     print("4. Search a number in directory")
     print("5: Search a number by first letter of name")
     print("6. Search by name")
     print("7. Quit")
     choice=int(input("\n\n\n Enter your choice: "))
     call_by_choice(choice)
   else:
       print("You chose to quit...\nExiting...")
       exit()

print("TELEPHONE DIRECTORY\n\n\n")
directory=dict()
print_menu()



    




    

import json 
import string
print("welcome to expense tracker...")
expenses =[] # creation of a list named expenses, it lives forever in the program
def add_expense(): # function definition , no parameters given
     while True: # loops to check for errors
         try: 
            amount = float(input(" Enter the cost")) 
            name = string(input("enter your name: "))
            category = string(input("Enter the category of your expense"))
            break
         except ValueError:
             print ("Invalid input, try again")

     expense = { "amount":amount,
                 "category":category,
                 "name":name
               }
     expenses.append(expense)
     save_expenses()
     print("Expense added succecfully!")
# side note: why does coding feel like solving maths???

def view_details (): 
     if not expenses: # assuming the user clicks on opt 2 and there's no expense input yet
          print("no expenses yet")
     else:
       for i, exp in enumerate(expenses, start=1): # i is for counter, exp is the expense list with the expenses dictionaries, start ensures i starts from 1
           print(f"{i}. {exp['name']} - ${exp['amount']} {exp['category']}") #f is to format the sentence with the insertion of variables using  the curly braces and the use of square brackets for accessing dictionary values    
           print()

def add_exp():
    total = 0
    for exp in expenses: # take each item inside of te list and name it exp
     total+= exp['amount']
    print (total)
    
#def show_total():
   # print(f"Total ecpenses: ${add_exp()}\n")

def save_expenses():
    with open ('expenses.json', 'w') as file:
        json.dump (expenses, file)

def load_expenses():
    global expenses
    try:
        with open ('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
        
#choice=()???
#def view_menu():
     #pick = int(input("Enter your choice: "))
     #print (" 1. Add expenses")
     #print (" 2. View expenses")
     #print ("3. Quit")
    
     


# add expenses
while True:
    print("WELCOME TO EXPENSE TRACKER")
    print("1. Add expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Quit")
    print ("0. Previous")
    choice = int(input("CLICK ON ANY OPTION TO COUNTINUE" ))
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_details()
    elif choice == 3:
        add_exp()
    elif choice == 4:
      print ("Goodbye! THANK YOU FOR USING THIS SYSTEM")
      break
    else:
        print("INVALID CHOICE")
        
# errors to move to intermediate level
# no input safety
# menu numbering inconsistency
# function naming clarity
# 
    


 
    
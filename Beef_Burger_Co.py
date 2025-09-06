import sys #allows for sys.exit() function

#Full Menu Dictionary
menu = {'Burgers': { #Burger Menu Dictionary
    'Cheeseburger': { #Dictionary for individual item
    'Price': 8.99, #Key:Value pair for price
    'Toppings': ['Beef Patty', 'Cheese', 'Pickles', 'Onion', 'Ketchup', 'Mustard'] #Key:Value Pair with list for toppings 
    },
    'Beef Burger': {
        'Price': 9.95,
        'Toppings': ['Beef Patty', 'Cheese', 'Tomato', 'Lettuce', 'Pickles', 'Ketchup', 'Mustard']
    },
     'Bacon Burger': {
        'Price': 9.95,
        'Toppings': ['Beef Patty', 'Cheese', 'Bacon', 'Onion Rings', 'Barbecque Sauce']
    }
    },
    'Sides': { #Sides Menu Dictionary
        'Small Fries':{ 
        'Price':3.49
    },
    'Medium Fries':{ 
        'Price':4.49
    },
    'Large Fries':{ 
        'Price':5.99
    }},
    
    'Drinks': { #Drinks Menu Dictionary
        'Small Coke':{'Price': 3.49},
        'Large Coke':{'Price':4.99},
        'Small Sprite':{'Price': 3.49},
        'Large Sprite':{'Price':4.99},
        'Small Fanta':{'Price': 3.49},
        'Large Fanta':{'Price':4.99},}
}

#Toppings that a customer can add to their burger
burger_toppings = ['Beef Patty', 'Bacon', 'Cheese', 'Pickles', 'Onion', 'Onion Rings', 'Tomato', 'Lettuce', 'Ketchup', 'Mustard', 'Barbecque Sauce']

#Customer order Dictionary, information gets added to this after an item is ordered, and this is then printed out at the checkout
customer_order = {'Burgers':[], #Dictionary for Burger Orders
                  'Sides':[], #Dictionary for Sides Orders
                  'Drinks':[]} #Dictionary for Drinks Orders

def order(): #Function for ordering a burger
    print("Welcome to Beef Burger Co!")
    while True:
        print("Here's our menu:")
        for index, key in enumerate(menu.keys()): #Prints out keys of menu dictionary (names of sub-menus) - enumerate() allows these to be printed as a numerical list
            print(f"{index+1}. {key}")
        menu_option = input("Enter 1, 2, or 3 to select a menu to view, or enter 4 to complete your order: ") #Customer selects menu or proceeds to checkout
        if menu_option == '1':
            burgers() #Goes to burger menu
        elif menu_option == '2':
            sides() #Goes to sides menu
        elif menu_option == '3':
            drinks() #Goes to drinks menu
        elif menu_option == '4':
            checkout() #Goes to checkout
        else:
            print("Invalid choice.") #If customer enters a value other than 1, 2, 3 or 4

def burgers(): #Burger Menu
    print('Burgers Menu:')
    burger_list = list(menu['Burgers'].items()) #Creates list of keys/values in burger menu to print
    for index, (burger, details) in enumerate(burger_list): 
        print(f'{index+1}. {burger}: ${details['Price']}') #Prints numbered list with burger and price
    while True:
        selection = (input("Enter an item's number to view it, or type r to return to menu selection or c to proceed to the checkout: "))
        try:
            selection = int(selection)
            if 1 <= selection <= len(burger_list): #If number within range of burgers in menu
                selected_burger, details = burger_list[selection-1] #Accesses burger name and details from list, (choice -1 to get correct index value as list starts from 0)
                print(f"{selected_burger}:") #Burger Name
                print(f"  Price: ${details['Price']}") #Burger Price
                print(f"  Toppings: {', '.join(details['Toppings'])}") #Prints toppings of burger
                while True:
                    choice = input('Add burger to order? y for yes, n to return to the menu ')
                    if choice == 'y':
                        updated_toppings=list(details['Toppings']) # Allows removals to be removed from burger toppings/additions added
                        choice = input('Make any changes to order? 1. Yes, 2. No ')
                        if choice == '1':
                            additions = [] #Additions are added to list as selected
                            removals = [] #Removals are added to list as selected
                            while True:
                                choice = input('1. Add an item\n 2. Remove an item\n 3. Continue ')
                                if choice == '1':
                                    print(f"Current toppings on your {selected_burger}:")
                                    print(', '.join(updated_toppings))
                                    print('Available items:')
                                    print(', '.join(burger_toppings)) #Prints toppings that can be added to a burger
                                    choice = input('Select an item from the list to add to your burger, or press enter to return to the changes menu: ').title()
                                    if choice in burger_toppings: 
                                        if choice in removals: #item was previously removed from burger
                                            removals.remove(choice) #removes item from removals list
                                        else:
                                            additions.append(choice) #Adds item to additions list
                                        updated_toppings.append(choice) #Adds item to the list of items on the customers current burger order
                                        print(f"{choice} added to burger") 
                                elif choice == '2':
                                    print(f"{selected_burger} toppings:")
                                    print(', '.join(details['Toppings'])) #Prints toppings on burger
                                    if details['Toppings'] != updated_toppings:
                                        print(f"Current toppings on your {selected_burger}:")
                                        print(', '.join(updated_toppings)) #Prints toppings on burger
                                    #Make code only print out current toppings on burger
                                    choice = input('Select an item to remove from the burger, or press enter to return to the changes menu:').title()
                                    if choice in updated_toppings:
                                        if choice in additions: #Item was previously added to burger
                                            additions.remove(choice) 
                                        else:
                                            removals.append(choice) #Adds toppings to removals list
                                        updated_toppings.remove(choice) #Remove topping from customers current burger order
                                        print(f"{choice} removed from burger")
                                    elif choice != '':
                                        print('This item is not on the burger')
                                elif choice == '3':
                                    while True:
                                        try:
                                            choice = int(input('How many would you like to order? '))
                                            if choice > 0:
                                                print(f"{choice} {selected_burger} added to order") 
                                                if updated_toppings != details['Toppings']:
                                                    burger_added = 'n'
                                                    for i in customer_order['Burgers']:
                                                        if i['Item'] == selected_burger and i['Additions'] == additions and i['Removals'] == removals and i['Updated Toppings'] == updated_toppings: #If burger with same changes is already in order
                                                            i['Quantity'] += choice #Increaes quantity rather than creating a new item in list so it is only printed out once at checkout
                                                            burger_added = 'y' #sets to y so burger is not added again below
                                                            break
                                                    if burger_added == 'n': #only adds if burger was not added in loop above
                                                            customer_order['Burgers'].append({'Item': selected_burger, 'Quantity':choice,'Price': details['Price'], 'Additions':additions, 'Removals':removals, 'Updated Toppings':updated_toppings}) #Adds order details to customer_orders dictionary to print out at checkout
                                                            break
                                                    break
                                                else:
                                                    burger_added = 'n' 
                                                    for i in customer_order['Burgers']:
                                                        if i['Item'] == selected_burger and i['Additions'] == additions and i['Removals'] == removals: #If burger with same changes is already in order
                                                            i['Quantity'] += choice #Increaes quantity rather than creating a new item in list so it is only printed out once at checkout
                                                            burger_added = 'y' #sets to y so burger is not added again below
                                                            break
                                                    if burger_added == 'n': #only adds if burger was not added in loop above
                                                            customer_order['Burgers'].append({'Item': selected_burger, 'Quantity':choice,'Price': details['Price'], 'Additions':additions, 'Removals':removals}) #Adds order details to customer_orders dictionary to print out at checkout
                                                            break
                                                    break
                                            else:
                                                print("Enter a valid input")
                                        except ValueError:
                                            print('Enter a valid input')
                                    break
                                else:
                                    print("Enter a valid input")
                        else:
                            while True:
                                try:
                                    choice = int(input('How many would you like to order? '))
                                    if choice > 0:
                                        print(f"{choice} {selected_burger} added to order")
                                        burger_added = 'n' 
                                        for i in customer_order['Burgers']:
                                            if i['Item'] == selected_burger and i['Additions'] == '' and i['Removals'] == '': #If burger with same changes is already in order
                                                i['Quantity'] += choice #Increaes quantity rather than creating a new item in list so it is only printed out once at checkout
                                                burger_added = 'y' #sets to y so burger is not added again below
                                                break
                                        if burger_added == 'n': #only adds if burger was not added in loop above
                                            customer_order['Burgers'].append({'Item': selected_burger, 'Quantity':choice,'Price': details['Price'], 'Additions':'', 'Removals':''}) #Adds order details to customer_orders dictionary to print out at checkout
                                            break
                                        break
                                    else:
                                        print("Enter a valid input")
                                except ValueError:
                                    print('Enter a valid input')
                        burgers()
                    else:
                         burgers()
                    break
            else: #User's integer input is not within range of number of burgers
                print("Invalid Choice")
        except ValueError:  #If user's input is not an integer
            selection = str(selection)
            selection = selection.lower()
            if selection == 'r': #Return to main menu
                order()
            elif selection == 'c':#Proceed to checkout
                checkout()
            else:
                print("Invalid Choice") #Any other choice is invalid
def sides(): #Sides Menu
    print('sides')

def drinks(): #Drinks Menu
    print('drinks')

def checkout(): #Checkout
    print(customer_order)
    if len(customer_order['Burgers']) != 0: #Checks if no burgers were ordered
        print('Burgers')
        for burger in customer_order['Burgers']:
            for key, value in burger.items():
                if key == 'Additions' or key == 'Removals':
                    if len(value) > 0:
                        print(f'{key}: {value}')
                elif key == 'Price':
                    print(f"Price: ${value}") #Different print to add dollar sign 
                else:
                    print(f'{key}: {value}')
    sys.exit() #Ends program


order() #Calls function to begin program
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
    }},
    'Drinks': { #Drinks Menu Dictionary
        'Small Coke':{'Price': 3.49},
        'Large Coke':{'Price':4.99}}
}

#Toppings that a customer can add to their burger
burger_toppings = ['Beef Patty', 'Bacon', 'Cheese', 'Pickles', 'Onion', 'Onion Rings', 'Tomato', 'Lettuce', 'Ketchup', 'Mustard', 'Barbecque Sauce']

#Customer order Dictionary, information gets added to this after an item is ordered, and this is then printed out at the checkout
customer_order = {'Burgers':{ #Dictionary for Burger Orders

},
                  'Sides':{}, #Dictionary for Sides Orders
                  'Drinks':{}} #Dictionary for Drinks Orders

def order(): #Function for ordering a burger
    print("Welcome to Beef Burger Co!")
    while True:
        print("Here's our menu:")
        for index, key in enumerate(menu.keys()): #Prints out keys of menu dictionary (names of sub-menus) - enumerate() allows these to be printed as a numerical list
            print(f"{index+1}. {key}")
        choice = input("Enter 1, 2, or 3 to select a menu to view, or enter 4 to complete your order: ") #Customer selects menu or proceeds to checkout
        if choice == '1':
            burgers() #Goes to burger menu
        elif choice == '2':
            sides() #Goes to sides menu
        elif choice == '3':
            drinks() #Goes to drinks menu
        elif choice == '4':
            checkout() #Goes to checkout
        else:
            print("Invalid choice.") #If customer enters a value other than 1, 2, 3 or 4

def burgers(): #Burger Menu
    print('burger')


def sides(): #Sides Menu
    print('sides')

def drinks(): #Drinks Menu
    print('drinks')

def checkout(): #Checkout
    print('money please')
    #Print out order and cost
    quit() #Ends program


order() #Calls function to begin program
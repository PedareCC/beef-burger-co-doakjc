menu = {'Burgers': {
    'Cheeseburger': {
    'Price': 8.99,
    'Toppings': ['Beef Patty', 'Cheese', 'Pickles', 'Onion', 'Ketchup', 'Mustard']
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
    'Sides': {'Small Fries':{
        'Price':3.49
    }},
    'Drinks': {'Small Coke':{'Price': 3.49},
               'Large Coke':{'Price':4.99}}
}

burger_toppings = ['Beef Patty', 'Bacon', 'Cheese', 'Pickles', 'Onion', 'Onion Rings', 'Tomato', 'Lettuce', 'Ketchup', 'Mustard', 'Barbecque Sauce']

customer_order = {'Burgers':{

},
                  'Sides':'',
                  'Drinks':''}

def order():
    print("Welcome to Beef Burger Co!")
    while True:
        print("Here's our menu:")
        for index, key in enumerate(menu.keys()):
            print(f"{index+1}. {key}")
        try:
            choice = int(input("Enter 1, 2, or 3 to select a menu to view, or enter 4 to complete your order: "))
            if choice == 1:
                burgers()
            elif choice == 2:
                sides()
            elif choice == 3:
                drinks()
            elif choice == 4:
                checkout()
            else:
                print("Invalid choice.")
        except ValueError:
            print('Invalid Choice')

def burgers():
    print('burger')


def sides():
    print('sides')

def drinks():
    print('drinks')

def checkout():
    print('money please')


order()
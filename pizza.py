# Name: Ashley Gatterman
# Prog Purpose: This program creates a receipt for a Palermo Pizza purchase.
#   NOTE: All pizzas have no toppings.
#   NOTE: The user must be able to enter upper or lower case pizza code.
#       S Small pizza: $9.99
#       M Medium pizza: $12.99
#       L Large pizza: $14.99
#       X Extra Large pizza: $17.99
#       Sales tax rate: 5.5%

import datetime

#define tax rate and prices
SALES_TAX_RATE = 0.055
S_PIZZA = 9.99
M_PIZZA = 12.99
L_PIZZA = 14.99
X_PIZZA = 17.99

#define global variables
pizza_size = 0
num_pizza = 0
pizza_cost = 0
sales_tax = 0
total = 0

#define program functions
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to make another order? (Y/N): ")
        if yesno.upper() != "Y":
            another_order = False

def get_user_data():
    global pizza_size, num_pizza
    pizza_size = str(input("Pizza slice size (S,M,L,X): "))
    num_pizza = int(input("Number of pizza slices: "))
 
def perform_calculations():
    global pizza_cost, sales_tax, total
    if pizza_size.upper() == 'S':
        pizza_cost = num_pizza * S_PIZZA
    elif pizza_size.upper() == 'M':
        pizza_cost = num_pizza * M_PIZZA
    elif pizza_size.upper() == 'L':
        pizza_cost = num_pizza  * L_PIZZA
    elif pizza_size.upper() == 'X':
        pizza_cost = num_pizza * X_PIZZA
    else:
        pizza_cost = 0
    sales_tax = pizza_cost * SALES_TAX_RATE
    total = pizza_cost + sales_tax

def display_results():
    print('\n------------------------------------')
    print('********** PALERMO PIZZA ***********')
    print('------------------------------------')
    print("     " + str(datetime.datetime.now()))
    print('------------------------------------')
    print('Number of pizzas          : ' + format(num_pizza,'8'))
    print('Pizza cost                $ ' + format(pizza_cost,'8,.2f'))
    print('Sales Tax                 $ ' + format(sales_tax,'8,.2f'))
    print('Total                     $ ' + format(total,'8,.2f'))
    print('------------------------------------')
    print('We look forward to seeing you again.')
    print('------------------------------------')

#call on program to execute
main()

# Name: Ashley Gatterman
# Prog Purpose: This program calculates the weekly pay for a Fresh Food Marketplace store employee.
#
#   Category codes and hourly pay rates:
#       C   Cashier: $16.50
#       S   Stocker: $15.75
#       J   Janitor: $15.75
#       M   Maintenance: $19.50
#
#   Deduction Rates:
#       Federal income tax rate: 12%
#       State income tax rate: 3%
#       Social Security tax rate: 6.2%
#       Medicare tax rate: 1.45%

import datetime

#define deduction rate tuple
DEDUCTION_RATES = (0.12, 0.03, 0.062, 0.0145)

#define pay rate tuple
PAY_RATES = (16.50, 15.75, 15.75, 19.50)

#define global variables
hours_worked = 0
job_category = 0
pay_rate = 0
gross_pay = 0
federal_deduct = 0
state_deduct = 0
social_security_deduct = 0
medicare_deduct = 0
total_deduct = 0
net_pay = 0

#define program functions
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to input data for another employee? (Y/N): ")
        if yesno.upper() != "Y":
            another_employee = False
            print("\nHave a good day.")

#ask user for job category code and number of hours worked
def get_user_data():
    global job_category, hours_worked
    job_category = str(input("Job category code (C,S,J,M): "))
    hours_worked = int(input("Number of hours worked: "))

# Calculations (Gross pay, each deduction amount, total deductions, net pay)
def perform_calculations():
    global gross_pay, federal_deduct, state_deduct, total_deduct, social_security_deduct, medicare_deduct, net_pay
    #assign job category pay rate
    if job_category.upper() == "C":
        pay_rate = PAY_RATES[0]
    elif job_category.upper() == "S":
        pay_rate = PAY_RATES[1]
    elif job_category.upper() == "J":
        pay_rate = PAY_RATES[2]
    elif job_category.upper() == "M":
        pay_rate = PAY_RATES[3]
    else:
        pay_rate = 0
        print("\nPlease enter a valid job code.")
    #gross pay 
    gross_pay = hours_worked * pay_rate
    #calculate each deduction
    federal_deduct = gross_pay * DEDUCTION_RATES[0]
    state_deduct = gross_pay * DEDUCTION_RATES[1]
    social_security_deduct = gross_pay * DEDUCTION_RATES[2]
    medicare_deduct = gross_pay * DEDUCTION_RATES[3]
    #total deductions
    total_deduct = federal_deduct+state_deduct+social_security_deduct+medicare_deduct
    #net pay
    net_pay = gross_pay - total_deduct

def display_results():
    print('\n********************************')
    print('     Fresh Food Marketplace     ')
    print('   Store Employee Weekly Pay    ')
    print('--------------------------------')
    print('Number of hours     : ' + format(hours_worked,'10'))
    print('Gross Pay           $ ' + format(gross_pay,'10,.2f'))
    print('Federal income tax  $ ' + format(federal_deduct, '10,.2f'))
    print('State income tax    $ ' + format(state_deduct,'10,.2f'))
    print('Social security tax $ ' + format(social_security_deduct, '10,.2f'))
    print('Medicare tax        $ ' + format(medicare_deduct, '10,.2f'))
    print('Total deductions    $ ' + format(total_deduct, '10,.2f'))
    print('Net pay             $ ' + format(net_pay,'10,.2f'))
    print('--------------------------------')
    print('   ' + str(datetime.datetime.now()))
    print('********************************')

#execute program
main()

"""
4. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires,
and maintenance. The program should then display the total monthly cost of these
expenses, and the total annual cost of these expenses.
"""
def main():
    loan = float(input("please enter the monthly costs for loan payment: "))
    insurance = float(input("please enter the monthly costs for insurance: "))
    gas = float(input("please enter the monthly costs for gas: "))
    oil = float(input("please enter the monthly costs for oil: "))
    tires = float(input("please enter the monthly costs for tires: "))
    maintenance = float(input("please enter the monthly costs for maintenance: "))

    cost_monthly = monthly_costs(loan, insurance, gas, oil, tires, maintenance)
    cost_annual = annual_costs(loan, insurance, gas, oil, tires, maintenance)
    print(f"your monthly costs are {cost_monthly:.2f} CHF and your annual costs are {cost_annual:.2f} CHF")


def monthly_costs(loan, insurance, gas, oil, tires, maintenance):
    total_monthly= loan + insurance + gas + oil + tires + maintenance
    return total_monthly

def annual_costs(loan, insurance, gas, oil, tires, maintenance):
    total_annual = 12 * monthly_costs(loan, insurance, gas, oil, tires, maintenance)
    return total_annual


# Conditionally execute main only if this module is run as the main program
if __name__ == '__main__':
    main()
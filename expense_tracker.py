import pyinputplus as pyip
from pprint import pprint
import datetime


# This is a simple Expense Tracker application.
# It tracks expenses to a budget. 
# Categorize expenses
# Includes overspend warnings
# Surplus gets added to the savings account, shortfall deducted from the Savings account.

categories = {}
income = []
savings_acc = []
transactions = []
entry = {}
entry_dict = dict(date={}, item={}, category={}, cost={})

income.append(pyip.inputNum("What is your monthly income: "))

def category_selector():
    print("Here is a list of budget categories: ")
    for cat_list in (list(dict.keys(categories))):
        print(cat_list)
    if bool(categories) == False:
        print("There are no categories yet.")

    edit_category = pyip.inputYesNo("Would you like to add or remove a category? yes/no ")
    if edit_category == "yes":
        add_category = pyip.inputChoice(['add', 'delete'])
        if add_category == "add":
            new_cat_name = input("What is the name of the new category? ")
            categories[new_cat_name] = {}
            cat_add_add = list(dict.keys(categories))
            print(f"How much would you like allocate for {new_cat_name} ?")
            categories[new_cat_name] = pyip.inputNum(new_cat_name + ": ")
            income.append(categories[new_cat_name])

        elif add_category == "delete":
            if bool(categories) == False:
                print("There are no categories to delete")

            else:
                del_cat_name = input("Which category would you like to delete ")
                del categories[del_cat_name]

    income[0] = income[0] - income[-1]

    # Budget overdrawn warning
    if income[0] <= 0:
        print("WARNING: You're over budget!")
    print(f"Balance: R{income[0]}\n")

    # Print categories & their budgets
    for key, value in categories.items():
        print(key, ' : ', value)


category_selector()
while True:
    another_category = input("Would you like to add another category? yes/no ")
    if another_category == "yes":
        category_selector()
    elif another_category == "no":
        break

"""

# TODO: budget surplus into savings
# Deposit surplus budget into savings
if budget >= 0:
    print(f"Budget surplus = {budget}\n" 
          f"Depositing surplus into savings account.\n")
    savings_acc = int(str(savings_acc)) + int(str(budget))
    print(f"Savings account balance: {savings_acc}\n")
"""

def entry():
    # Loop to generate expense entries according to date, type of expense, category & price
    date = pyip.inputDate(prompt='Date of expense: ', formats=['%d/%m/%Y'])
    entry_dict["date"] = date

    expense: str = input("What was the expense for? ")
    entry_dict["item"] = expense

    print("Choose a category: (write the category name)")
    spend_cat = list(dict.keys(categories))
    choice_cat = pyip.inputMenu(spend_cat, numbered=True)
    entry_dict["category"] = choice_cat

    cost = pyip.inputFloat(prompt='Cost: ')
    entry_dict["cost"] = cost
    print("\n")

    transactions.append(list(entry_dict.items()))

    # Check if categories match. If they match, deduce purchase amount from category budget
    if entry_dict["category"] in categories.keys():
        check_cats = entry_dict["category"]
        categories[check_cats] = categories[check_cats] - transactions[-1][3][1]

    print("\n")

    # Print transaction entry
    for key, value in entry_dict.items():
        print(key, ' : ', value)

    print("\n")

    # Print updated category budgets
    for key, value in categories.items():
        print(key, ' : ', value)

print("\n")

# Check whether the user wants to add an entry
while True:
    another = input("Would you like to add an entry? yes/no ")
    if another == "yes":
        entry()
    elif another == "no":
        break

print("\n")

# Print list of transactions
pprint(transactions)






# TODO: Option to use existing categories / non-new users

# TODO: Print final - items, category totals, grand total
# TODO: Low budget warning
# TODO: Add totals & display transactions from categories
# TODO: Show expense so far per category
# TODO: Deduct expenses off total budget

# TODO: Assign transactions to categories

# TODO: List by category, type, date & price
# TODO: Draw chart of expenses

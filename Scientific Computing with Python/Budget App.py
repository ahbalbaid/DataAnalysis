
# It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment.
# When objects are created, they are passed in the name of the category.

# Input:
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
# print(food)
# print(clothing)
#
# print(create_spend_chart([food, clothing, auto]))

class Category:
    '''It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment.'''
    def __init__(self, category):
        '''The class should have an instance variable called ledger that is a list. '''
        self.category = category
        self.ledger = list()


# The class should also contain the following methods:
    def deposit(self, amount, description=''):
        '''A deposit method that accepts an amount and description. If no description is given, it should default to an empty string.
        The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.'''
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=''):
        '''A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number.
        If there are not enough funds, nothing should be added to the ledger.
        This method should return True if the withdrawal took place, and False'''
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        '''A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.'''
        balance = 0
        for i in self.ledger:
           balance += i['amount']

        return balance

    def transfer(self,amount,category):
        '''A transfer method that accepts an amount and another budget category as arguments.
        The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
         The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
         If there are not enough funds, nothing should be added to either ledgers.
        This method should return True if the transfer took place, and False otherwise.'''
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self,amount):
        '''A check_funds method that accepts an amount as an argument.
         It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
         This method should be used by both the withdraw method and transfer method.'''
        if self.get_balance() >= amount:
            return True
        return False

    def totalwithdraws(self):
        balance_withdraws = 0
        for i in self.ledger:
            if i['amount'] < 0:
                balance_withdraws += i['amount']
        return balance_withdraws

    def __str__(self):
        ''' Output:
        *************Food*************
        initial deposit        1000.00
        groceries               -10.15
        restaurant and more foo -15.89
        Transfer to Clothing    -50.00
        Total: 923.96'''
        title = f'{self.category:*^30}\n'
        all = ''
        balance = 0
        for i in self.ledger:
            all += f"{i['description'][0:23]:23}{i['amount']:>7.2f}\n"
            balance += i['amount']
        output = f'{title}{all}Total: {str(balance)}'
        return output

def create_spend_chart(categories):
    '''create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
    Output:
    Output:
 Percentage spent by category
 100|
  90|
  80|
  70|
  60| o
  50| o
  40| o
  30| o
  20| o  o
  10| o  o  o
   0| o  o  o
     ----------
      F  C  A
      o  l  u
      o  o  t
      d  t  o
         h
         i
         n
         g'''
    output = 'Percentage spent by category\n'
    scale = [
        '100',
        '90',
        '80',
        '70',
        '60',
        '50',
        '40',
        '30',
        '20',
        '10',
        '0',
    ]
    balance = 0
    for i in categories:
        balance += round(i.totalwithdraws(), 2)
    categorys = [i.category for i in categories]
    categorys_withdraws = [i.totalwithdraws() for i in categories]
    categorys_withdraws_percent = [round(i / balance, 2) * 100 for i in
                        categorys_withdraws]

    for i in scale:
        output += i.rjust(3) + '| '
        for j in categorys_withdraws_percent:
            if int(i) <= j:
                output += 'o  '
            else:
                output += '   '
        output += '\n'

    output += '    ----' + '---' * (len(categorys) - 1)
    output += '\n     '

    lenght = 0
    for i in categorys:
        if lenght < len(i):
            lenght = len(i)

    for i in range(lenght):
        for j in categorys:
            if len(j) > i:
                output += j[i] + '  '
            else:
                output += '   '
        if i < lenght - 1:
            output += '\n     '

    return output

# create_spend_chart: takes a list of categories as an argument. It should return a string that is a bar chart.
# The chart should show the percentage spent in each category passed in to the function.
# The percentage spent should be calculated only with withdrawals and not with deposits.
# Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character.
# The height of each bar should be rounded down to the nearest 10.
# The horizontal line below the bars should go two spaces past the final bar.
# Each category name should be written vertically below the bar.
# There should be a title at the top that says "Percentage spent by category".

if __name__ == '__main__':
    pass
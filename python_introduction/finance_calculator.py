income = input('Enter your monthly income: ')
expenses = input('Enter your monthly expenses: ')
savings = expenses - income
projected_savings = savings * 12 + (savings * 12 * 0.05)
print('Your monthly savings are $',savings)
print('Projected savings after one year, with interest, is: $',projected_savings)

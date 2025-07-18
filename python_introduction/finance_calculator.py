monthly_income = input('Enter your monthly income: ')
monthly_expenses = input('Enter your monthly expenses: ')
monthly_savings = monthly_expenses - monthly_income
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print('Your monthly savings are $',monthly_savings)
print('Projected savings after one year, with interest, is: $',projected_savings)

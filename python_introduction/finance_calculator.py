monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = int((monthly_income - total_monthly_expenses))

#annual_interest_rate = 5

#print(monthly_savings)
#print(f"projected savings after one year, with interest, is : {}")
print(f"Your monthly savings are {monthly_savings}")
projected_savings = monthly_savings * 12 + (int(monthly_savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is: {projected_savings}")
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
monthlysavings = income - expenses

projectedsavings = monthlysavings * 12 + (monthlysavings * 12 * 0.05)
print(f"Your monthly savings are ${monthlysavings}")

print(f"Projected savings after one year, with interest, is: ${projectedsavings}")
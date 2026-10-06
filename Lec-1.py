# 28. Hands-on TasksTask 1 — Personal Information Create variables for:Name
# Age
# City
# Qualification
# Experience
# Display all information.

Name="Priyanshu"
age=21
city="Ahemdabad"
Qualification="BCA"
Experience="Fresher"

print("The name is:",Name)
print("The age is:",age)
print("The city is:",city)
print("The qualification is:",Qualification)
print("The experience is:",Experience)


# Task 2 — Employee Salary
# Create: basic_salary = 30000
# allowance = 5000
# bonus = 3000
# Calculate:
# Total Salary = Basic Salary + Allowance + Bonus

basic_salary=30000
allowance=5000
bonus=3000
total_salary=basic_salary+allowance+bonus
print("\nThe total salary is:",total_salary)

# Task 3 — Sales Calculation
# Create: quantity = 10
# unit_price = 2500
# Calculate total sales.

quantity=10
unit_price=2500
total_sales=quantity*unit_price
print("\nThe total sales is:",total_sales)

# Task 4 — Profit Calculation
# Create:sales = 100000
# cost = 75000
# Calculate:Profit
# Profit Percentage
# Formula:Profit = Sales - Cost
# Profit % = (Profit / Sales) × 100

sales=100000
cost=75000
profit=sales-cost
profit_percentage=(profit/sales)*100
print("\nThe profit is:",profit)
print("The profit percentage is:",profit_percentage)

# Task 5 — Average Marks
# Create marks for five subjects: Python
# SQL
# Excel
# Power BI
# Statistics
# Calculate:
# Total marks
# Average marks
Python=78
SQL=85
Excel=80
Power_bi=78
Stat=90
Total_marks=Python+SQL+Excel+Power_bi+Stat
Average_marks=Total_marks/5
print("\nThe total marks is:",Total_marks)
print("The average marks is:",Average_marks)

# Task 6 — Customer Bill
# Take the following from the user Product name
# Quantity
# Unit price
# Calculate and display:
# Product
# Quantity
# Unit Price
# Total Amount

product_name=input("Enter your product name:")
quantity=int(input("Enter the quantity:"))
unit_price=float(input("Enter the unit price:"))

print("\n Product name is:",product_name)
print("Quantity is:",quantity)
print("Unit price is:",unit_price)
total_amt=quantity*unit_price
print("Total amount is:",total_amt)

# Task 7 — Discount Calculation
# Given: price = 50000
# discount = 10
# Calculate:
# Discount Amount
# Final Price
# Formula:
# Discount Amount = Price × Discount / 100
# Final Price = Price - Discount Amount
price=50000
discount=10
discount_amount=(price*discount)/100
final_price=price-discount_amount
print("\n The Discount amt is:",discount_amount)
print("The final price is:",final_price)

# Task 8 — Data Analyst Salary
# Take the following inputs:
# Employee Name
# Monthly Salary
# Calculate:
# Annual Salary
# Formula:
# Annual Salary = Monthly Salary × 12
Employee_name=input("enter your name:")
Monthly_salary=float(input("Enter your salary:"))
annual_salary=Monthly_salary*12
print("\nThe name is:",Employee_name)
print("The monthly salary is:",Monthly_salary)
print("The annual salary is:",annual_salary)


# 29. Lecture Activity — Real Business Problem
# Scenario
# A company sold 150 laptops at ₹45,000 each. The cost of each laptop was ₹38,000.
# Calculate:Total Revenue
# Total Cost
# Total Profit
# You should identify:
# Quantity = 150
# Selling Price = 45000
# Cost Price = 38000
Selling_price=45000
quantity=150
Cost=38000
Total_cost=Cost*quantity
Total_revenue=quantity*Selling_price
Total_profit=Total_revenue-Total_cost
print("\nThe total cost is:",Total_cost)
print("The total revenue is:",Total_revenue)
print("The total profit is:",Total_profit)

# 30. Homework
# Problem 1
# Create a program that accepts:
# Employee name
# Monthly salary
# Bonus
# Calculate annual income.

Employee_name=input("Enter your name: ")
Monthly_salary=float((input("Enter your monthly salary: ")))
Bonus=float(input("Enter your bonus: "))
yearly_income=Monthly_salary*12
annual_income=yearly_income+Bonus
print("\n The annual income is:",annual_income)

# Problem 2
# Create a program that accepts: Product name
# Quantity
# Price
# Discount %
# Calculate the final bill amount.

product_name=input("Enter the product name:")
quantity=int(input("Enter the quantity:"))
price=float(input("Enter the price:"))
discount=float(input("Enter the discount"))
total_price=quantity*price
discount_amt=(discount*total_price)/100
final_bill=total_price-discount_amt
print("\nThe final bill amount is:",final_bill)


# Problem 3
# A company has: January Sales = ₹50,000
# February Sales = ₹65,000
# March Sales = ₹75,000
# Calculate:
# Total Sales
# Average Sales
# Highest Sales
# Lowest Sales

January_sales=50000
February_sales=65000
March_sales=75000
Total_sales=January_sales+February_sales+March_sales
Average_sales=Total_sales/3
Highest_sales=max(January_sales,February_sales,March_sales)
Lowest_sales=min(January_sales,February_sales,March_sales)
print("\nThe total sales is:",Total_sales)
print("The average sales is:",Average_sales)
print("The highest sales is:",Highest_sales)
print("The lowest sales is:",Lowest_sales)

# 18. Mini Project — Sales Performance Analyzer
# Create a program that accepts:# Sales Amount
# Cost Amount
# Calculate:# Revenue
# Profit
# Profit Percentage
# Performance
# Business Rules
# Condition	Performance
# Sales >= 100000 and Profit >= 20000	Excellent
# Sales >= 75000	Good
# Sales >= 50000	Average
# Otherwise	Poor

sales_amt=float(input("Enter the sales amount:"))
cost_amt=float(input("Enter the cost amount:"))

revenue=sales_amt-cost_amt
profit=revenue
profit_percentage=(profit/sales_amt)*100
if sales_amt>=100000 and profit>=20000:
    performance="Excellent"
elif sales_amt>=75000:
    performance="Good"
elif sales_amt>=50000:
    performance="Average"
else:
    performance="Poor"
print("Sales:",sales_amt)
print("Cost:",cost_amt)
print("Profit:",profit)
print("Revenue:",revenue)
print("Profit percentage:",profit_percentage)
print("Performance:",performance)


# 19. Hands-on Tasks
# Task 1 — Number Classification
# Take a number and determine whether it is:# Positive
# Negative
# Zero
num=float(input("Enter a number:"))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("the number is zero")


# Task 2 — Even or Odd
# Take a number and determine whether it is even or odd. Use %.
num=int(input("Enter a number:"))
if num%2==0:
    print("The value is even")
else:
    print("The value is odd")

# Task 3 — Sales Classification
# Sales	Category
# >= 100000	Excellent
# >= 75000	Good
# >= 50000	Average
# < 50000	Poor

sales=int(input("Enter the value"))
if sales>=100000:
    category="Excellent"
elif sales>=75000:
    category="Good"
elif sales>=50000:
    category="Average"
else:
    category="Poor"
print("The SAles category:",category)

# Task 4 — Profit or Loss
# Take sales and cost and determine profit or loss.

sales=int(input("Enter the sales amount:"))
cost=int(input("Enter the cost amount:"))
if sales>cost:
    profit=sales-cost
    print("The profit is:",profit)
elif sales<cost:
    loss=cost-sales
    print("the loss is:",loss)
else:
    print("no loss,no profit")

# Task 5 — Customer Segmentation
# Purchase	Customer Type
# >= 100000	Premium
# >= 50000	Gold
# >= 25000	Silver
# < 25000	Regular
purchase=int(input("Enter the purchase amount:"))
if purchase>=100000:
    customer_type="Premium"
elif purchase>=50000:
    customer_type="Gold"
elif purchase>=25000:
    customer_type="Silver"
else:
    customer_type="Regular"
print("The customer type is:",customer_type)

# Task 6 — Discount Calculator
# Amount	Discount
# >= 100000	20%
# >= 50000	10%
# >= 25000	5%
# < 25000	0%
# Calculate the final amount.

amount=int(input("Enter the amount"))
if amount>=100000:
    discount="20%"
elif amount>=50000:
    discount="10%"
elif amount>=25000:
    discount="5%"
else:
    discount="0%"
print("The discount amt is:",discount)

# Task 7 — Employee Bonus
# Take employee sales and profit.
# Sales >= 100000 AND Profit >= 20000
# → Bonus Eligible
# Otherwise
# → Not Eligible
employee_sales=int(input("Enter the employee sales:"))
employee_profit=int(input("Enter the employee profit:"))
if employee_sales>=100000 and employee_profit>=20000:
    print("The employee is eligible for bonus")
else:
    print("The employee is not eligible for bonus")

# Task 8 — Data Validation
# Take customer age.
# 18 to 100 → Valid
# Otherwise → Invalid
customer_age=int(input("enter the age"))
if customer_age>=18 and customer_age<100:
    print("It is valid:",customer_age)
else:
    print("It is not valid:",customer_age)

# Task 9 — Student Result
# 90+ → A
# 75–89 → B
# 60–74 → C
# 35–59 → D
# Below 35 → Fail
student_result=int(input("Enter the student marks:"))
if student_result>=90:
    grade="A"
elif student_result>=75:
    grade="B"
elif student_result>=60:
    grade="C"
elif student_result>=35:
    grade="D"
else:
    grade="Fail"
print("The student grade is:",grade)

# Task 10 — Order Validation
# Take quantity and unit price.
# Both must be greater than 0.
# Display Valid Order or Invalid Order.
quantity=int(input("Enter the quantity:"))
unit_price=float(input("Enter the unit price:"))
if quantity>0 and unit_price>0:
    print("Valid order")
else:
    print("Invalid order")

# 20. Challenge Task — Customer Classification
# Take:
# Customer Name
# Purchase Amount
# Number of Orders
# Rules
# Premium:
# Purchase >= 100000 AND Orders >= 10
# Gold:
# Purchase >= 50000 AND Orders >= 5
# Silver:
# Purchase >= 25000
# Regular:
# Everything else
# Display:Customer Name
# Purchase Amount
# Number of Orders
# Customer Segment
customer_name=input("Enter the customer name:")
purchase_amt=float(input("Enter the purchase amount:"))
number_of_orders=int(input("Enter the number of orders:"))
if purchase_amt>=100000 and number_of_orders>=10:
    customer_segment="Premium"
elif purchase_amt>=50000 and number_of_orders>=5:
    customer_segment="Gold"
elif purchase_amt>=25000:
    customer_segment="Silver"
else:
    customer_segment="Regular"
print("Customer Name:", customer_name)
print("Purchase Amount:", purchase_amt)
print("Number of Orders:", number_of_orders)
print("Customer Segment:", customer_segment)
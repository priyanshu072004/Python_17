# Print all numbers from 1 to 50.
for i in range(1,51):
    print(i)

# Print all even numbers between 1 and 100.
for i in range(1,101):
    if i%2==0:
        print(i)

# Calculate the sum of numbers from 1 to 100.
total=0
for i in range(1,101):
    total+=i
    print(total)


# Calculate the total and average of a list of 10 sales values.
sales=[12000, 15000, 18000, 10000, 20000,32000,15000,20000,25000,30000]
total_sales=0
for amt in sales:
    total_sales+=amt
    avg_sales=total_sales/len(sales)
print("Total sales:",total_sales)
print("Average sales:",avg_sales)


# Count how many sales values exceed ₹50,000.
sales=[12000, 15000, 18000, 10000, 20000,32000,15000,20000,55000,30000,55000]
count=0
for amt in sales:
    if amt>=50000:
        count+=1
print("Number of sales:",count)


# Find the highest sales value without using max().
sales=[12000, 15000, 18000, 10000, 20000,32000,15000,20000,25000,30000]
highest_sales=sales[0]
for amt in sales:
    if amt>highest_sales:
        highest_sales=amt
print("Highest sales value:",highest_sales)


# Find the lowest sales value without using min().
sales=[12000, 15000, 18000, 10000, 20000,32000,15000,20000,25000,30000]
lowest_sales=sales[0]
for amt in sales:
    if amt<lowest_sales:
        lowest_sales=amt
print("Lowest sales value:",lowest_sales)


# Count the number of negative values in a list of transactions.
transactions=[-12000, 15000, -18000, 10000, -20000,32000,-15000,20000,-25000,30000]
count=0
for amt in transactions:
    if amt<0:
        count+=1
print("Number of negative transactions:",count)


# Calculate profit for each product using separate sales and cost lists.
sales=[12000, 15000, 18000, 10000, 20000]
cost=[8000, 12000, 15000, 7000, 18000]
for i in range(len(sales)):
    profit=sales[i]-cost[i]
    print("Profit for product",i+1,":",profit)


# Count how many students passed, given a list of marks and a passing score of 35.
marks=[75,23,45,78,12,90,56,34,67,89]
passed=0
for mark in marks:
    if mark>=35:
        passed+=1
print("Number of students who passed:",passed)


# Print customer names from a list, skipping empty strings.
customers=["Alice","Bob","","Charlie","","David"]
for name in customers:
    if name!="":  # Check if the string is not empty
        print(name)


# Use a while loop to display numbers from 10 down to 1.

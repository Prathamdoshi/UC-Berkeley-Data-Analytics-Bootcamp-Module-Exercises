instructions = """
# House Of Pies

## Instructions

# Part 1

* Create an order form that will display a list of pies to the user in the following way:

```
Welcome to the House of Pies! Here are our pies:

---------------------------------------------------------------------
(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
```

* Then prompt the user to select which pie they'd like to order via number.

* Immediately after, follow the order with `Great! We'll have that <PIE NAME> right out for you.` and then ask if they would like to make another order. If so, repeat the process.

* Once the user is done purchasing pies, print the total number of pies ordered.

# Part 2 (Very Challenging!)

* Modify the application once again, this time conclude the user's purchases by listing out the total pie count broken by *each* pie.

```
You purchased:
0 Pecan
0 Apple Crisp
0 Bean
2 Banoffee
0 Black Bun
0 Blueberry
0 Buko
0 Burek
0 Tamale
1 Steak
```
"""



# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0] * 10

# Pie List 
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", 
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

  # Show pie selection prompt 
  print("---------------------------------------------------------------------")
  print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
        " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
        " (9) Tamale, (10) Steak ")

  pie_choice = input("Which would you like? ")

  # Add pie to the pie list by finding the matching index and adding one to its value
  pie_purchases[int(pie_choice)-1] = pie_purchases[int(pie_choice)-1] + 1

  print("------------------------------------------------------------------------")

  # Inform the customer of the pie purchase
  print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")

  # Provide exit option
  shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete 
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
for pie_index in range(len(pie_list)):

  # Gather the count of each pie in the pie list and print them alongside the pies
  print(str(pie_purchases[pie_index]) + " " + str(pie_list[pie_index]))


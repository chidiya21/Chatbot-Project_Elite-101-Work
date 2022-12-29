user = (input(
  "TO QUIT SIMULATION, RESPOND WITH \"QUIT\". TO CONTINTUE, RESPOND WITH \"GO\" "
)).lower()

while user != "quit":
  user = (input(
    "\nHi. Welcome to Chidiya's! How many people do you need a table for? ")
          ).lower()

  print(
    f"\nThat's great. We have an empty table with {user} seats in seating area F. Please follow the signs on site."
  )

  user = (input(
    "\nPlease enter the 6-digit code found on the table to confirm your presence "
  )).lower()

  menu = {
    "1 - French Fries": ' $3.00',
    '2 - Salad': '$5.00',
    "3 - Chicken Burger": '$7.00',
    "4 - Cake": '$10.00'
  }
  menu_two = {"1": '3.00', '2': '5.00', "3": '7.00', "4": '10.00'}

  print(
    f"\nCODE: {user}. TABLE CONFIRMED.\n Thank you. Here is a digital copy of our menu (Dish, Price)\n\n",
    menu)

  user = ((input("\nWould you like to order a dish? (yes/no) ")).lower())

  price = 0.00

  while user != "no":
    user = (input("\n--> What is the number of your chosen dish? "))
    price += float(menu_two[user])
    user = ((
      input("\n--> Would you like to order another dish? (yes/no) ")).lower())

  print(f"\nThe toal price is ${price}. Please play at the counter.")

  break

print("\nTHANK YOU for visiting Chidiya's! Please visit us again.")

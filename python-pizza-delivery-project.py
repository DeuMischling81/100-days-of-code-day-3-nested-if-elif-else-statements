print("Welcome to Python Pizza 🍕 Deliveries 🚚!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni_selection = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese_selection = input("Do you want extra cheese? y or n: ")
pizza_price = 0

if size == "S":
    pizza_price += 15

    if pepperoni_selection == "y":
        pizza_price += 2
    else:
        pizza_price += 0

    if extra_cheese_selection == "y":
        pizza_price += 1
    else:
        pizza_price += 0

    print(f"Alright! Your total price for your pizza is:${pizza_price}.")

elif size == "M":
    pizza_price += 20
    if pepperoni_selection == "y":
        pizza_price += 3
    else:
        pizza_price += 0

    if extra_cheese_selection == "y":
        pizza_price += 1
    else:
        pizza_price += 0

    print(f"Alright! Your total price for your pizza is:${pizza_price}.")

else:
    pizza_price += 25
    if pepperoni_selection == "y":
        pizza_price += 3
    else:
        pizza_price += 0

    if extra_cheese_selection == "y":
        pizza_price += 1
    else:
        pizza_price += 0

    print(f"Alright! Your total price for your pizza is:${pizza_price}.")

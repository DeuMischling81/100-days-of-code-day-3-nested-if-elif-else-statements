print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))
ticket = 0
if height >= 47:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        ticket = 5
        print("Child tickets are $5.")
    elif age <= 18:
        ticket = 7
        print("Youth tickets are $7.")
    else:
        print("Adult tickets are $12.")
        ticket = 12

    wants_picture = input("Do you want a picture? Respond 'y' for yes and 'n' for no: ")
    if wants_picture == "y":
        ticket += 3

    print(f"Your final price is ${ticket}.")

else:
    print("Sorry you have to grow taller before you can ride.")
  

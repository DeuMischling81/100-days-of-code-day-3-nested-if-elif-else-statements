print("Welcome to the 🎢Texas Giant rollercoaster!")
height = int(input("To determine if you can ride, we need to screen your height first.\n"
                   "What is your height in inches? \n"))
ticket = 0

if height >= 47:
    print("Alright! You're tall enough to ride the Texas Giant 🎢")
    age = int(input("I need to know how old you are, to charge you the right price.\n"
                    "How old are you?\n"))
    if age <= 12:
        ticket = 5
        print("Child tickets are $5.00.")

    elif age <= 18:
        ticket = 7
        print("Youth tickets are $7.00.")

    else:
        ticket = 12
        print("Adult tickets are $12.00.")

    wants_picture = input("Do you want to remember this experience with a picture?\nRespond 'y' for Yes or 'n' for No: ")
    if wants_picture == "y":
        ticket += 3

    print(f"Great! Your final admissions prices is: ${ticket}.")
else:
    print("Sorry you have to grow taller before you can ride.")
  

print("Welcome to the Texas Giant rollercoaster!")
height = int(input("To determine if you can ride, we need to screen your height first.\n"
                   "What is your height in inches? \n"))

if height >= 48:
    print("Great! You're tall enough to ride the Texas Giant 🎢")
    age = int(input("I need to know how old you are, to charge you the right price.\n"
                    "How old are you?\n"))
    if age <= 12:
        print("Your price is $5.00.")
    elif age <= 18:
        print("Your price is $7.00.")
    else:
        print("Your price is $12.00.")
else:
    print("Sorry you have to grow taller before you can ride.")

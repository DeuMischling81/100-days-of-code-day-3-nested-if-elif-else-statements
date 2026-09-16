user_number = int(input("Give me a number between 1 and 99: "))

is_it_even = user_number % 2

if is_it_even == 0:
    print("Your number is an EVEN modulo number.")
else:
    print("Your number is an ODD modulo number.")

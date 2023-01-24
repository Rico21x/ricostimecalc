print("Welcome to Rico's Time Table Calculator!")

while True:
    user_input = input("Choose a number between 1 and 10 to use the calculator (or 0 to exit): ")
  #this will print a message which allows the user to access the calculator

   #if the user types 0, the program stops because of the break
    try:
        number = int(user_input)
        if number == 0:
            break
        elif number > 10:
            print("Number must be between  1 and 10 to use the calculator!.")
        else:
            for i in range(1, 11):
              #this is the minimum and maximum range for the calculator to work
                print(f"{number} x {i} = {number*i}")
    except ValueError:
        print("Invalid input, please try again boss.")

import random

Upper_set = False
Lower_set = False
Range_valid = False
Guessed = False
while Range_valid is False:
    while Upper_set is False:
        try:
            upper_bound = int(input("Please choose the upper limit. Only integers are allowed.\n"))
            Upper_set = True
            break
        except:
            print("Invalid upper limit.\n")
            pass

    while Lower_set is False:
        try:
            lower_bound = int(input("Please choose the lower limit. Only integers are allowed.\n"))
            Lower_set = True
        except:
            print("Invalid lower limit.\n")
            pass

    if upper_bound >= lower_bound:
        Range_valid = True
        break

    elif upper_bound < lower_bound:
        Range_valid = False
        Upper_set = False
        Lower_set = False
        print("Sorry, upper limit is lower than lower limit. Please reset range.\n")

value = random.randint(lower_bound, upper_bound)
print(value)

while Guessed is False:
    try:
        guessed_number = int(input("Please guess a number within the range."))

        if guessed_number < value:
            print ("Incorrect. The number is higher.")
        elif guessed_number > value:
            print ("Incorrect. The number is lower.")

        elif guessed_number == value:
            print ("Congratulations! You guessed the number.")
            Guessed = True
    except:
        print("Error.Only integers are allowed.")
        pass

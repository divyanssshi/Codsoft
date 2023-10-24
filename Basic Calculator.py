# Basic Calculator using Python
print("Arithmetic Operation Menu")
print("1. Addition of two numbers  ")
print("2. Subtraction of two numbers")
print("3. Product of two numbers  ")
print("4. Division of two numbers  ")
print("5. Exits")
print()


def Add(num1, num2):  # function for addition
    print(num1+num2)


def Subtract(num1, num2):  # function for subtraction
    print(num1-num2)


def Product(num1, num2):  # function for multiplication
    print(num1*num2)


def Division(num1, num2):  # function for division
    print(num1/num2)


while True:
    # number chosen by user
    choice = int(input("Enter the choice : "))
    # to perform the operation

    if choice == 5:
        print("Exits")  # for exiting the program
        break

    num1 = float(input("Enter the first number : "))  # first number
    num2 = float(input("Enter the second number : "))  # second number

    if choice == 1:
        Add(num1, num2)
        print()
    elif choice == 2:
        Subtract(num1, num2)
        print()
    elif choice == 3:
        Product(num1, num2)
        print()
    elif choice == 4:
        if (num1 == 0) or (num2 == 0):
            print("Not divisible")
        else:
            Division(num1, num2)
        print()
    else:
        print("Enter the correct option")

while True:
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Modulus")
    print("5 Division")
    print("6 Enter q or Q to Exit")

    choice = input("Enter your choice : ")

    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))

    if choice == "1":
        print(num1, "+", num2, "=", (num1+num2))

    elif choice == "2":
        print(num1, "-", num2, "=", (num1-num2))

    elif choice == "3":
        print(num1, "*", num2, "=", (num1*num2))

    elif choice == "4":
        print(num1, "%", num2, "=", (num1%num2))

    elif choice == "5":
        if num2 == 0.0:
            print("Divide by 0 Error")
        else:
            print(num1, "/", num2, "=", (num1/num2))
    else:
        print("Invalid Choice")

    print()
# Prompt user to enter a class method
classmethod = int(input('Enter cm (1, 2, 3): '))

# Prompt user to enter an operation
vas = int(input('Enter op (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): '))

# Check the value of the operation and print the corresponding message
if vas == 1:
    print("op set to addition")
    # Prompt user to enter another class method
    a = int(input('Enter second cm: '))
    result = classmethod + a
    print(f"Result of addition: {result}")
elif vas == 2:
    print("op set to subtraction")
    # Prompt user to enter another class method
    a = int(input('Enter second cm: '))
    result = classmethod - a
    print(f"Result of subtraction: {result}")
elif vas == 3:
    print("op set to multiplication")
    # Prompt user to enter another class method
    a = int(input('Enter second cm: '))
    result = classmethod * a
    print(f"Result of multiplication: {result}")
elif vas == 4:
    print("op set to division")
    # Prompt user to enter another class method
    a = int(input('Enter second cm: '))
    if a != 0:
        result = classmethod / a
        print(f"Result of division: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")




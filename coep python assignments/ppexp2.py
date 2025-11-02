# Step 1: Take input from user
num = int(input("Enter a number: "))


# Step 2: Check if number is positive, negative, or zero
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")


# Step 3: Check if number is even or odd
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
def add_without_plus(x, y):
    while y != 0:
        # Calculate carry
        carry = x & y
        
        # Calculate sum without carry
        x = x ^ y
        
        # Shift carry left by one to add it to x
        y = carry << 1
    
    return x

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function and print the result
result = add_without_plus(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

try:
    num = int(input("Enter an integer: "))
    
    # Check if the input is a non-negative integer
    if num >= 0:
        binary_representation = bin(num)
        print(f"The binary equivalent of {num} is: {binary_representation}")
    else:
        print("Please enter a non-negative integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
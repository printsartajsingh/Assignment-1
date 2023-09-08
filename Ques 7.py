input_string = input("Enter a string: ")
alphabet_count=0
uppercase_count=0
lowercase_count=0
digit_count=0
symbol_count=0
for char in input_string:
        if char.isalpha():
            alphabet_count += 1
            if char.isupper():
                uppercase_count += 1
            else:
                lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
        
print("Number of alphabets:", alphabet_count)
print("Number of digits:", digit_count)
print("Number of symbols:", symbol_count)
print("Number of uppercase alphabets:", uppercase_count)
print("Number of lowercase alphabets:", lowercase_count)
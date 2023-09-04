while True:
    # Input the choice from the user
    choice = int(input("Select your question (1, 2, 3, 4, 5), or enter 0 to exit: "))

    if choice == 0:
        break  # Exit the loop if the user enters 0
    elif choice == 1:
        def convert_Celsius_To_Fahrenheit():
            celsius = float(input("Please enter a Celsius temperature in float format: "))
            fahrenheit = celsius * (9/5) + 32
            res = f"{fahrenheit:.2f}"
            return res

        result = convert_Celsius_To_Fahrenheit()
        print("Celsius to Fahrenheit = " + result)
        print("\n")

    elif choice == 2:
        # Case 2: Find Maximum of Three Integers
        # Input three integers from the user
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        num3 = int(input("Enter the third integer: "))

        # Find the maximum among them using conditional statements
        max_value = num1

        if num2 > max_value:
            max_value = num2

        if num3 > max_value:
            max_value = num3

        print(f"The maximum number is: {max_value}")
        print("\n")

    elif choice == 3:
        # Input an integer from the user
        user_input = int(input("Please enter a number: "))

        # Initialize variables for counting digits, smallest, and highest
        digit_count = 0
        smallest_digit = None
        highest_digit = None

        # Handle the case when the user enters 0 separately
        if user_input == 0:
            digit_count = 1
            smallest_digit = 0
            highest_digit = 0
        else:
            # Find the number of digits, smallest, and highest digits
            while user_input > 0:
                digit = user_input % 10
                digit_count += 1
                if smallest_digit is None or digit < smallest_digit:
                    smallest_digit = digit
                if highest_digit is None or digit > highest_digit:
                    highest_digit = digit
                user_input //= 10  #floor method

        # Print the results
        print(f"Number of digits in the given number is: {digit_count}")
        print(f"Smallest number is: {smallest_digit}")
        print(f"Highest number is: {highest_digit}")
        print("\n")

    elif choice == 4:
        # Function to calculate the sum of numbers from 1 to n
        def calculate_sum(n):
            total = 0
            for i in range(1, n + 1):
                total += i
            return total

        # Input a number from the user
        user_input = int(input("Enter a number: "))

        # Call the function to calculate the sum
        resulting_sum = calculate_sum(user_input)

        # Print the resulting sum
        print(f"The sum of all numbers from 1 to {user_input} is: {resulting_sum}")
        print("\n")

    elif choice == 5:
        # Function to convert decimal to binary
        def decToBinary(dec):
            if dec == 0:
                return '0'
            binary = ''
            while dec > 0:
                binary = str(dec % 2) + binary
                dec //= 2
            return binary


        # Function to convert binary to other bases (binary, octal, hex)
        def binaryToN(bin_num, base_type):
            decimal = 0
            power = 0
            if base_type == 'binary':
                base = 2
            elif base_type == 'octal':
                base = 8
            elif base_type == 'hex':
                base = 16

            for digit in reversed(bin_num):
                decimal += int(digit) * (base ** power)
                power += 1

            if base_type == 'binary':
                return bin(decimal)[2:]
            elif base_type == 'octal':
                return oct(decimal)[2:]
            elif base_type == 'hex':
                return hex(decimal)[2:]

        # Function to convert decimal to octal
        def decToOctal(dec):
            if dec == 0:
                return '0'
            octal = ''
            while dec > 0:
                octal = str(dec % 8) + octal
                dec //= 8
            return octal

        # Function to convert decimal to hexadecimal
        def decToHex(dec):
            if dec == 0:
                return '0'
            hex_chars = '0123456789ABCDEF'
            hex_string = ''
            while dec > 0:
                hex_string = hex_chars[dec % 16] + hex_string
                dec //= 16
            return hex_string


        dec_value = int(input("Enter a decimal number but don't include a floating number: "))
        binary_result = decToBinary(dec_value)
        octal_result = decToOctal(dec_value)
        hex_result = decToHex(dec_value)

        print(f"Decimal to Binary: {binary_result}")
        print(f"Decimal to Octal: {octal_result}")
        print(f"Decimal to Hexadecimal: {hex_result}")

        bin_num = input("Enter a binary number: ")
        type = input("Enter the type of conversion (binary, octal, hex): ")
        converted_result = binaryToN(bin_num, type)
        print(f"{type.capitalize()} to Decimal: {converted_result}")
        print("\n")


    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 0 to exit.")

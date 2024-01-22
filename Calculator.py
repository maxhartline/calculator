def main():

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    #User input
    first_number = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    second_number = float(input("Enter the second number: "))

    #Perform calculation
    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    elif operator == "/":
        result = divide(first_number, second_number)
    else:
        result = "Invalid"

    #Display result to user
    print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()
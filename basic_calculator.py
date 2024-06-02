def main():
    choice()


def choice():
    while True:
        user_choice = (
            input("Wanna learn arithmetic operations? (Yes/No) ").lower().strip()
        )
        if user_choice in ["y", "yes", "1", "true"]:
            user_in_no()
        elif user_choice in ["n", "no", "0", "false"]:
            print("Have a nice day!")
            break
        else:
            print("Invalid input! Kindly enter true or false.")
            # continue
        # break
        print("\n")


def user_in_no():
    while True:
        try:
            m = float(input("Enter the first number: "))
            n = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Enter numeric values!")
            continue
        Operation(m, n)
        break


def Operation(num1, num2):
    while True:
        operation = input("Enter the operator: ").strip()
        if operation in ["+", "-", "*", "/"]:
            result = None
            match operation:
                case "+":
                    result = addition(num1, num2)
                case "-":
                    result = subtraction(num1, num2)
                case "*":
                    result = multiply(num1, num2)
                case "/":
                    result = divide(num1, num2)
            if result is None:
                user_in_no()
            print(f"Result: {result}")
            break
        else:
            print("No operation given! Re-enter.")


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero. Please re-enter the valid numbers.")
        return None
    return num1 / num2


if __name__ == "__main__":
    main()

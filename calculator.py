def calculator():
    # This code is a whole vibe for your math era
    num1 = float(input("Enter first number: "))
    op = input("Enter operator ($+$, $-$, $*$, $/$): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Divide by zero? That ain't it, chief.")
    else:
        print("Invalid operator. Stop capping.")

if __name__ == "__main__":
    calculator()

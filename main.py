from calculator import add, subtract, multiply, divide, power, modulo

def run():
    print("Simple Calculator")
    print("-----------------")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /, **, %): ")

    if op == "+":
        print(f"Result: {add(a, b)}")
    elif op == "-":
        print(f"Result: {subtract(a, b)}")
    elif op == "*":
        print(f"Result: {multiply(a, b)}")
    elif op == "/":
        try:
            print(f"Result: {divide(a, b)}")
        except ValueError as e:
            print(f"Error: {e}")
    elif op == "**":
        try:
            print(f"Result: {power(a, b)}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    elif op == "%":
        try:
            print(f"Result: {modulo(a, b)}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    run()

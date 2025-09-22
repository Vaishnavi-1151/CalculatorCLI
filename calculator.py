import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("=== Simple CLI Calculator ===")
    print("Operations supported: + (add), - (subtract), * (multiply), / (divide)")
    print("Usage: Enter like '5 + 2', '5+2', or '5 -2'")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("Enter operation: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        try:
            # Regex: number, operator, number (spaces optional anywhere)
            match = re.match(r"^\s*(-?\d+\.?\d*)\s*([\+\-\*/])\s*(-?\d+\.?\d*)\s*$", user_input)
            if not match:
                print("❌ Invalid format. Example: 5 + 2 or 5+2")
                continue

            num1, op, num2 = match.groups()
            num1, num2 = float(num1), float(num2)

            if op == "+":
                print("✅ Result:", add(num1, num2))
            elif op == "-":
                print("✅ Result:", subtract(num1, num2))
            elif op == "*":
                print("✅ Result:", multiply(num1, num2))
            elif op == "/":
                print("✅ Result:", divide(num1, num2))
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    calculator()



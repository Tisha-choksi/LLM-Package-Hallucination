from pycalc import Calculator

def run_calculator():
    calc = Calculator()
    while True:
        expression = input("Enter a mathematical expression (or 'exit' to quit): ")
        if expression.lower() == 'exit':
            break
        try:
            result = calc.evaluate(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_calculator()

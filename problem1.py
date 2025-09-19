class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "add":
            result = self.a + self.b
            print("Result:", result)
        elif self.operation == "subtract":
            result = self.a - self.b
            print("Result:", result)
        elif self.operation == "multiply":
            result = self.a * self.b
            print("Result:", result)
        elif self.operation == "divide":
            if self.b == 0:
                print("Error: Division by zero")
            else:
                result = self.a / self.b
                print("Result:", result)
        else:
            print("Error: Invalid operation")

a = 10.0
b = 5.0
operation = "multiply"

calc = Calculator(a, b, operation)
calc.calculate()

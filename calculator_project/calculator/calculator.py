class Calculator:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            raise ValueError("Invalid input types for addition")

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

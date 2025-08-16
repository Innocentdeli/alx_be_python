# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does not need class or instance reference."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Has access to the class (cls)."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


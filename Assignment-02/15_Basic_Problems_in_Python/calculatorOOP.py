
class Calculator:
    def __init__(self, name='Simple'):
        self.name = name
    
    def add(self, a, b):
        return str(a) + " + " + str(b) + ": " + str(a+b)
    
    def subtract(self, a, b):
        return str(a) + " - " + str(b) + ": " + str(a-b)
    
    def multiply(self, a, b):
        return str(a) + " * " + str(b) + ": " + str(a*b)
    
    def divide(self, a, b):
        return str(a) + " / " + str(b) + ": " + str(round(a/b, 3))
    
    def modulo(self, a, b):
        return str(a) + " % " + str(b) + ": " + str(a%b)
    
    def power(self, a, b):
        return str(a) + " ^ " + str(b) + ": " + str(a**b)

a = 7
b = 3
calc = Calculator()
print(calc.add(a, b))
print(calc.subtract(a, b))
print(calc.multiply(a, b))
print(calc.divide(a, b))
print(calc.modulo(a, b))
print(calc.power(a, b))

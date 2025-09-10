# verysimple_calc.py
a = float(input("Число 1: "))
b = float(input("Число 2: "))
op = input("Операция (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b if b != 0 else "❌ На ноль делить нельзя")
else:
    print("Неизвестная операция")

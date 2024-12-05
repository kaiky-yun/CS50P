expression = input("Expression: ")

x, y, z = expression.split(" ")
x = float(x)
z = float(z)
if y == "+":
    calculo = float(x + z)
    print(f"{calculo:.1f}")
elif y == "-":
    calculo = float(x - z)
    print(f"{calculo:.1f}")
elif y == "*":
    calculo = float(x * z)
    print(f"{calculo:.1f}")
elif y == "/":
    calculo = float(x / z)
    print(f"{calculo:.1f}")
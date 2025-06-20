#Math interpreter
exp = input("Expression: ").split(" ")
x,y,z = exp

n1 = float(x)
n2 = float(z)


if y == "+":
   result = n1+n2
elif y == "-":
   result = n1-n2
elif y == "*":
   result = n1*n2
elif y == "/":
   result = n1/n2
print(result)

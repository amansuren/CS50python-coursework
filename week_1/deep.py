"""def main():
    life = input("What is the Answer to the Great Question of life, the universe, and Everything? ").lower().strip()
    if life == "42":
        output("Yes")
    elif life == "forty-two":
        output("Yes")
    elif life == "forty two":
        output("Yes")
    else:
        output("No")
def output(n):
    print(n)

main()
"""
#another way
life = input("What is the Answer to the Great Question of life, the universe, and Everything? ").lower().strip()
if life == "42" or life == "forty-two" or life == "forty two":
    print("Yes")
else:
    print("No")

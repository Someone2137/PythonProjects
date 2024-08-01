import cmath

a = int(input("Enter a positive integer number: "))
if a <= 0:
    raise ValueError("Please enter only positive numbers.")
b = int(input("Enter an integer number: "))
c = int(input("Enter an integer number: "))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    solution1 = ((-b - cmath.sqrt(delta)) / (2 * a)).real
    solution2 = ((-b + cmath.sqrt(delta)) / (2 * a)).real
    print("First solution: ", solution1)
    print("Second solution: ", solution2)
elif delta == 0:
    solution3 = -b / (2 * a)
    print("There is one solution: ", solution3)
elif delta < 0:
    print("There are no real solutions to this equation.")
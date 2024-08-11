a = int(input("Enter the number of elements: "))

l = []

for i in range(1, a+1):
    x = int(input(f"Enter the {i} element: "))
    l.append(x)

print(l)
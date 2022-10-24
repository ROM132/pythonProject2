qus = input("Enter the mex number: ")
if qus.isdigit():
    qus = int(qus)
else:
    print("Pls enter a number next time!")

for i in range(1, qus):
    print(i + 1)


max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)
d = int(input("Enter the number: "))
binary = ''

if d == 0:
    binary = '0'
else:
    while d > 0:
        binary = str(d % 2) + binary
        d = d // 2

print("The binary representation is:", binary)
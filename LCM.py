def LCM(a, b, c):
    largest = max(a, b, c)
    i = 1
    multiple = largest
    while True:
        if multiple % a == 0 and multiple % b == 0 and multiple % c == 0:
            return multiple
        else:
            multiple = largest * i
        i += 1

print(LCM(2, 8, 20))
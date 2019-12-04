words = input('Ведите свою сказку! ')
prepin = ('.',',', '!', '?', '-', ':', ';', '(', ')', '"', "'", ']', '[', '{', '}')
pinani = []
otvet = []

for i in words:
    if i in prepin:
        pinani += i
    elif i != prepin:
        otvet += i

print("Naidennye znaki-" + ''.join(pinani))
print("Slova bez prepinanii - " + ''.join(otvet))
koren = float(input('Enter number: '))
a = 0
x = 0.5 * (1 + koren)
while a * a - abs(koren) > 0.01 or a * a - abs(koren) < -0.01:
   a = 0.5 * (x + koren / x)
   x = a
print(a)

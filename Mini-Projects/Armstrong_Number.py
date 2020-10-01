nu = int(input("Enter a number: "))
sum = 0
x = nu
while x > 0:
   digit = x % 10
   sum += digit ** 3
   x //= 10
if nu == sum:
   print(nu,"is an Armstrong number")
else:
   print(nu,"is not an Armstrong number")

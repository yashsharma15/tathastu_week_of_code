n = int(input("Enter Number:"))
x = 0
b = 1
print ("The Fibonacci series upto",n,"th number is following:")
for i in range (n):
  print(x,end=' ')
  c = x + b
  x = b
  b = c

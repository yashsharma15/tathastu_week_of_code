n = int(input("Enter Number:"))
for i in range (0,n):
  print((str(n-i) + "*") * (n-1-i) + str(n-i))
  if (n-i == 1):
    print (str(n-i))
for i in range (2,n+1):
  print((str(i) + "*") * (i - 1) + str(i))

n = int(input("Enter Number:"))
for i in range (0,n):
  print ("*" * (n-i) + "  " * (i+1) + "*" * (n-1-i) + "*")
  if (n-i == 1):
    print ("*" * 1 + "  " * (i+1) + "*" * 1)
for i in range (2,n+1):
  print ("*" * i + "  " * (n-i+1) + "*" * i)

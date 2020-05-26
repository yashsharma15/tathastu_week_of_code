n = int(input("Enter Number:"))
for i in range (0,n):
  print (" " * i + "*" + "  " * (n-1-i) + "*")
for i in range (0,n):
  print (" " * (n-1-i) + "*" + "  " * i + "*")

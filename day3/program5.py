n = int(input("Enter number of element in list 1:"))
m = int(input("Enter number of element in list 2:"))
l = []
s = []
x = []
for i in range (0,n):
  a = int(input("Enter element in lis1 1:"))
  l.append(a)
for j in range (0,m):
  b = int(input("Enter element in lis1 2:"))
  s.append(b)

for i in l:
  for j in s:
    if (i == j):
      if i not in x:
        x.append(i)

print (x)

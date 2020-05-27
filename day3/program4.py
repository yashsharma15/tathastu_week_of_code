n = int(input("No of elements in list:"))
l = []
for i in range (0,n):
  a = int(input("Enter element in list"))
  if a not in l:
    l.append(a)
 

print (l)

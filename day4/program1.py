n = int(input("Size of Tuple:"))
print ("Enter elements in Tuple:")
l = []
for i in range (0,n):
  a = input("")
  l.append(a)
ar = tuple(l)
e = input("Enter element whose occurraance you want count:")
m = l.count(e)
print ("Number of times tuple contain element is :",m)

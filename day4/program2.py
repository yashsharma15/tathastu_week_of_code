n = int(input("Enter size of list:"))
m = int(input("Enter size of each Tuple :"))
l = []
for i in range (0,n):
  print("Enter elements in Tuple :",i+1)
  T = []
  for j in range (0,m):
    a = int(input("Enter the element"+str(j+1)+":"))
    T.append(a)
  l.append(tuple(T))
p = int(input("Enter the Nth index about which you want to sort the list:"))
l.sort(key = lambda x : x[p])
print ("After sorting tuple list by Nth index sort:",l)

def Sum(l3,b,sum):
  l4 = []
  if (b == 1):
    for x in l3:
      l4.append(sum + x)
    return (l4)
  l5 = list(l3)
  for x in l3:
    l5.remove(x)
    l4.extend(Sum(l5,b-1,sum+x))
  return l4





def summation(l1,a):
  l2 = list(l1)
  for i in range (2,a+1):
    l2.extend(Sum(l1,i,0))
  n1 = 1
  while True:
    if n1 not in l2:
      print ("Least integer not preset in list and cannot be obtained by addition of sub-elements is : ",n1)
      break
    n1 = n1 + 1





n = int(input("Enter number of elements in list :"))
l = []
print ("Enter elements in list :")
for i in range (0,n):
  a = int(input(""))
  l.append(a)
summation (l,n)

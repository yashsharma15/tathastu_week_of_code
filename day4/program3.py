n = int(input("Enter Size of Dictonary:"))
d = dict()
for i in range (0,n):
  k = input("Enter the key for item"+str(i+1)+"in Dictonary:")
  v = int(input("Enter the value for item"+str(i+1)+"in Dictonary:"))
  d[k] = v
print ("The second largest value in Dictonary is:",list(sorted(d.values()))[-2])

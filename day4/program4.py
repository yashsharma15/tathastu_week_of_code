n = int(input("Enter the size of Dictonary:"))
d = dict()
for i in range (0,n):
  k = input("Enter the key  for item"+str(i+1)+"in Dictonary:")
  v = int(input("Enter the value fot item"+str(i+1)+"in Dictonary:"))
  d[k] = v
result = dict()
for k,v in d.items():
  if v not in result.values():
    result[k] = v
print ("Dictonary after removing duplicate elements:",result)

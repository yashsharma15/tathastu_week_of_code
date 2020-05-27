def duplicate(a):
  d = ""
  for i in a:
    if i not in d:
      d = d + i
  return (d)


s = input("Enter String : ")
print ("String after duplicate elements :",duplicate(s))

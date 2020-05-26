def armstrong(a):
  sum1 = 0
  temp = a
  while (temp > 0):
    b = temp % 10
    c = b ** 3
    sum1 = sum1 + c
    temp = temp // 10
  if (a == sum1):
    return True
  else:
    return False

def even(d):
  if (d % 2 == 0):
    return True
  return False

def palindrome(e):
  f=e
  g=0
  while e>0:
    h=e%10
    g=(g*10)+h
    e=e//10
  if(g==f):
    return True
  else:
    return False

def prime(k):
  if (k > 1):
    for i in range (2,k):
      if (k%i == 0):
        return False
        break
    else:
      return True
  else:
    return False


n = int(input("Enter Number:"))
if (even(n)):
  print ("Even Number")
else:
  print ("Odd Number")
if (prime(n)):
  print ("Prime Number")
else:
  print ("Not Prime Number")
if (palindrome(n)):
  print ("Palindrome Number")
else:
  print ("Not Palindrome Number")
if (armstrong(n)):
  print ("Armstrong Number")
else:
  print ("Not Armstrong Number")

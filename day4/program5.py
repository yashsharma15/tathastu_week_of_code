n = int(input("Enter the no of votes: "))

v = []

for i in range(0,n):
  a = input("Enter the name of the Candidate to cast the Vote: ")

  v.append(a)

v1 = []

for name in v:

    v1.append((name, v.count(name)))  

v1.sort(key = lambda x : x[0], reverse = True )

v1.sort(key = lambda x : x[1])

print("The name of the candidate who won the election is", v1[-1][0])

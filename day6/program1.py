def lps(s): 

    n = len(s) 

    L = [[0 for x in range(n)]for y in range(n)] 

    for i in range(n): 

        L[i][i] = 1

    for c in range( 2, n+1): 

        for i in range(n - c + 1): 

            j = i + c - 1

            if (s[i] == s[j] and c == 2): 

                L[i][j] = 2

            elif (s[i] == s[j]): 

                L[i][j] = L[i + 1][j - 1] + 2

            else: 

                L[i][j] = max(L[i][j - 1],L[i + 1][j])

    return L[0][n - 1]

def minimum_Deletions( s): 

    n = len(s) 

    l = lps(s)

    return (n - l) 

s = input("Enter string : ")
print( "Minimum number of deletions : ", minimum_Deletions(s))

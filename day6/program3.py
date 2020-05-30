def segregate(ar, size): 

    j = 0

    for i in range(size): 

        if (ar[i] <= 0): 

            ar[i], ar[j] = ar[j], ar[i] 

            j += 1  

    return j

def find_Missing_Positive(ar, size): 

    for i in range(size): 

        if (abs(ar[i]) - 1 < size and ar[abs(ar[i]) - 1] > 0): 

            ar[abs(ar[i]) - 1] = -ar[abs(ar[i]) - 1] 

    for i in range(size): 

        if (ar[i] > 0): 

            return i + 1

    return size + 1

def find_Missing(ar, size): 

    shift = segregate(ar, size) 

    return find_Missing_Positive(ar[shift:], size - shift)  

ar = [ 0, 10, 2, -10, -20 ] 

arr_size = len(ar)  

missing = find_Missing(ar, arr_size)  

print("The smallest positive missing number is ", missing)

# Prime is prime if it cannot be divided by any number evenly. other than itself and 1.
#i.e., 7, 5, 3.

prime_List = []

for j in range(2,105000):
    j_Prime = True
    for i in range(2,j):
        if j % i == 0:
            j_Prime = False
            break
    if j_Prime == True:
        
        prime_List.append(j)

print(prime_List[10000])

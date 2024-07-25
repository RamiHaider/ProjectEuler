#Problem 4, find the largest Palindrome product of 2 3-digit numbers

import math

palindrome_List = []

for i in range(100,999):
    for j in range(100,999):
        is_Palindrome = True
        v = i*j
        v = str(v)
        for k in range(0,math.floor((len(v)/2))): 
            if v[k] != v[(k*(-1)) - 1]:
                is_Palindrome = False
                break
        if is_Palindrome == True:
            v = int(v)
            palindrome_List.append(v)
palindrome_List.sort()
print(f'{palindrome_List[-1]} is the largest Palindrome product of 2 two-digit #s!')


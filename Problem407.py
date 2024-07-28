# Question is simple: Find the sum of all a values from 1 to 10^7, such that, for i in range of mod n value, find the largest a value s.t. a^2 = a for mod n. For example, we look at n = 3. the only possiblilities are 1 & 2, since a < n. anyways, 1^2 = 1 = 1, so for mod 3, and actually it looks like the default will always be 0. anyways, 2^2 = 4, but in mod 3 it is equal to 1, so a^2 != a in mod 3. Now, we take 1, and we do that check for each number, and then find the sum of them. 

# For each number in range (1-10) find the largest of of that number -1, such that, that number squared 

#Begin at 5, Look at the range from 1 - 5, compute for each value, if i^2 % 5 = i % 5, then save that number, and just do a counter, we can set a flag to 0, and update it if it is the largets number, then do for the next number


addition_of_largest_numbers = 0

for x in range(1,10):
    for i in range(x-1,0,-1):
        if (i * i - i) % x == 0:
            addition_of_largest_numbers += i
            break
print(addition_of_largest_numbers)

##Too inefficient, Despite being as efficient as possible in python
##We need to use another language!!

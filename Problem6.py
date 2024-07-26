#Find the difference between the sum of the squares of the first one hundred
#natural numbers and the square of the sums

sum_Of_Squares = 0

for i in range(1,101):    
    sum_Of_Squares += i**2

sum_Of_Naturals = 0
for i in range(1,101):
    sum_Of_Naturals += i    
square_Of_Sums = sum_Of_Naturals**2

Difference = square_Of_Sums - sum_Of_Squares

print(f'The Square of the Sums is {square_Of_Sums} whilst the sum of the squares is {sum_Of_Squares}, thus, the difference is = {Difference}')

#Problem 500 at Project Euler:

#First step, find the smallest integer number with the given number of divisors, in this case 5

target = 30
divisors = []
a = 10000
b = 1000000
for x in range(a,b):
    divisor_Counter = 0
    divisors = []
    for i in range(1,a+1):
        if x % i == 0:
            divisors.append(i)
            #print(f'{x} % {i} == {x%i}')
            divisor_Counter += 1
            #print({divisor_Counter})
    if divisor_Counter == target:
        break
print(f'{x} has {target} divisors, which are {divisors}')

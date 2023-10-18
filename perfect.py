def is_perfect_number(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    
    if sum(divisors) == n:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")

def check_even_odd(n):
    if n & 1 == 0:
        return "even"
    else:
        return "odd"
    
def check_prime(n):
    is_prime = 0
    for i in range(1,9):
        if nm%i == 0:
            is_prime += 1
    if is_prime >=2:
        print("prime")

nm = int(input("Enter a number: "))
check_prime(nm)

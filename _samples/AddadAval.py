
def is_prime(n):
    aval = True

    for i in range(2,n):
        if n % i == 0:
            aval = False
    return aval

for i in range(1,11):
    if is_prime(i):
        print (i)
def is_prime(num):
    for n in range(2,num):
        if num%n==0:
            return False
    return True


num=80
print(is_prime(num))
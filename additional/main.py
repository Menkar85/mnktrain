import time


def is_prime(n):
    for i in range(2, n//2+1):
        if (not (n % i)):
            return 0
    return 1


num_primes = 0

start_time = time.time()

for i in range(2, 100000):
    num_primes += is_prime(i)

end_time = time.time()

print(num_primes)
print(end_time - start_time)

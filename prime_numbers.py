import math


def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # 1 is not prime
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# # ====== Test Function ======
# for n in range(1, 21):
#     print(n, is_prime_v1(n))


def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # 1 is not prime

    max_divisor = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_divisor):
        if n % i == 0:
            return False
    return True


# # ====== Test Function ======
# for n in range(1, 21):
#     print(n, is_prime_v2(n))

def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 2:
        return True  # 1 is not prime
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_divisor):
        if n % i == 0:
            return False
    return True

# ====== Test Function ======
for n in range(1, 21):
    print(n, is_prime_v2(n))

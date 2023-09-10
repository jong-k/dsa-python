def is_prime_number(n):
    """
    n이 소수인지 판별하는 함수
    :param n: 2이상의 자연수
    :return: boolean
    """
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


print(is_prime_number(4))  # False
print(is_prime_number(7))  # True

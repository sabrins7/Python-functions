def is_prime(num):
    
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


print(f"Does number {5} is prime? {is_prime(5)}")
print(f"Does number {11} is prime? {is_prime(11)}")
print(f"Does number {4} is prime? {is_prime(4)}")
print(f"Does number {30} is prime? {is_prime(30)}")
print(f"Does number {9 } is prime? {is_prime(9)}")






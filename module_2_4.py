numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_number = False
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    for j in range(2, numbers[i]):
        if numbers[i]%j == 0:
            not_primes.append(numbers[i])
            is_number = True
            break
    if not is_number:
        primes.append(numbers[i])
    is_number = False
print(primes)
print(not_primes)
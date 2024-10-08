import random
n = random.randint(3,20)
result = ''
for i in range(1,20):
    for j in range(1,20):
        if i < j:
            if n%(i + j) == 0:
                result = result + str(i) + str(j)
print(result)
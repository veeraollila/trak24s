import time
import random

# Toteutus 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# Toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__ == "__main__":
    n = 10**7
    numbers = [random.randint(1, 100) for _ in range(n)]

    start = time.time()
    result1 = count_even1(numbers)
    endtime = time.time()
    print(f"Toteutus 1 suoritusaika: {endtime - start} sekuntia")

    start = time.time()
    result2 = count_even2(numbers)
    endtime = time.time()
    print(f"Toteutus 2 suoritusaika: {endtime - start} sekuntia")
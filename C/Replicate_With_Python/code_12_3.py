import math


def is_prime(start=101, end=200):
    count = 0
    for i in range(start, end + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        if j >= int(math.sqrt(i)):
            print(i, end=' ')
            count += 1
            if count % 5 == 0:
                print()
    print()
    return 0


if __name__ == '__main__':
    is_prime()
    
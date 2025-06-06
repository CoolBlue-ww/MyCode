def is_prime(start, end):
    count = 0
    for i in range(start, end + 1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        if j == i // 2:
            print(i, end=' ')
            count += 1
            if count % 5 == 0:
                print()
    print()
    return 0

if __name__ == '__main__':
    start, end = 101, 200
    is_prime(start, end)

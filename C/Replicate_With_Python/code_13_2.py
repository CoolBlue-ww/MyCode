def print_num():
    for num in range(100, 1000):
        x = num // 100
        y = num % 100 // 10
        z = num % 100 % 10
        if x ** 3 + y ** 3 + z ** 3 == x * 100 + y * 10 + z:
            print(f"{num} 是水仙花数")
    return


def main():
    print_num()

if __name__ == '__main__':
    main()
def print_num():
    for x in range(1, 10):
        for y in range(0, 10):
            for z in range(0, 10):
                if x ** 3 + y ** 3 + z ** 3 == x * 100 + y * 10 + z:
                    print(f"{x}{y}{z} 是水仙花数")
    return


def main():
    print_num()


if __name__ == '__main__':
    main()

def is_prime(start, end):
    count = 0
    for i in range(start, end + 1):
        mean = (i // 2) + 1
        sign = 0
        for j in range(2, mean):
            if i % j == 0:
                sign += 1
                break
            else:
                continue
        if sign == 0:
            print(i, "是素数")
            count += 1
        if sign == 1:
            continue
    print(f"在{start}到{end}之间共有 {count} 个素数")
    return

is_prime(101, 200)

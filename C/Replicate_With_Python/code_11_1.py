def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if n >= 3:
        temp1, temp2 = 1, 1
        for i in range(3, n + 1):
            temp2, temp1 = temp1 + temp2, temp2
            print(f"第{i}个月的兔子对数为： {temp2}")
        return temp2
    
month = int(input("请输入月份："))
total = fibonacci(month)
print("\n" + "-" * 70)
print(f"第{month}个月后总共有： {total} 对兔子")

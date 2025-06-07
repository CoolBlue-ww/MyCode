def main(input_num):
    print(input_num, end='=')
    for num in range(2, input_num):
        while input_num % num == 0:
            input_num /= num
            if input_num == 1:
                print(num, end='*')
                break
    return 0

if __name__ == '__main__':
    num = int(input('Enter a number: '))
    main(num)
    
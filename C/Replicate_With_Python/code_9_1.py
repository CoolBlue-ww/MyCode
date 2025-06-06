def print_chessboard():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                print(chr(219) * 2, end="  ")
            else:
                print("  " * 2, end="  ")
        print()
    return


if __name__ == '__main__':
    print_chessboard()
def print_chessboard():
    for i in range(8):
        if i == 0 or i == 2 or i == 4 or i == 6:
            for j in range(8):
                if j == 1 or j == 3 or j == 5 or j ==7:
                    print(chr(219), end=" ")
                else:
                    print(" ", end=" ")
            print()
        else:
            for j in range(8):
                if j == 0 or j ==2 or j == 4 or j == 6:
                    print(chr(219), end=" ")
                else:
                    print(" ", end=" ")
            print()
    return


if __name__ == '__main__':
    print_chessboard()
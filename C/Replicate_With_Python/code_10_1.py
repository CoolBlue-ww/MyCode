def print_smFace_with_stair(m, n):
    sm_face = chr(9786)
    stair = chr(9656)
    print(sm_face * m)
    for i in range(3, n + 1):
        print(stair * i)
    return 


if __name__ == '__main__':
    m = int(input("请输入笑脸的个数："))
    n = int(input("请输入楼梯的高度："))
    print_smFace_with_stair(m, n)
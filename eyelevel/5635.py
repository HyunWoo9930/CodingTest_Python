if __name__ == '__main__':
    n = int(input())
    array = [[0 for col in range(4)] for row in range(n)]
    for i in range(n):
        inform = input().split(" ")
        array[i][3] = inform[0]
        array[i][2] = int(inform[1])
        array[i][1] = int(inform[2])
        array[i][0] = int(inform[3])

    array.sort(key=lambda x: (x[0], x[1], x[2]))
    print(array[n-1][3])
    print(array[0][3])
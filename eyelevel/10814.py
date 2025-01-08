if __name__ == '__main__':
    N = int(input())
    array = [[0 for col in range(3)] for row in range(N)]
    for i in range(N):
        a, b = input().split(" ")
        array[i][0] = int(a)
        array[i][1] = b
        array[i][2] = i
    array.sort(key=lambda x: (x[0], x[2]))

    for i in range(N):
        print(str(array[i][0]) + ' ' + str(array[i][1]))

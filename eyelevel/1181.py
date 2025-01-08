if __name__ == '__main__':
    N = int(input())
    array = [[0 for col in range(2)] for row in range(N)]
    for i in range(N):
        word = input()
        array[i][0] = len(word)
        array[i][1] = word
    array.sort(key=lambda x: (x[0], x[1]))
    result = []

    for i in range(N):
        if not result.__contains__(array[i][1]):
            result.append(array[i][1])

    for i in range(len(result)):
        print(result[i])
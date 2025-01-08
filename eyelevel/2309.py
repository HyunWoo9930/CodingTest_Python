def get(s):
    for i in range(8):
        for j in range(i + 1, 9):
            temp = s.copy()
            temp.pop(j)
            temp.pop(i)
            SUM = sum(temp)
            if SUM == 100:
                return temp

if __name__ == '__main__':
    s = []
    for i in range(9):
        a = int(input())
        s.append(a)
    s.sort()
    s = get(s)
    for i in range(7):
        print(s[i])

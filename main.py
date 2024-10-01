x = int(input())
d = [0] * x


def cal(x):
    for i in range(2, x):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            min(d[i], d[i // 5] + 1)
    return d[x]


print(cal(x))

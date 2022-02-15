key = [
    11, 32, 43, 45, 67, 23, 45, 67, 7, 8, 8, 9, 7, 6, 44, 55, 66, 77, 16, 75,
    98, 9, 12, 3, 4, 5, 6, 7, 6, 5, 8, 77, 3, 5, 7, 22, 33, 44, 52, 64,
    75, 82, 98, 107, 113, 125, 4, 32, 99, 122, 11, 32, 43, 45, 67, 23, 45, 67, 7, 8,
    8, 9, 7, 6, 44, 55, 66, 77, 16, 75, 98, 9, 12, 3, 4, 5, 6, 7, 6, 5,
    8, 77, 3, 5, 7, 22, 33, 44, 52, 64, 75, 82, 98, 107, 113, 125, 4, 32, 99, 122,
]


def edcoder(buffer, n):
    lp = int(n / len(key))
    ll = int(n % len(key))
    for i in range(lp):
        base = i * len(key)
        for j in range(len(key)):
            buffer[j + base] ^= key[j]

    base = lp * len(key)
    for i in range(ll):
        buffer[i + base] ^= key[i]


if __name__ == '__main__':
    s = "你好nihao123{}{}{}{}{}{'''''''{}{}{}{nihao1你好1"
    s = s.encode('utf-8')
    print(s)
    p = list(s)

    print(p)
    edcoder(p, len(p))
    edcoder(p, len(p))

    p = bytes(p)
    print(p)
    print(p.decode('utf-8'))

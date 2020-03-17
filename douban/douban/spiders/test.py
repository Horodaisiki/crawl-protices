# # -*- coding: utf-8 -*-
# def test(a=0):
#     while True:
#         if a>0:
#             yield 3
#         else:
#             yield -3
# if __name__ == "__main__":
#     c=test(3)
#     print(next(c))
#     print(c.send(-3))
#     c.close()


def test():
    a=[]
    while True:
        a.append(1)
        b=a.copy()
        for li in range(1, len(a)-1):
            b[li] = a[li-1]+a[li]
        a=b.copy()
        yield b
    return None


if __name__ == "__main__":
    n = 0
    results = []
    for t in test():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

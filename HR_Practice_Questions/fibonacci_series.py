cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    fibo = []
    for i in range(n):
        # return a list of fibonacci numbers
        if i in (0, 1):
            fibo.append(i)
            a = i
        elif i == 2:
            a = 1
            b = 1
            # a ,b = b, a+b
            fibo.append(b)
        else:
            a, b = b, a + b
            fibo.append(b)
    return fibo


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

def print_rangoli(size):
    n = size
    b = ''
    letters = ''
    c = []
    for i in range(n):
        letters += chr(97 + i)
    print(letters)
    for i in letters[::-1]:
        b += "-" + i
        print(b)
        c.append(b + b[:-1][::-1])
        c[-1] = c[-1].strip('-')

    print(c)

    for i in c:
        print(i.center(len(c[-1]), '-'))

    for i in c[::-1][1:]:
        print(i.center(len(c[-1]), '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

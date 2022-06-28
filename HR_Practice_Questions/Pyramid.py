# if __name__ == '__main__':
#     for i in range(1, 11):
#         if i % 2 != 0:
#             i = i * 'H'
#             print(i .center(10))
def print_rangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        print(temp)
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))


n = int(input())
print_rangoli(n)
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = eval(input())
    for i in range(N):
        a, b = input().split(" ")
        try:
            a = int(a)
            b = int(b)
            r = a//b
            print(r)
        except ZeroDivisionError as err:
            print("Error Code: integer division or modulo by zero")
        except ValueError as err:
            print("Error Code:", str(err))
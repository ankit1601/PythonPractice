# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    n = eval(input())
    for i in range(n):
        wrong_cube = False
        inner_n = eval(input())
        if inner_n % 2 != 0:
            inner_n += 1
        stack = []
        d = deque(map(int, input().split()))
        for i in range(inner_n // 2):
            print(i)
            print(d)
            print(stack)
            if len(d) > 1:
                a = d.pop()
                b = d.popleft()
            else:
                a = d.pop()
                b = 0
            # print(a,b)
            # print(stack)
            if not stack:
                a_1 = d[-1]
                b_1 = d[0]
                if a < a_1:
                    print('No')
                    wrong_cube = True
                    break
                else:
                    diff_1 = abs(a - b)
                    diff_2 = abs(a - a_1)
                    diff_3 = abs(b - b_1)
                    if a == b:
                        stack.append(a)
                        stack.append(b)
                    elif diff_1 < diff_2 and diff_1 < diff_3:
                        if a > b:
                            stack.append(a)
                            stack.append(b)
                        else:
                            stack.append(b)
                            stack.append(a)
                    elif diff_2 > diff_1 and diff_2 > diff_3:
                        d.appendleft(b)
                        b = d.pop()
                        if a > b:
                            stack.append(a)
                            stack.append(b)
                        else:
                            stack.append(b)
                            stack.append(a)
                    else:
                        d.append(a)
                        a = d.popleft()
                        if a > b:
                            stack.append(a)
                            stack.append(b)
                        else:
                            stack.append(b)
                            stack.append(a)



            else:
                top = stack[-1]
                # print(d)
                if d:
                    a_1 = d[-1]
                    b_1 = d[0]
                    if a_1 > top or b_1 > top:
                        print('No')
                        wrong_cube = True
                        break
                if a > top or b > top:
                    print('No')
                    wrong_cube = True
                    break
                elif d:
                    # print(d)
                    a_1 = d[-1]
                    b_1 = d[0]
                    diff_1 = abs(a - b)
                    diff_2 = abs(a - a_1)
                    diff_3 = abs(b - b_1)
                    if diff_1 < diff_2 and diff_1 < diff_3:
                        if a > b:
                            stack.append(a)
                            stack.append(b)
                        else:
                            stack.append(b)
                            stack.append(a)
                    elif diff_2 > diff_1 and diff_2 > diff_3:
                        d.appendleft(b)
                        b = d.pop()
                        if a > b:
                            stack.append(a)
                            stack.append(b)
                        else:
                            stack.append(b)
                            stack.append(a)
                    else:
                        d.append(a)
                        a = d.popleft()
                        if a > b:
                            stack.append(a)
                            stack.append(b)
                        else:
                            stack.append(b)
                            stack.append(a)
                else:
                    # print('here')
                    if a > b:
                        stack.append(a)
                        stack.append(b)
                    else:
                        stack.append(b)
                        stack.append(a)
        if not wrong_cube:
            print('Yes')
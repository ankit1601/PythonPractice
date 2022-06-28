n = int(input())
s = set(map(int, input().split()))
number_of_commands = eval(input())

for _ in range(number_of_commands):
    operation_list = input().split()
    operation = operation_list[0]
    if len(operation_list) == 2:
        value = int(operation_list[-1])
    if operation == 'pop':
        s.pop()
    elif operation == 'remove':
        s.remove(value)
    elif operation == 'discard':
        s.discard(value)
print(sum(s))
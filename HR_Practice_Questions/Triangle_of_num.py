for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * pow(10, i) // 9)

for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(pow(pow(10, i) // 9, 2))
# if i==1:
#     print(i)
#     prev = 1
# else:
#     multiplier = pow(10,i-1)+prev
#     print(i*multiplier)
#     prev = multiplier

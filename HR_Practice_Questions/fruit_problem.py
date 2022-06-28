"""
Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation

BANANA FRIES: Quantity bought:
, Price:
Net Price:
POTATO CHIPS: Quantity bought: , Price:
Net Price:
APPLE JUICE: Quantity bought: , Price:
Net Price:
CANDY: Quantity bought: , Price:
Net Price:
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = eval(input())
price_fruit = OrderedDict()
for _ in range(N):
    word_list = input().split()
    # print(word_list)
    price = int(word_list[-1])
    if len(word_list) > 2:
        word_list.pop()
        word_ = " ".join(word_list)
    else:
        word_ = word_list[0]
    if price_fruit.get(word_):
        price_fruit[word_] += price
    else:
        price_fruit[word_] = price

for i, v in price_fruit.items():
    print(f'{i} {v}')


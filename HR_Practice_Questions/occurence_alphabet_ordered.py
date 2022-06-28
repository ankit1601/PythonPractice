"""
Here we try to find out occurence of alphabet in ordered manner
"""
from collections import OrderedDict, Counter

string = "abdjhjdffjkflfdkfdhhfhfhgdfjdjfkvdbdghfbndkfhkfhdmnfbdklfhkdghfkjdfhldfh"

str_occ_dict = {}

for i in string:
    if i.isalpha():
        if str_occ_dict.get(i):
            str_occ_dict[i] = str_occ_dict.get(i)+1
        else:
            str_occ_dict[i] = 1

new_dict = OrderedDict(sorted(str_occ_dict.items()))
sorted_dict = dict(sorted(str_occ_dict.items()))
print(str_occ_dict)
print(new_dict)
print(sorted_dict)
print(Counter(string))
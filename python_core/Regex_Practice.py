"""
Regex are used to perform following operations
Matching strings: match only if expression found match at beginning
Search strings:  search anywhere in the string and group first occurrence
Findall strings: search all including duplicate in the string
Replace: replace string with sub matched by regex
"""

import re
prog = re.compile(r'm\w\w')
# return all the occurrence of regex
str1 = 'mat rat mat fat maa mrrmt my'
print(prog.findall(str1))
# Search anywhere in the string and return first match
str2 = "hello this is op format for metix"
res = prog.search(str2)
print(res.group())

# Return only if match found in the beginning
print(prog.match(str1).group())

# Split using regex
# Capital W represent all non alphanumeric character
print(re.split(r'\W', str1))
print(re.split(r'\w', str1))

# Regex can also be used to replace the string with sub string matched by regex
# sub(regex, new string, string)
str3 = 'Kumbhmela will be cinducted at Delhi in India'
res = re.sub(r'cin', 'con', str3)
print(res)

res = re.findall(r'a[\w]*', str3) # it will return word with a start, it will not consider spaces
res1 = re.findall(r'\ba[\w]*\b', str3)
print(res)
print(res1)


# word starting with numeric and end with anything
res2 = re.findall(r'\d[\w]*', "hello i am 1st and 2nd in th2is org")
print(res2)

res2 = re.findall(r'\b\d[\w]*\b', "hello i am 1st and 2nd in th2is org")
print(res2)


# find all word having 5 character length
res3 = re.findall(r'\b[\w]{5}\b', "hello how are you what are you doing")
print(res3)

# search first matching word with length 5
res3 = re.search(r'\b[\w]{5}\b', "hello how are you what are you doing")
print(res3.group())


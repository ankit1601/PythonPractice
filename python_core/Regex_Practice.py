"""
Regex are used to perform following operations
Matching strings: match only if expression found match at beginning
Search strings:  search anywhere in the string and group first occurrence
Findall strings: search all including duplicate in the string
Replace: replace string with sub matched by regex

Characters in Regular Expression
\d: Reperesnts any digit 0-9
\D: Represent any non-digit
\s: Represent while space e.g \t\n\r\f\v
\S: Represent non while space character
\w: Represent any alphanumeric (A to Z, a to z, 0 to 9)
\W: Represent any non alphanumeric character
\b: Represent space around word
\A: Match only at start of the string
\Z: Match only at end of the string

Quantifiers in Regex
+ : 1 or more repetition of the preceding regex
*: 0 or more repetition of preceding regex
?: 0 or 1 repetition of preceding regex
{n}: exactly n occurrences
{m, n}: exactly m to n occurrences, m by defaults 0 and n by default infinity [like range both inclusive if given]

Special Characters in Regex
'\' : Escape special character
'.' : Matched any character except new line
'^' : Matches beginning of a string
'$' : Matches end of a string
[...]:Denotes set of possible characters, Ex: [6b-d] matches any character '6','b','c','d','6'
{...}:Matches regex inside the parentheses and the result can be captured
R1|R2 : Matches either Regex R1 or R2
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

res = re.findall(r'a[\w]*', str3)  # it will return word with a start, it will not consider spaces
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

# find all words having atleast length 4
res4 = re.findall(r'\b[\w]{4,}\b', 'hello how are you what are you doing')
print(res4)

# find all the words having at least 3 and at most 5 length
res5 = re.findall(r'\b\w{3,5}\b', "hi how are you what are you doing")
print(res5)

# find only single digit from a string
res6 = re.findall(r'\b\d\b', "i thin 1 or 2 both are prime and natural numbers")
print(res6)

# find last word of the string if it starts with t
res7 = re.findall(r'\bt[\w]*\Z', "i want that")
print(res7)

# find phone number of a person in a given string
res8 = re.findall(r'\d+', "My mobile number is 9999999999")
print(res8)

# example find non digit characters
res8 = re.findall(r'\D+', "My mobile number is 9999999999 one")
print(res8)

# find all words starting with an or ak
res9 = re.findall(r'\ba[nk][\w]*\b', "ankit anant akash at least listen to ajay")
print(res9)

# find out all the dates included in the string
res10 = re.findall(r'\d{2}-\d{2}-\d{4}', 'hello my joining was 10-09-2018 but you wrote 10-09-2011')
print(res10)

res11 = re.search(r'^He', "Hello World")
print(res11.group())

res12 = re.search(r'rld$', " Hello World")
print(res12.group())

res12 = re.search(r'rld$', " Hello WORLD", re.IGNORECASE)  # regex is case sensitive hence to ignore case
print(res12.group())

# Python program to retrieve marks and names from given string
str10 = 'Rahul got 75 marks, Vijay got 80 marks but Subbhu got 85 marks'
marks = re.findall(r'\d{2,}', str10)
print(marks)

names = re.findall(r'[A-Z][a-z]*', str10)
print(names)

both = re.findall(r'\d{2,}|[A-Z][a-z]*', str10)  # using or in regex
print(both)

# write regex to find time in am and pm in given string
str11 = 'Meeting may be at 10am 9am 4pmm 5pm'
times = re.findall(r'\d{1,2}am|\d{1,2}pm', str11)
print(times)

# find out the email ids in given string
str12 = " Mr Ajay can be contacted at ajay.gupta@gmail.com if not reachable then you can contact samay123@gmail.com " \
        "and sachingupta@neo.org"
emails = re.findall(r'[A-Za-z0-9]+\.?[A-Za-z0-9]+@[A-Za-z0-9]+\.com', str12)
print(emails)

emails = re.findall(r'\S+@\S+', str12)
print(emails)

with open('records.txt') as f:
    with open('salary.txt', 'w') as f2:
        for line in f:
            employee_id = re.search(r'\d+', line)
            salary = re.search(r'\d+\.\d+', line)
            f2.write(employee_id.group() + '\t' + salary.group() + '\n')

# Retrieving the information from HTML file using regular expression
str13 = "<div><p><i></i></p></div>"
all_elements = re.findall(r'<[a-z]+>', str13)
all_elements_end = re.findall(r'</[a-z]+>', str13)
print(all_elements)
print(all_elements_end)


expression = r'(?=ANA)'
print(re.findall(expression, 'BANANA'))


print(re.findall(r'\b\|\|\b', "a || b"))

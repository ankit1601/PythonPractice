# weekdays = {1: 'sun', 2: 'mon', 3: 'tue', 4: 'wed', 5: 'thu', 6: 'fri', 7: 'sun', 8: 'mon', 9: 'mon'}

weekdays = {1: 'sun', 2: 'mon', 6: 'fri', 7: 'sun', 8: 'mon', 9: 'mon', 3: 'tue', 4: 'wed', 5: 'thu'}

# de duplicate the values keeping the keys intact
temp_dict = {}
keys = list(weekdays.keys())

for key in keys:
    if temp_dict.get(weekdays[key]):
        weekdays.pop(key)
    else:
        temp_dict[weekdays[key]] = key
print(weekdays)

# Four cors and 20 user, and API would take around 3 hrs for each user and we need to return results after 30 mns
# Workers
# Multiprocessing
# Threads

# flask framework
# Six month inside the project
# Project
# unit testing
# code coverage
# integrate swagger with Python automatically

# Automatically generate Swagger Documentation.
# Owner of the product
# Requirement would be coming from team/ Looking for Contributor/Owner





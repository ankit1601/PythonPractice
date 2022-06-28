# Enter your code here. Read input from STDIN. Print output to STDOUT
from calendar import Calendar
from datetime import datetime

if __name__ == '__main__':
    date = input()
    # print(date)
    date_formatted = datetime.strptime(date, '%m %d %Y')
    if date_formatted.isocalendar()[2] == 1:
        print('MONDAY')
    elif date_formatted.isocalendar()[2] == 2:
        print('TUESDAY')
    elif date_formatted.isocalendar()[2] == 3:
        print('WEDNESDAY')
    elif date_formatted.isocalendar()[2] == 4:
        print('THURSDAY')
    elif date_formatted.isocalendar()[2] == 5:
        print('FRIDAY')
    elif date_formatted.isocalendar()[2] == 6:
        print('SATURDAY')
    else:
        print('SUNDAY')


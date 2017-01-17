"""
Program that prints a 12 month calendar for the year entered by the user.
Creates a text file for output corresponding to year number.
Supports leap years.
"""
import math

# Dictionary to store month and it's corresponding amount of days
MonthNum = {'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31}


def findjan1(year):
    """
    Calculates which day January 1st falls on any given year
    :param year: Desired year given by the user
    :return: Returns the day with Sunday corresponding to 0, Monday 1, etc.
    """
    date = (year + math.floor((year-1)/4) - math.floor((year-1)/100) + math.floor((year-1)/400)) % 7
    return date


def isleap(year):
    """
    Calculates if a year is a leap year or not, changes amount of days if true
    :param year: Desired year given by the user
    :return: Returns true(1) if the year is a leap year. Returns false(2) if not. Changes amount of days in Feb.
    """
    if year % 4 == 0 and year % 100 != 0:
        MonthNum['February'] = 29
        return 1
    elif year % 400 == 0:
        MonthNum['February'] = 29
        return 1
    else:
        return 0

# Prompt user for input
inputYear = input('Please enter year: ')
# Calculates if leap year
isleap(int(inputYear))
# Calculates Jan 1 to base calendar off of
jan1 = findjan1(int(inputYear))
# Create output file and name
fileName = 'calendar' + inputYear + '.txt'
output = open(fileName, 'w')
# For loop for each month in dictionary
for month in MonthNum:
    outputString = '       ' + month + ' ' + inputYear + '\nSun Mon Tue Wed Thu Fri Sat\n'
    output.write(outputString)
    # Print offset depending on what day Jan 1 falls on
    for e in range(jan1):
        output.write('    ')
    # Print out the day numbers, prints new line after Saturdays to wrap numbers
    for i in range(1, MonthNum[month]+1):
        if jan1 % 7 == 0 and i != 1:
            output.write('\n')
        # Formatting if number is 1 or 2 characters in length
        if i < 10:
            outputString = '  ' + str(i) + ' '
        else:
            outputString = ' ' + str(i) + ' '
        output.write(outputString)
        jan1 += 1
    output.write('\n\n')
    jan1 %= 7
output.close()

number = int(input('Enter a day number: '))
week_days = {1: 'Monday',
             2: 'Tuesday',
             3 : 'Wednesday',
             4: 'Thursday',
             5: 'Friday',
             6: 'Saturday',
             7: 'Sunday'}
if number in week_days:
    print(number, '-', week_days[number])
else:
    print('Sorry, that day does not exist')

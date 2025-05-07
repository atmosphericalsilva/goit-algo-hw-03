from datetime import datetime, timedelta
from random import randint

# first task:
def get_days_from_today(user_input):

    current_date = datetime.now()

    # turning string input into a date:
    user_date = datetime.strptime(user_input, '%Y-%m-%d')

    # calculating the difference and printing the result:
    difference = current_date - user_date
    print(f'this date was {difference.days} days ago')

# second task:
def get_numbers_ticket(min, max, quantity):

    ticket_nums = set()

    # checking the requirements:
    if min > 0 and max < 1001:

        # adding unique numbers until the set is filled:
        while len(ticket_nums) != quantity:
            ticket_nums.add(randint(min, max))
        print(sorted(list(ticket_nums)))   
    else:
        print(list(ticket_nums))

# first task call:
get_days_from_today(user_input = input('input your date (Y-m-d): '))

# second task call:
get_numbers_ticket(min = int(input('min: ')), max = int(input('max: ')), quantity = int(input('quantity: ')))
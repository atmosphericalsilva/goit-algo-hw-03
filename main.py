from datetime import datetime, timedelta
from random import randint

# first task:
def get_days_from_today(user_input):

    current_date = datetime.today()

    try:
        # turning string input into a date:
        user_date = datetime.strptime(user_input, '%Y-%m-%d')

        # calculating the difference and printing the result:
        difference = current_date - user_date
        return difference.days
    
    # error handle:
    except ValueError:
        return None

# second task:
def get_numbers_ticket(min_str, max_str, quantity_str):

    ticket_nums = set()

    try:
        
        # turning string into integer
        min = int(min_str)
        max = int(max_str)
        quantity = int(quantity_str)

        delta = max - min

        # checking the requirements:
        if min > 0 and max < 1001 and max >= min and quantity <= delta + 1:

        # adding unique numbers until the set is filled:
            while len(ticket_nums) != quantity:
                ticket_nums.add(randint(min, max))
            return sorted(list(ticket_nums))
        else:
            return list(ticket_nums)
        
    # correct format check:
    except ValueError:
        return None

# first task call:
print(get_days_from_today(user_input = input('input your date (Y-m-d): ')))

# second task call:
print(get_numbers_ticket(min_str = input('min: '), max_str = input('max: '), quantity_str = input('quantity: ')))
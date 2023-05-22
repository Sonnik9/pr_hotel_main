# import datetime

# date_str = '23 april 2023'
# date_obj = datetime.datetime.strptime(date_str, '%d %B %Y')
# date_formatted = date_obj.strftime('%Y-%m-%d')

# print(date_formatted) # 2023-04-23

# python testTime.py

# import dateparser
# from faker import Faker

# def transform_date(date_string):
#     # Parse the date string using dateparser
#     parsed_date = dateparser.parse(date_string, languages=['en', 'ru'])
#     # Format the date in the desired format
#     transformed_date = parsed_date.strftime('%Y-%m-%d')

#     return transformed_date

# # Example usage
# date_en = '23 April 2023'
# date_ru = '23 Апреля 2023'

# transformed_date_en = transform_date(date_en)
# transformed_date_ru = transform_date(date_ru)

# print(transformed_date_en)  # Output: 2023-04-23
# print(transformed_date_ru)  # Output: 2023-04-23



# def generate_fake_time():
#     fake = Faker()
#     fake_time = fake.time(pattern='%H:%M:%S')
#     return fake_time

# # Example usage
# fake_time = generate_fake_time()
# print(fake_time) 

# from datetime import datetime, timedelta
# from random import randint



# def generate_fake_dates(date_string):
#     # Convert the input date string to a datetime object
#     base_date = datetime.strptime(date_string, '%Y-%m-%d')

#     # Subtract a random number of days between 3 and 12 from the base date
#     subtract_days = randint(3, 12)
#     checkin_date = base_date - timedelta(days=subtract_days)

#     # Calculate the remaining days between the check-in date and the base date
#     remaining_days = (base_date - checkin_date).days

#     # Add a random number of days between 1 and the remaining days to the check-in date
#     add_days = randint(1, remaining_days)
#     checkout_date = checkin_date + timedelta(days=add_days)

#     # Format the dates as strings in the desired format
#     checkin_date_str = checkin_date.strftime('%Y-%m-%d')
#     checkout_date_str = checkout_date.strftime('%Y-%m-%d')

#     return checkin_date_str, checkout_date_str

# # Example usage
# base_date_str = '2023-04-07'
# checkin, checkout = generate_fake_dates(base_date_str)
# print(f'Check-in: {checkin}')
# print(f'Check-out: {checkout}')


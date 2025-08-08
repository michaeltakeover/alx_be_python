from datetime import datetime, timedelta
date_now = datetime.now()

def display_current_datetime():
    date_now = datetime.now()
    formatted_date = date_now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_date)
    return date_now

number_of_days = int(input("Enter the number of days: "))
def calculate_future_date(date_now, number_of_days):
    future_date = date_now + timedelta(days=number_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date: ", formatted_future)
    return future_date

now = display_current_datetime()
calculate_future_date(now, number_of_days)
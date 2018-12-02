import datetime

def day_of_month():
    """Return day of month"""
    
    return datetime.datetime.today().day 


def day_of_week():
    """Return day of week"""

    return datetime.date.today().weekday
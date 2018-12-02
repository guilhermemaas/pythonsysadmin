import datetime

#Use this methods in work_queue, to determinate the conditions where the emails should be sent.

def day_of_month():
    """Return day of month"""
    
    return datetime.datetime.today().day 


def day_of_week():
    """Return day of week"""

    return datetime.datetime.today().weekday


def day_of_year():
    """Return current year"""

    return datetime.datetime.today().year


def date_time():
    """Return current date and time: yy-mm-dd hh:mm:ss:ms"""

    return datetime.datetime.today()
import datetime
from dateutil import parser
from datetime import datetime
from sqlalchemy import *


def convert_datetime_to_string_and_parse_object(form_date: str) -> list:
    """
    Converts datetime object to string and parse object to list.
    Blank spaces are removed to create a list of strings / integers.
    
    Returns a list of integers and strings.
    """
    try:
        get_date = datetime.strptime(form_date, "%Y-%m-%dT%H:%M")
        get_date = get_date.strftime('%c')
        formatted_date = get_date.split(' ')
        # formatted_form_date = form_date.strftime("%c")
        return formatted_date, get_date
    except Exception as e:
        return [str(e)]
    
    
def convert_string_date_to_datetime_date_object_str(string_date: str) -> tuple:
    """
    Converts a date string into a datetime object.
    Function parses the string and converts into datetime object.
    The datetime object is then formatted using strftime and split into a list.
    
    Returns Day, Month, Date, Year in list.
    """
    try:
        # pasre the string into datetime object
        parse_date = parser.parse(string_date)
        # format the result to - Day, Month, Date, Time, Year
        format_datetime = parse_date.strftime('%c')
        # split datetime into separate objects
        datime_list = format_datetime.split(' ')
        # get the date from the list
        form_date = datime_list[2]
        return (form_date[0], form_date[2], form_date[1], form_date[4])
    except Exception as e:
        return {'Error': str(e)}

def convert_string_time_to_datetime_time_object_str(string_time: str) -> str:
    """
    Converts a time string into a datetime object.
    Function parses the string and converts into datetime object.
    The datetime object is then formatted using strftime and split into a list.
    
    Returns time from list index.
    """
    try:
        parse_time = parser.parse(string_time)
        format_datetime = parse_time.strftime('%c')
        # format the result to - Day, Month, Date, Time, Year
        datetime_list = format_datetime.split(' ')
        form_time = datetime_list[3]
        return form_time
    except Exception as e:
        return {'Error': str(e)}
    
    
def convert_string_date_and_time_to_datetime_object(date_obj: list, time_obj: str) -> str:
    """
    Converts date & time string into a datetime object.
    Function parses the string and coverts into datetime object.
    The datetime object is then formatted using strftime and converted into a list.
    
    Returns datetime string
    """
    try:
        day = date_obj[0]
        month = date_obj[1]
        date = date_obj[2]
        year = date_obj[4]
        parse_date = parser.parse(f'{day} {date} {month} {year} {time_obj}')
        format_date = parse_date.strftime('%c')
        formatted_date = str(format_date)
        return formatted_date
    except Exception as e:
        return {'Error': str(e)}
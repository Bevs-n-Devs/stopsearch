import datetime
from sqlalchemy import *


def convert_datetime_to_string_and_parse_object(form_date: datetime) -> list:
    """
    Converts datetime object to string and parse object to list.
    Blank spaces are removed to create a list of strings / integers.
    
    Returns a list of integers and strings.
    """
    try:
        formatted_form_date = form_date.strftime("%c")
        return formatted_form_date
    except Exception as e:
        return [str(e)]
    
    

import datetime
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
    
    

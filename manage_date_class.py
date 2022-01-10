from datetime import date, datetime, timedelta
import re
from unidecode import unidecode


class Manage_Date:

    @staticmethod
    def str_to_date(string_date):
        if isinstance(string_date, str):
            if unidecode(string_date.lower()) == "amanha":
                return Manage_Date.date_to_str(Manage_Date.next_day())
            elif string_date.lower() == "hoje":
                return Manage_Date.date_to_str(Manage_Date.today())

            list_date = [int(element) for element in re.split('-|/', string_date)]
            list_date.reverse()
            return datetime(*list_date)
        elif isinstance(string_date, datetime):
            string_date2 = Manage_Date.date_to_str(string_date)
            return Manage_Date.str_to_date(string_date2)

    @staticmethod
    def date_to_str(date):
        if isinstance(date, datetime):
            return format(date.day, '02d')+'/'+format(date.month, '02d')+'/'+format(date.year, '04d')
        elif isinstance(date, str):
            date = Manage_Date.str_to_date(date)
            return format(date.day, '02d')+'/'+format(date.month, '02d')+'/'+format(date.year, '04d')

    @staticmethod
    def next_day():
        return datetime.now() + timedelta(1)

    @staticmethod
    def today():
        return datetime.now()



    
class Manage_Date:

    @staticmethod
    def convert_date(str_or_date):
        '''Identify and convert string to datetime or datetime to string'''
        if isinstance(str_or_date, str):
            return Manage_Date.str_to_date(str_or_date)
        elif isinstance(str_or_date, datetime):
            return Manage_Date.date_to_str(str_or_date)
        else:
            raise TypeError('Formato não suportado. Utilizar datetime ou str.')


    @staticmethod
    def str_to_date(string_date):
        if unidecode(string_date.lower()) == "amanha":
            return Manage_Date.next_day()
        elif string_date.lower() == "hoje":
            return Manage_Date.today()
        else:
            try:
                list_date = [int(element) for element in re.split('-|/', string_date)]
                list_date.reverse()
                return datetime(*list_date)
            except ValueError:
                raise Exception("[!] A data está incorreta ou o formato não é suportado, use apenas números e barras.")

    @staticmethod
    def date_to_str(date):
        return format(date.day, '02d')+'/'+format(date.month, '02d')+'/'+format(date.year, '04d')

    @staticmethod
    def next_day():
        return datetime.now() + timedelta(1)

    @staticmethod
    def today():
        return datetime.now()



from datetime import date, datetime, timedelta
import re
from typing import Type
from unidecode import unidecode
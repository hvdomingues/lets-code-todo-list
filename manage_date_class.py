from datetime import date, datetime, timedelta
import re


class Manage_Date:

    @staticmethod
    def str_to_date(string_date):
        list_date = [int(element) for element in re.split('-|/', string_date)]
        list_date.reverse()
        return datetime(*list_date)

    @staticmethod
    def date_to_str(date):
        return format(date.day, '02d')+'/'+format(date.month, '02d')+'/'+format(date.year, '04d')

    @staticmethod
    def next_day():
        return datetime.now() + timedelta(1)

    @staticmethod
    def today():
        return datetime.now()



    
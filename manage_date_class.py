from datetime import date, datetime, timedelta


class manage_date:

    @staticmethod
    def str_to_date(string_date):
        pass

    @staticmethod
    def date_to_str(date):
        return format(date.day, '02d')+'/'+format(date.month, '02d')+'/'+format(date.year, '04d')

    @staticmethod
    def check_str_date(str_date):
        pass

    @staticmethod
    def next_day():
        return datetime.now() + timedelta(1)

    


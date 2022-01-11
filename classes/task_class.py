class Task:
    
    __status_dict = {0:"Pendente", 1:"Concluído"}

    def __repr__(self):
        if hasattr(self, 'date'):
            return f"{self.title} {self.date}"
        else:
            return f"{self.title}"

    def __init__(self, title, date=None, category=None, status = 'Pendente'): #category é salva como int, status é salvo como str

            self.title = title
            self.date = Task.check_date(date)
            self.category = Task.check_category(category)
            self.status = Task.check_status(status)

    
    @staticmethod
    def check_date(date):
        if date == None:
            return None
        elif isinstance(date, datetime):
            return Manage_Date.convert_date(date)
        elif isinstance(date, str):
            return Manage_Date.convert_date(Manage_Date.str_to_date(date))
        else:
            return Manage_Date.convert_date(date)
            
    @staticmethod
    def check_category(category):
        if category == None:
            return category
        elif isinstance(category, str):
            return Category.find_code(category)
        elif isinstance(category, int):
            return Category.check_code(category)
        else:
            raise TypeError("O tipo da categoria não é válido. Utilize o código ou o nome por extenso.")

    @staticmethod
    def check_status(status):
        if isinstance(status, str):
            if status in ('Pendente', 'Concluído'):
                return status
            else:
                raise KeyError("O Status digitado não está correto. Digite 'Pendente' ou 'Concluído'")
        elif isinstance(status, int):
            if status in (0,1):
                return Task.__status_dict[status]
            else:
                raise KeyError("Código do status incorreto, possíveis: 0 ou 1.")
        else:
            raise TypeError("O tipo do status está errado. Tipos permitidos, int ou str.")


from datetime import datetime
from os import stat
from typing import Type
import pandas as pd
from classes.manage_csv_class import Manage_Csv
from classes.category_class import Category
from classes.manage_date_class import Manage_Date
from classes.task_list_class import Task_List

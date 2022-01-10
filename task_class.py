from datetime import datetime
import pandas as pd
from manage_csv_class import Manage_Csv
from category_class import Category
from task_list_class import Task_List

class Task:

    __path = 'task_list.csv'
    
    def __init__(self, title, date=None, category=None, status = 'Pendente'):
        self.title = title
        self.date = date
        self.category = category
        self.status = status

    def __repr__(self):
        return f"{self.title} {self.date}"
    
            
    @staticmethod
    def delete_task_by_title_date():
        pass
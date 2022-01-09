import pandas as pd
from manage_csv_class import Manage_Csv
from category_class import Category

class Task:

    __path = 'task_list.csv'
    
    def __init__(self, title, date, category, status = 'Pendente'):
        self.title = title
        self.date = date
        self.category = category
        self.status = status

    def __repr__(self):
        return f"{self.title} {self.date}"
    
    @staticmethod
    def insert_task(*tasks):

        to_insert = pd.DataFrame(columns=Manage_Csv.read(Task.__path).columns)

        for task in tasks:
            try:
                Task.__check_task_existence(task)
                title = task.title
                date = task.date
                category_code = Category.find_code(task.category)
                status = task.status
                to_insert.loc[-1] = [title,category_code,status,date]

            except Exception as e:
                print(f"Erro ao inserir a task: {task}\nException: {str(e)}")

            

        Manage_Csv.append_df_to_csv(to_insert, Task.__path)
        
    @staticmethod
    def __check_task_existence(task):
        existing_tasks = Manage_Csv.read(Task.__path)

        equal_tasks = existing_tasks.loc[(existing_tasks['title'] == task.title) & (existing_tasks['date'] == task.date)].values

        if len(equal_tasks) > 0:
            print(task)
            raise Exception('Já existe uma tarefa com o mesmo nome e mesma data.')
            
    @staticmethod
    def delete_task_by_title():
        pass
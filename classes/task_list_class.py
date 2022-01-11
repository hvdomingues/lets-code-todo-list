class Task_List():
    
    __path = './database/task_list.csv'
 
    @staticmethod
    def get_task_list():
        return Manage_Csv.read(Task_List.__path)

    @staticmethod
    def get_treated_task_list():
        task_list = Task_List.get_task_list()
        task_list['category_code'].replace(Category.get_categories(), inplace = True)
        task_list.rename(columns={
            'title':'Título',
            'category_code':'Categoria', 
            'status':'Status', 
            'date':'Data'
            }, inplace=True)
        task_list.rename_axis('id', axis = 'columns', inplace = True)
        return task_list

    @staticmethod
    def update_task_list(to_update): #É necessário esse método? 
        Manage_Csv.rewrite_df_to_csv(to_update, Task_List.__path)

    @staticmethod
    def get_equal_tasks(task):
        '''This function returns tasks with the same Title or the task having same Title and Date based on object Task. If none found, return empty list.'''
        existing_tasks = Manage_Csv.read(Task_List.__path)

        if task.title != None:
            if task.date != None:
                if type(task.date) == datetime:
                    task.date = Manage_Date.date_to_str(task.date)
                equal_tasks = existing_tasks.loc[(existing_tasks['title'].str.lower() == task.title.lower()) & (existing_tasks['date'] == task.date)]
            else:
                equal_tasks = existing_tasks.loc[(existing_tasks['title'].str.lower() == task.title.lower())]
        
        if equal_tasks.empty:
            return []
        else:
            return equal_tasks

    @staticmethod
    def check_task_existence(task):
        '''This function requires a object Task as parameter and returns if the task exists based on the Title or Title and Date'''

        equal_tasks = Task_List.get_equal_tasks(task)

        if type(equal_tasks) == list:
            return False
        else:
            return True

    @staticmethod
    def insert_task(*tasks):
        '''This function requires one or more tasks, and try to append them to the CSV file'''

        to_insert = pd.DataFrame(columns=Manage_Csv.read(Task_List.__path).columns)

        sucess = 0
        errors = len(tasks)

        for task in tasks:
            if task == None:
                continue
            try:
                if Task_List.check_task_existence(task):
                    raise Exception("Já existe task com o mesmo nome e mesma data.")

                to_insert.loc[-1] = [task.title,task.category,task.status,task.date]

                print(f"\n[green][✓] Task '{task.title}', com data '{task.date}' inserida com sucesso.[/]")
                sucess += 1
                errors -= 1

            except Exception as e:
                print(f"\n[red][!] Erro ao inserir a task: {task}\nMotivo: {str(e)}[/]")
                

        Manage_Csv.append_df_to_csv(to_insert, Task_List.__path)

        if len(tasks) > 1:
            print(f"{sucess} tasks adicionadas com sucesso, {errors} não inseridas devido a erro.")

        

    @staticmethod
    def delete_task(task):
        '''This function receives a task type list or an index'''
        csv_tasks = Task_List.get_task_list()

        #print(task)

        if isinstance(task, list):
            index = csv_tasks.loc[(csv_tasks['title'].str.lower() == task[0].lower()) & (csv_tasks['date'] == task[3])].first_valid_index()
            csv_tasks.drop(index, inplace=True)
            Task_List.update_task_list(csv_tasks)
            print(f'Removendo: {task} ... [green][✓] Sucesso![/]')
            
        else:
            raise Exception("[red][!] Formato não suportado.[red]")

from datetime import datetime
from classes.manage_csv_class import Manage_Csv
from classes.category_class import Category
from classes.manage_date_class import Manage_Date
from classes.task_class import Task
import pandas as pd
from rich import print
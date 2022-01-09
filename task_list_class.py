from manage_csv_class import Manage_Csv
from category_class import Category

class Task_List():
    
    __path = 'task_list.csv'

    @staticmethod
    def get_task_list():
        return Manage_Csv.read(Task_List.__path)

    @staticmethod
    def print_tasks():
        task_list = Task_List.get_task_list()
        task_list['category_code'].replace(Category.get_categories(), inplace = True)
        task_list.rename(columns={
            'title':'Título',
            'category_code':'Código da Categoria', 
            'status':'Status', 
            'date':'Data'
            }, inplace=True)
        task_list.rename_axis('id', axis = 'columns', inplace = True)
        print(task_list)

    @staticmethod
    def update_task_list(to_update):
        Manage_Csv.rewrite_df_to_csv(to_update, Task_List.__path)
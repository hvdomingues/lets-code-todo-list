from manage_csv_class import Manage_Csv

class Task_List():
    
    __path = 'task_list.csv'

    @staticmethod
    def get_task_list():
        return Manage_Csv.read(Task_List.__path)
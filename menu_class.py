from numpy import ndarray


class Menu:

    @staticmethod
    def clean():
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def write_menu():
        Menu.clean()

        print('   ________________________________')
        print(' / \                               \ ')
        print('|   |      _.·´¯`·.¸.·´¯`·.¸_      |')
        print(' \_ |      TO-DO LIST PROJECT      |')
        print('    |      ¯`·.¸¸.·´`·.¸¸.·´¯      |')
        print('    |                              |')
        print('    |    O que deseja fazer?       |')
        print('    |                              |')
        print('    | 1 - Adicionar tarefa         |')
        print('    | 2 - Alterar status da tarefa |')
        print('    | 3 - Remover tarefa           |')
        print('    | 4 - Visualizar tarefa        |')
        print('    | 5 - Fechar                   |')
        print('    |   ___________________________|___')
        print('    |  /                              /')
        print('    \_/______________________________/')


    @staticmethod
    def check_menu_input() -> int:
        choice = 0
        while True:
            try:
                choice = int(input('\nDigite o número correspondente à opção: '))
                if choice in [1, 2, 3, 4, 5]:
                    return choice
                else:
                    print('Você deve escolhar um dos números do menu...')
                    sleep(1.5)
                    Menu.write_menu()
                    return Menu.check_menu_input()
            except:
                # Não sei se eu deveria lançar um Exception aqui
                print('A entrada deve ser de um número inteiro!')
                sleep(1.5)
                Menu.write_menu()

    @staticmethod
    def navigate():
        Menu.write_menu()
        choice = Menu.check_menu_input()
        if choice == 1:
            Menu.add_task()      
        elif choice == 2:
            Menu.change_task_status()
        elif choice == 3:
            Menu.remove_task()
        elif choice == 4:
            Menu.filter_task_by_date()
        else:
            # Fechar
            Menu.clean()
            print('Obrigado por usar este programa!')
            sleep(2)
            print('(de verdade)')
            sleep(1)
            Menu.clean()


    @staticmethod
    def add_task():
        Menu.clean()
        print('Adicionando uma nova tarefa! Digite algumas informações:')

        # o nome pode aceitar qualquer coisa de propósito
        name = input('Nome da tarefa: ')
        # data ainda sem tratamento de erros, posteriormente criar uma função check_date()
        date = input('Data da tarefa (dd/mm/aaaa): ')
        # ainda sem tratamento de erros para categoria
        category = input('Categoria (Casual | Importante | Urgente): ')
        status = -1
        while status != '0' and status != '1':
            status = input('Status (0 - Pendente | 1 - Concluído): ')
            if status not in ['0', '1']:
                print('Entrada inválida, tente novamente...')
        status = 'Pendente' if status == '0' else 'Concluído'

        task = Task(name, date, category, status)  
        Task_List.insert_task(task)
        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()
    
    @staticmethod
    def change_task_status():
        Menu.clean()
        print('Alterando o status de uma tarefa!')

        print('Segue a lista de tarefas: ')
        print(Task_List.get_treated_task_list())

        titulo = input('\nDigite o título da tarefa a ser alterada: ')

        tasks = Task_List.get_task_list()
        filter = tasks.loc[tasks['title'] == titulo]
        if len(filter) == 1:
            index = tasks.loc[tasks['title'] == titulo].first_valid_index()
            tasks.loc[index,'status'] = 'Concluído' if tasks.loc[index,'status'] == 'Pendente' else 'Pendente'
            Task_List.update_task_list(tasks)
            Menu.clean()
            print('Alteração realizada com sucesso!')
            print(Task_List.get_treated_task_list())
        elif len(filter) > 1:
            print('Muitas linhas com esse mesmo título!')
        else:
            print('Título não encontrado na tabela!')
        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()

    @staticmethod
    def remove_task():
        Menu.clean()
        print('Removendo uma tarefa da lista!')

        print('Segue a lista de tarefas: ')
        print(Task_List.get_treated_task_list())

        title = input('\nDigite o título da tarefa a ser removida: ')

        search_task = Task(title)

        tasks_found = Task_List.get_equal_tasks(search_task)

        if not isinstance(tasks_found, list):

            tasks_found_list = tasks_found.values.tolist()

            if len(tasks_found) == 1:
                Task_List.delete_task(tasks_found_list[0])
                Menu.clean()
                print('Alteração realizada com sucesso!')
                print(Task_List.get_treated_task_list())
            elif len(tasks_found) >= 1:
                Menu.clean()
                print(f"Tarefas encontradas com esse título: \n{Menu.list_tasks(tasks_found_list)}")
                input_index = (input("\nDigite os indexes que deseja remover separados por espaço ou 'todas' para deletar todas as tasks. "))
                
                if input_index == 'todas':
                    for task in tasks_found_list:
                        Task_List.delete_task(task)
                else:
                    indexes_to_remove = input_index.split(' ')   
                    [Task_List.delete_task(task) for index, task in enumerate(tasks_found_list) if str(index) in indexes_to_remove]
        else:
            print('Título não encontrado na tabela!')

        
            
        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()

    @staticmethod
    def filter_task_by_date():
        Menu.clean()
        print(Task_List.get_treated_task_list())
        print_date = False
        date = input('\nDigite a data a ser pesquisada (hoje | amanhã | dd/mm/aaaa): ')
        if date.lower() == 'hoje':
            date = Manage_Date.date_to_str(Manage_Date.today())
            print_date = True
        elif date.lower() == 'amanha' or date.lower() == 'amanhã':
            date = Manage_Date.date_to_str(Manage_Date.next_day())
            print_date = True
        else:
            try: 
                converted_date = Manage_Date.str_to_date(date) 
                date = Manage_Date.date_to_str(converted_date)
                print_date = True
            except ValueError as e: 
                print("O formato da data está incorreto, use apenas números e barras.") 
            except TypeError as e: 
                print("Digite uma data correta")
        
        # Agora filtrar a tabela
        if print_date:
            tasks = Task_List.get_task_list()
            filtered_tasks = tasks.loc[tasks['date'] == date].copy()
            ### Talvez trocar isso pelo método Task_List.get_treated_task_list() alterado para receber qualquer dataframe
            filtered_tasks['category_code'].replace(Category.get_categories(), inplace = True)
            filtered_tasks.rename(columns={
                'title':'Título',
                'category_code':'Categoria', 
                'status':'Status', 
                'date':'Data'
                }, inplace=True)
            filtered_tasks.rename_axis('id', axis = 'columns', inplace = True)
            ###
            if filtered_tasks.empty:
                print('\nNão foram encontradas tarefas para esta data.')
            else:
                Menu.clean()
                print(f'Exibindo resultados encontrados para {date}:\n')
                print(filtered_tasks)

        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()

    @staticmethod
    def list_tasks(tasks):
        tasks_string = ""
        for index, task in enumerate(tasks):
            tasks_string += f"\n{index}: {task[0]} | {task[3]}"

        return tasks_string



import os
import platform
from time import sleep
from datetime import datetime, timedelta
import re
from manage_csv_class import Manage_Csv
from manage_date_class import Manage_Date
from category_class import Category
from task_class import Task
from task_list_class import Task_List
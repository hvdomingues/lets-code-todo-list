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

        print('[yellow]   ________________________________[/]')
        print('[yellow] / \                               \ [/]')
        print('[yellow]|   |[/]      [magenta]_.·´¯`·.¸.·´¯`·.¸_[/]      [yellow]|[/]')
        print('[yellow] \_ |[/]      [bold yellow]TO-DO LIST PROJECT[/]      [yellow]|[/]')
        print('[yellow]    |[/]      [magenta]¯`·.¸¸.·´`·.¸¸.·´¯[/]      [yellow]|[/]')
        print('[yellow]    |                              |[/]')
        print('[yellow]    |[/]    [cyan]O que deseja fazer?[/]       [yellow]|[/]')
        print('[yellow]    |                              |[/]')
        print('[yellow]    |                              |[/]')
        print('[yellow]    | 1 - Adicionar tarefa         |[/]')
        print('[yellow]    | 2 - Alterar status da tarefa |[/]')
        print('[yellow]    | 3 - Remover tarefa           |[/]')
        print('[yellow]    | 4 - Visualizar tarefa        |[/]')
        print('[yellow]    | 5 - Fechar                   |[/]')
        print('[yellow]    |   ___________________________|___[/]')
        print('[yellow]    |  /                              /[/]')
        print('[yellow]    \_/______________________________/[/]')


    @staticmethod
    def check_menu_input() -> int:
        choice = 0
        while True:
            try:
                choice = int(input('\n - Digite o número correspondente à opção: '))
                if choice in [1, 2, 3, 4, 5]:
                    return choice
                else:
                    print('\n[red][!]Você deve escolhar um dos números do menu...[/]')
                    sleep(1.5)
                    Menu.write_menu()
                    return Menu.check_menu_input()
            except:
                # Não sei se eu deveria lançar um Exception aqui
                print('\n[red][!] A entrada deve ser de um número inteiro![/]')
                sleep(1.5)
                Menu.write_menu()

    @staticmethod
    def navigate():
        Menu.write_menu()
        choice = Menu.check_menu_input()
        try:
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
                print('[green][✓] Obrigado por usar este programa![/]')
                sleep(2)
                print('[cyan](de verdade)[/]')
                sleep(1)
                Menu.clean()
        except Exception as e:
            print(f'\n[red]Erro: {e}[/]')
            input('\nPressione qualquer tecla para voltar ao Menu...')
            Menu.navigate()


    @staticmethod
    def add_task():
        Menu.clean()
        print(' [bold yellow]~ Adicionando uma nova tarefa! ~[/] \n\nDigite algumas informações:\n')

        # o nome pode aceitar qualquer coisa de propósito
        name = input(' - Nome da tarefa: ')
        # data ainda sem tratamento de erros, posteriormente criar uma função check_date()
        date = input(' - Data da tarefa (dd/mm/aaaa | hoje | amanhã): ')
        # ainda sem tratamento de erros para categoria
        category = input(' - Categoria (Casual | Importante | Urgente): ').capitalize()
        status = -1
        while status != '0' and status != '1':
            status = input(' - Status (0 - Pendente | 1 - Concluído): ')
            if status not in ['0', '1']:
                print('[red][!] Entrada inválida, tente novamente...[/]')
        status = 'Pendente' if status == '0' else 'Concluído'

        task = Task(name, date, category, status)  
        Task_List.insert_task(task)

        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()
    
    @staticmethod
    def change_task_status(): #MUDAR
        Menu.clean()
        print(' [bold yellow]~ Alterando o status de uma tarefa! ~[/]\n')

        print('Segue a lista de tarefas:\n')
        Menu.navigate_dataframe(Task_List.get_treated_task_list())

        titulo = input('\n - Digite o título da tarefa a ser alterada: ')

        tasks_found = Task_List.get_equal_tasks(Task(title=titulo))

        tasks_found_list = Task.df_to_task_list(tasks_found)

        if len(tasks_found) == 1:
            
            if tasks_found_list[0].status == 'Concluído':
                tasks_found_list[0].status = 'Pendente'
            else:
                tasks_found_list[0].status = 'Concluído'

            Task_List.update_task(tasks_found_list[0])
            Menu.clean()
            print('[green][✓] Alteração realizada com sucesso!\n')
            print(Task_List.get_treated_task_list())

        elif len(tasks_found) >= 1:
            Menu.clean()
            print(f"Tarefas encontradas com esse título: \n{Menu.list_tasks(tasks_found.values.tolist())}")
            input_index = (input("\nDigite os indexes que deseja mudar o status separados por espaço ou 'todas' para alterar de todas as tasks. "))
            
            if input_index == 'todas':
                for task in tasks_found_list:

                    task.change_status()

                    Task_List.update_task(task)

                print('\n[green][✓] Alteração de status de todas as tarefas com o mesmo título realizada com sucesso!')
            else:
                indexes_to_remove = input_index.split(' ')

                # Troquei para um for fora de list comprehension só para facilitar o print em caso de digitação errada 
                for index,task in enumerate(tasks_found_list):
                    if str(index) in indexes_to_remove:
                        task.change_status()
                        Task_List.update_task(task)

                print('\n[green][✓] Alteração de status de todas as tarefas selecionadas realizada com sucesso!')

        else:
            print('[red][!] Título não encontrado na tabela![/]')

        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()

    @staticmethod
    def remove_task():
        Menu.clean()
        print(' [bold yellow]~ Removendo uma tarefa da lista! ~[/]\n')

        print('Segue a lista de tarefas:\n')
        print(Task_List.get_treated_task_list())

        title = input('\n - Digite o título da tarefa a ser removida: ')

        search_task = Task(title)

        tasks_found = Task_List.get_equal_tasks(search_task)

        if not isinstance(tasks_found, list):

            tasks_found_list = tasks_found.values.tolist()

            if len(tasks_found) == 1:
                Task_List.delete_task(tasks_found_list[0])
                Menu.clean()
                print('[green][✓] Remoção realizada com sucesso!\n')
                print(Task_List.get_treated_task_list())
            elif len(tasks_found) >= 1:
                Menu.clean()
                print(f"Tarefas encontradas com esse título: \n{Menu.list_tasks(tasks_found_list)}")
                input_index = (input("\nDigite os indexes que deseja remover separados por espaço ou 'todas' para deletar todas as tasks. "))
                
                if input_index == 'todas':
                    for task in tasks_found_list:
                        Task_List.delete_task(task)
                    print('\n[green][✓] Remoção de todas as tarefas com o mesmo título realizada com sucesso!')
                else:
                    indexes_to_remove = input_index.split(' ')
                    remove_something = False   
                    # Troquei para um for fora de list comprehension só para facilitar o print em caso de digitação errada 
                    for index, task in enumerate(tasks_found_list):
                        if str(index) in indexes_to_remove:
                            Task_List.delete_task(task)
                            remove_something = True
                    
                    # Antigo
                    #[Task_List.delete_task(task) for index, task in enumerate(tasks_found_list) if str(index) in indexes_to_remove]

                    if not remove_something:
                        print('[red][!] Entrada inválida[/]')
                

        else:
            print('[red][!] Título não encontrado na tabela![/]')

        
            
        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()

    @staticmethod
    def filter_task_by_date():
        Menu.clean()
        print(' [bold yellow]~ Filtrando a tabela por data! ~[/] \n\nTabela completa:\n')
        # Essa exibição de toda a tabela é proposital
        Menu.navigate_dataframe(Task_List.get_treated_task_list())
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
                print("[red][!] O formato da data está incorreto, use apenas números e barras.[/]") 
            except TypeError as e: 
                print("[red][!] Digite uma data correta[/]")
        
        # Agora filtrar a tabela
        if print_date:

            filtered_tasks = Task_List.get_equal_tasks(Task(None, date=date))

            if isinstance(filtered_tasks, list):
                print('\n[red][!] Não foram encontradas tarefas para esta data.[/]')
            else:
                Menu.clean()
                filtered_tasks = Task_List.get_treated_task_list(filtered_tasks)
                print(f'[green][✓] Exibindo resultados encontrados para {date}:\n')
                Menu.navigate_dataframe(filtered_tasks)

        input('\nPressione qualquer tecla para voltar ao Menu...')
        Menu.navigate()

    @staticmethod
    def list_tasks(tasks):
        tasks_string = ""
        for index, task in enumerate(tasks):
            tasks_string += f"\n{index}: {task[0]} | {task[3]}"

        return tasks_string

    @staticmethod 
    def navigate_dataframe(df, limit = 10, page = 1): 
 
        print(f' [yellow][Lista de Tarefas][/] Página {page}/{int(np.ceil(len(df.index)/limit))}:\n') 
 
        index = page*limit 
 
        print(df.iloc[index-limit:(index)]) 
 
        if len(df.index) > limit: 
            option = -1 
 
            if page - 1 == 0: 
                while option not in (1,3): 
                    option = int(input("\nDigite 1 para a próxima página e 3 para manter a página: ")) 
            elif len(df.index) > index: 
                while option not in (1,2,3): 
                    option = int(input("\nDigite 1 para a próxima página, 2 para a página anterior e 3 para manter a página: ")) 
            else: 
                while option not in (2,3): 
                    option = int(input("\nDigite 2 para a página anterior e 3 para manter a página: ")) 
 
            if option == 1: 
                Menu.clean() 
                Menu.navigate_dataframe(df, limit, page + 1) 
            elif option == 2:
                Menu.clean()  
                Menu.navigate_dataframe(df, limit, page - 1)




import os
import platform
from time import sleep
import numpy as np
from classes.manage_date_class import Manage_Date
from classes.category_class import Category
from classes.task_class import Task
from classes.task_list_class import Task_List
from rich import print
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
    def change_task_status():
        Menu.clean()
        print(' [bold yellow]~ Alterando o status de uma tarefa! ~[/]\n')

        print('Segue a lista de tarefas:\n')
        print(Task_List.get_treated_task_list())

        titulo = input('\n - Digite o título da tarefa a ser alterada: ')

        tasks = Task_List.get_task_list()
        filter = tasks.loc[tasks['title'].str.lower() == titulo.lower()]
        if len(filter) == 1:
            index = tasks.loc[tasks['title'].str.lower() == titulo.lower()].first_valid_index()
            tasks.loc[index,'status'] = 'Concluído' if tasks.loc[index,'status'] == 'Pendente' else 'Pendente'
            Task_List.update_task_list(tasks)
            Menu.clean()
            print('[green][✓] Alteração realizada com sucesso!\n')
            print(Task_List.get_treated_task_list())
        elif len(filter) > 1:
            print('\n[red][!] Muitas linhas com esse mesmo título![/]')
        else:
            print('\n[red][!] Título não encontrado na tabela![/]')
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
                print("[red][!] O formato da data está incorreto, use apenas números e barras.[/]") 
            except TypeError as e: 
                print("[red][!] Digite uma data correta[/]")
        
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
                print('\n[red][!] Não foram encontradas tarefas para esta data.[/]')
            else:
                Menu.clean()
                print(f'[green][✓] Exibindo resultados encontrados para {date}:\n')
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
from classes.manage_date_class import Manage_Date
from classes.category_class import Category
from classes.task_class import Task
from classes.task_list_class import Task_List
from rich import print
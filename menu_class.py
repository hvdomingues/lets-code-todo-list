import os
import platform
from time import sleep

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
                choice = int(input('Digite o número correspondente à opção: '))
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
            # Adicionar tarefa
            pass
        elif choice == 2:
            # Alterar status da tarefa
            pass
        elif choice == 3:
            # Remover tarefa
            pass
        elif choice == 4:
            # Visualizar tarefa
            pass
        else:
            # Fechar
            Menu.clean()
            print('Obrigado por usar este programa!')
            sleep(2)
            print('(de verdade)')
            sleep(1)
            Menu.clean()
            

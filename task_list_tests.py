from task_list_class import Task_List
from task_class import Task


# ----------------------------------------------------------------------------------------- #
# ---------------------------- Testes da classe Task_List --------------------------------- #
# ----------------------------------------------------------------------------------------- #

print("------------------- Testes de funções para retornar a task_list CSV no formato DataFrame -------------------")
print("Retorno esperado -> DataFrame de tasks\n")
print(Task_List.get_task_list())

print("\n\nRetorno esperado -> DataFrame de tasks com nomes de coluna e categoria tratados.\n")
print(Task_List.get_treated_task_list())

print("\n\n\n------------------- Testes de função para reescrever o DataFrame -------------------")
print("\n\nRetorno esperado -> ")

print("\n\n\n------------------- Testes de função para procurar objeto Task na Task_List utilizando title ou title e date -------------------")
print("\n\nTeste 01. Retorno esperado -> Dataframe contendo - Primeira tarefa,1,Pendente,22/10/1999\n")
print(Task_List.get_equal_tasks(Task("Primeira tarefa")))

print("\n\nTeste 02. Retorno esperado -> Dataframe contendo duas tasks com o mesmo nome, datas diferentes.\n")
print(Task_List.get_equal_tasks(Task("escovar os dentes")))

print("\n\nTeste 03. Retorno esperado -> Lista vazia\n")
print(Task_List.get_equal_tasks(Task("teste de task de batata assada")))

print("\n\n\n------------------- Testes de função para checar existência da Task na Task_List utilizando title ou title e date -------------------")
print("\n\nTeste 01. Somente título passado - Retorno esperado -> True\n")
print(Task_List.check_task_existence(Task("Assar batatas")))

print("\n\nTeste 02. Título e data passado - Retorno esperado -> True\n")
print(Task_List.check_task_existence(Task("Assar batatas", date="09/01/2022")))

print("\n\nTeste 03. Somente título passado - Retorno esperado -> False\n")
print(Task_List.check_task_existence(Task("Esse título não existe")))

print("\n\nTeste 04. Título existente e data inexistente passado - Retorno esperado -> False\n")
print(Task_List.check_task_existence(Task("Escovar os dentes", date="22-10-1998")))

print("\n\n\n------------------- Testes de função para inserir Task na Task_List ---------------------")
print("\n ------------------- PRECISA RESETAR O CSV ---------------------")
print("\n\nTeste 01. Somente uma task passada, não existente - Retorno esperado -> print de sucesso da task adicionada\n")
task1 = Task("Ler Harry Potter", date="22/10/2022", category="Urgente")
Task_List.insert_task(task1)

print("\n\nTeste 02. Duas tasks passadas, uma existe e outra não - Retorno esperado -> 1 sucesso e 1 erro\n")
task1 = Task("Ler Harry Potter", date="22/10/2022", category="Urgente")
task2 = Task("Aprender Python", date="31/12/1999", category="Urgente")
Task_List.insert_task(task1, task2)

print("\n\nTeste 03. Duas tasks passadas, uma existente e outra com data incorreta - Retorno esperado -> 2 erros, um devido a data incorreta\n")
task1 = Task("Ler Harry Potter", date="22/10/2022", category="Urgente")
task2 = Task("Aprender Python", date="72/12/1959", category="Urgente")
Task_List.insert_task(task1, task2)

print("\n\nTeste 04. Uma task passada, categoria inexistente - Retorno esperado -> 1 erro devido a categoria inexistente\n")
task1 = Task("Ler Harry Potter 2", date="22/10/2022", category="Batata")
Task_List.insert_task(task1)









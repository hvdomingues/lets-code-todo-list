from task_class import Task

# ----------------------------------------------------------------------------------------- #
# ---------------------------- Testes da classe Task -------------------------------------- #
# ----------------------------------------------------------------------------------------- #

print("\n\n------------------- Testes de funções para instanciar o objeto task -------------------")
print("\nRetorno esperado -> Objeto com todos os atributos preenchidos\n")
task1 = Task("Tarefa 1", date="28/02/2022", category=0)
print(task1.title, " data: ", task1.date, " categoria: ", task1.category, " Status: ", task1.status)

print("\n\nRetorno esperado -> Objeto com título e data de hoje. Sem categoria e status pendente.\n")
task2 = Task("Tarefa 2", date='hoje')
print(task2.title, " data: ", task2.date, " categoria: ", task2.category, " Status: ", task2.status)

print("\n\nRetorno esperado -> Objeto com título e data de amanhã. Sem categoria e status pendente.\n")
task3 = Task("Tarefa 3", date='amanha')
print(task3.title, " data: ", task3.date, " categoria: ", task3.category, " Status: ", task3.status)

print("\n\nRetorno esperado -> Erro ao instanciar, data inválida\n")
task4 = Task("Tarefa 4", date='ontem')

print("\n\nRetorno esperado -> Erro ao instanciar, data inválida\n")
task5 = Task("Tarefa 5", date='31/02/2022')












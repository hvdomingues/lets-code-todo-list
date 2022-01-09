import pandas as pd

class Manage_Csv:

    # Retorna o conteúdo do .csv em formato de DataFrame
    @staticmethod
    def read(path):
        df = pd.read_csv(path)
        return df
    
    # Escreve novos conteúdos ao final de um arquivo pré-existente/ cria um novo se o arquivo não existir
    @staticmethod
    def append_df_to_csv(to_append, path):
        try:
            to_append.to_csv(path, mode='a', header=False, index=False)
        except Exception as e:
            print(e)

    # Reescrever o arquivo, para caso haja alguma deleção na lista de tarefas
    @staticmethod
    def rewrite_df_to_csv(to_append, path):
        try:
            to_append.to_csv(path, mode='w', header=False, index=False)
        except Exception as e:
            print(e)

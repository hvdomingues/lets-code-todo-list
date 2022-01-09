import pandas as pd

class Manage_Csv:

    @staticmethod
    def read(path):
        df = pd.read_csv(path)
        return df
    
    @staticmethod
    def append_df_to_csv(to_append, path):
        try:
            to_append.to_csv(path, mode='a', header=False, index=False)
        except Exception as e:
            print(e)
from os import stat

class Category:

    # Atributo privado que funciona como um enumerator

    __categories = ['Importante','Urgente','Casual']
    
    # Retorna o primeiro código(key) dentro de __categories que possui o nome category_name
    # Se quiser manter essa estrutura de keys podemos usar uma lista no lugar de dicionário
    # E aí colocaríamos return apenas  __categories.index(category_name)
    @staticmethod
    def find_code(category_name):
        if category_name in Category.__categories:   
            return Category.__categories.index(category_name)
        else:
            raise KeyError('O nome da categoria é inválido.')

    # Retorna o nome da categoria associada ao código pesquisado
    @staticmethod
    def find_name(category_code):
        return Category.__categories[category_code]

    # Retorna o dicionário de categorias cadastradas
    @staticmethod
    def get_categories():
        return Category.__categories

    # Valida se o código é valido, caso não seja gera um erro e caso seja retorna o código.
    @staticmethod
    def check_code(code):
        if code in Category.__categories:
            return code
        else:
            raise KeyError("O código da categoria é inexistente.")
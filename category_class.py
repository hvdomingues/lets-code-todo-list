from os import stat

class Category:

    # Atributo privado que funciona como um enumerator
    __categories = {0:'Casual', 1:'Importante', 2: 'Urgente'}
    
    # Retorna o primeiro código(key) dentro de __categories que possui o nome category_name
    # Se quiser manter essa estrutura de keys podemos usar uma lista no lugar de dicionário
    # E aí colocaríamos return apenas  __categories.index(category_name)
    @staticmethod
    def find_code(category_name):
        return (list(Category.__categories.keys())[list(Category.__categories.values()).index(category_name)])

    # Retorna o nome da categoria associada ao código pesquisado
    @staticmethod
    def find_name(category_code):
        return Category.__categories[category_code]

    # Retorna o dicionário de categorias cadastradas
    @staticmethod
    def get_categories():
        return Category.__categories
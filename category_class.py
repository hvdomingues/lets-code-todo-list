class Category:

    # Atributo privado que funciona como um enumerator
    __categories = {0:'Importante', 1: 'Urgente', 2:'Casual', 3:'Urgente'}
    
    # Retorna o primeiro código(key) dentro de __categories que possui o nome category_name
    # Se quiser manter essa estrutura de keys podemos usar uma lista no lugar de dicionário
    # E aí colocaríamos return apenas  __categories.index(category_name)
    @staticmethod
    def find_code(category_name):
        return (list(Category.__categories.keys())[list(Category.__categories.values()).index(category_name)])
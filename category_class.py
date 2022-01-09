class Category:

    __categories = {0:'Teste'}
    
    @staticmethod
    def find_code(category_name):
        return (list(Category.__categories.keys())[list(Category.__categories.values()).index(category_name)])
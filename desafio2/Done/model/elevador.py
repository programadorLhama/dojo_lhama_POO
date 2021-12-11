class Elevador:
    def __init__(self, id) -> None:
        self.__id = id
        self.__andar = 1
    
    def set_andar(self, andar):
        self.__andar = andar
    
    def get_andar(self):
        return self.__andar
    
    def check_id(self, id):
        return (self.__id == id)
    
    def get_id(self):
        return self.__id
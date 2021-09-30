class Usuario():
    def __init__(self, id_sala=None):
        self.__id_sala = id_sala

    @property
    def id_sala(self):
        if self.__id_sala:
            return self.__id_sala
        else:
            return None

    @id_sala.setter
    def id_sala(self, id_sala=None):
        self.__id_sala = id_sala
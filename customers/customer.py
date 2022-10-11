class Customer:

    def __init__(self, _id, username, password):
        self.__id = _id
        self.__username = username
        self.__password = password

    def getId(self):
        return self.__id

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password
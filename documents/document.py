class Document:

    def __init__(self, documentId, name, author, documentType, copy, quantity, price, description):
        self.__documentId = documentId
        self.__name = name
        self.__copy = copy
        self.__author = author
        self.__documentType = documentType
        self.__quantity = quantity
        self.__price = price
        self.__description = description

    def getName(self):
        return self.__name

    def getCopy(self):
        return self.__copy

    def getAuthor(self):
        return self.__author

    def getDocumentType(self):
        return self.__documentType

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price

    def getdescription(self):
        return self.__description
class Sale:

    def __init__(self, saleId, customerId, documentId, payMethod, quantity, price, total, date):
        self.__saleId = saleId
        self.__customerId = idCustomer
        self.__documentId = idDocument
        self.__payMethod = payMethod
        self.__quantity = quantity
        self.__price = price
        self.__total = total
        self.__date = date

    def getSaleId(self):
        return self.__saleId

    def getCustomerId(self):
        return self.__customerId

    def getDocumentId(self):
        return self.__documentId

    def getPayMethod(self):
        return self.__payMethod

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price

    def getTotal(self):
        return self.__total

    def getDate(self):
        return self.__date
class Sale:

    def __init__(self, saleId, customer, document, payMethod, quantity, price, total, date):
        self.__saleId = saleId
        self.__customer = Customer
        self.__document = Document
        self.__payMethod = payMethod
        self.__quantity = quantity
        self.__price = price
        self.__total = total
        self.__date = date

    def getSaleId(self):
        return self.__saleId

    def getCustomer(self):
        return self.__customer

    def getDocument(self):
        return self.__document

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
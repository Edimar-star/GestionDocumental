class Rent:

        def __init__(self, rentId, customerId, documentId, payMethod, quantity, price, total, startDate, endDate):
        self.__rentId = rentId
        self.__customerId = idCustomer
        self.__documentId = idDocument
        self.__payMethod = payMethod
        self.__quantity = quantity
        self.__price = price
        self.__total = total
        self.__startDate = startDate
        self.__endDate = endDate

    def getRentId(self):
        return self.__rentId

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

    def getStartDate(self):
        return self.__startDate

    def getEndDate(self):
        return self.__endDate
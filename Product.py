class Product:
    def __init__(self, nameProduct, nameShop, price, count, units):
        self.nameProduct = nameProduct
        self.nameShop = nameShop
        self.price = price
        self.count = count
        self.units = units

    def getNameProduct(self):
        return self.nameProduct

    def getNameShop(self):
        return self.nameShop

    def getPrice(self):
        return self.price

    def getNameCount(self):
        return self.count

    def getUnits(self):
        return self.units

    def setNameProduct(self, nameProduct):
        self.nameProduct = nameProduct

    def setNameShop(self, nameShop):
        self.nameShop = nameShop

    def setPrice(self, price):
        self.price = price

    def setCount(self, Count):
        self.Count = Count

    def setUnits(self, units):
        self.units = units
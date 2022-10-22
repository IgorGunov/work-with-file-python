from Product import Product

def printProduct(arrayProduct):
    print("Данные из файла : ")
    for i in range(len(arrayProduct)):
        print("Номер товара = ", i,
              "Наименование товара: ", arrayProduct[i].getNameProduct(),
              "Наименование магазина: ", arrayProduct[i].getNameShop(),
              "Цена: ", arrayProduct[i].getPrice(),
              "Количество: ", arrayProduct[i].getNameCount(),
              "Единица измерения товара: ", arrayProduct[i].getUnits())

def printMenu():
    print("Что вы хотите сделать ?\n"
          "1 - Скорректировать данные\n"
          "2 - Дополнить список\n"
          "3 - Сортировать по названию товара\n"
          "4 - Сортировака по названию магазига\n"
          "5 - Вывод информации о товаре, название которого введено с клавиатуры\n"
          "6 - Запись списка в файл под тем же или новым именем\n"
          "7 - Вывод информации в файле\n"
          "8 - Выход")

def change(arrayProduct):
    print("Какую запись вы хотите изменить ?")
    printProduct(arrayProduct)
    inputUser = int(input())
    arrayProduct[inputUser].setNameProduct(input("Введите новое имя продукта "))
    arrayProduct[inputUser].setNameShop((input("Введите новое имя магазина ")).lower())
    while (True):
        try:
            arrayProduct[inputUser].setPrice(input("Введите новую цену "))
            break
        except Exception:
            print("Должно вводиться число !")
    arrayProduct[inputUser].setCount(input("Введите новое количество "))
    arrayProduct[inputUser].setUnits(input("Введите новое измерение "))
    printProduct(arrayProduct)

def sortName(arrayProduct):
    arrayProduct.sort(key=lambda x: x.nameProduct, reverse=False)
    printProduct(arrayProduct)

def sortNameShop(arrayProduct):
    arrayProduct.sort(key=lambda x: x.nameShop, reverse=False)
    printProduct(arrayProduct)

def search(name, arrayProduct):
    for i in range(len(arrayProduct)):
        if (arrayProduct[i].getNameProduct() == name):
            print("Номер товара = ", i,
                  "Наименование товара: ", arrayProduct[i].getNameProduct(),
                  "Наименование магазина: ", arrayProduct[i].getNameShop(),
                  "Цена: ", arrayProduct[i].getPrice(),
                  "Количество: ", arrayProduct[i].getNameCount(),
                  "Единица измерения товара: ", arrayProduct[i].getUnits())

def addProduct(b):
    w = len(b)
    newProduct = Product("", "", 0, 0, "")
    b.append(newProduct)
    b[w].setNameProduct(input("Введите новое имя продукта "))
    b[w].setNameShop((input("Введите новое имя магазина ")).lower())
    while(True):
        try:
            b[w].setPrice(int(input("Введите новую цену ")))
            break
        except Exception: print("Должно вводиться число !")
    b[w].setCount(int(input("Введите новое количество ")))
    b[w].setUnits(input("Введите новое измерение "))

def saveNewArrayProduct(arrayProduct):
    file = input("Введите имя файла, в который сохранить информацию ? ")
    f = open(file, 'w')
    for i in range(len(arrayProduct)):
        f.writelines(arrayProduct[i].getNameProduct() + " " +
                     arrayProduct[i].getNameShop() + " " +
                     str(arrayProduct[i].getPrice()) + " " +
                     str(arrayProduct[i].getNameCount()) + " " +
                     arrayProduct[i].getUnits() + "\n")

Fin = open("file.txt")
s = Fin.readlines()
count = len(s)
a = []
arrayProduct = []

for i in range(count):
    a.append([""] * 5)

for i in range(len(s)):
    a[i] = s[i].split(" ")

for i in range(0, count):
    arrayProduct.append(Product(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4]))

while (True):
    printMenu()
    inputUser = int(input())
    if inputUser == 1:
        change(arrayProduct)
    elif inputUser == 2:
        addProduct(arrayProduct)
    elif inputUser == 3:
        sortName(arrayProduct)
    elif inputUser == 4:
        sortNameShop(arrayProduct)
    elif inputUser == 5:
        search(input("Введите имя товара "), arrayProduct)
    elif inputUser == 6:
        saveNewArrayProduct(arrayProduct)
    elif inputUser == 7:
        printProduct(arrayProduct)
    elif inputUser == 8:
        break

Fin.close()
spisok_dohod = []
spisok_rashod = []
def dobav_dohod():
    for i in range(1, 12+1):
        dohod = input(str(i) + "месяц =")
        try:
            dohod = int(dohod)
        except:
            print("Неверное число")
        spisok_dohod.append(dohod)
    print(spisok_dohod)
def dobav_rashod():
    for i in range(1, 12+1):
        rashod = input(str(i) + "Месяц =")
        try:
            rashod = int(rashod)
        except:
            print("неверное число")
        spisok_rashod.append(rashod)
        print(spisok_rashod)
def udalit_dohod():
    mecac = input("Какой месяц нужно удалить")
    try:
        mecac = int(mecac)
    except:
        print("Неверное число")
    spisok_dohod.pop(mecac)
    dohod = input("Какой новый доход")
    try:
        dohod = int(dohod)
    except:
        print("Неверное число")
    spisok_dohod.insert(mecac, dohod)
    print(spisok_dohod)
def udalit_rashod():
    mecac = input("Какой месяц нужно удалить")
    try:
        mecac = int(mecac)
    except:
        print("Неверное число")
    spisok_rashod.pop(mecac)
    dohod = input("Какой новый доход")
    try:
        dohod = int(dohod)
    except:
        print("Неверное число")
    spisok_rashod.insert(mecac, dohod)
    print(spisok_rashod)
def otchet():
    maxdohod = int(0)
    mindohod = int(0)
    maxroshod = int(0)
    minrshod = int(0)
    for i in range (0 , 11+1):
        if spisok_dohod[i] > maxdohod:
            maxdohod = spisok_dohod[i]
    print("Максимальный доход" + str(maxdohod))
    for i in range(0, 11+1):
       otchet = spisok_dohod[i] - spisok_rashod[i]
       print(otchet)
while True:
    print("1)Добавить Доход")
    print("2)Добавить Расход")
    print("3)Удалить доход")
    print("4)Удалить расход")
    print("5)Отчет")
    vibor = input("Выберите функцию")
    try:
        vibor = int(vibor)
    except:
        print("Неверное число")
    if vibor == 1:       
        dobav_dohod()
    elif vibor == 2:
         dobav_rashod()
    elif vibor == 3:
         udalit_dohod()
    elif vibor == 4:
        udalit_rashod()
    elif vibor == 5:
        otchet()
    else:
        print("Нет такой функции")

    
        
        
        
        

nachalo = input("Введите начальное число")
konec = input("Введите последнее число")
diaposon = input("Введите Диапозон")
if nachalo !="" and konec !="" and diaposon !="":
    nachalo1 = int(nachalo)
    konec1 = int(konec)
    diaposon1 = int(diaposon)
    if nachalo1 >0 and konec1 >0 and diaposon1 >0:
        for i in range (nachalo1,konec1+1,diaposon1):
            print(i)
    else:
        print("Низя же так, низя, низя!!!1адын") 
else:
    print("Низя же так, низя, низя!!!1адын")

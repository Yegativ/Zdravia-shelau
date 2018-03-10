number = input("Введите начало")
number1 = input("Введите конец")
redach = input("Введите диапозон между числами")
if number !="":
     provnumber = int(number)
     provnumber1 = int (number1)
     provredach = int(redach)

    if provnumber1 > provnumber and provnumber >0 and provnumber1 >0 and provredach >0:
       while provnumber <=number1:
             print(provnumber)
             provnumber += provredach
else:
       print("Низя так, низя, низя!!!1адын") 
else:
    print("Низя так, низя, низя!!!1адын")

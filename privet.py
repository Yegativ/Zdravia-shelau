den = int(input("Сколько сейчас времени"))

if den >=4 and den <=9:
    print("утро")
elif den == 12:
    print("Полдень")
elif den >=13 and den <=15:
    print("Обед")
elif den >= 18 and den <= 23 :
    print("Вечер")
elif den == 24:
    print("Полночь")
elif den >=1 and den <=5:
    print("Ночь")


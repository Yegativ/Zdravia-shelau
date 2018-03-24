ocenka = input("Введите оценку от 1 до 10")
otsiv = input("Оставьте свой отзыв")

if ocenka != "":
    provocenka = int(ocenka)
    if provocenka >0 and provocenka == 10:
        print(provocenka)
        print(otsiv)
    else:
        print("Неправильная оценка")
else:
    print("Сломать меня хотел да?")

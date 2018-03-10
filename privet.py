den = int(input("Введите день"))
mecac = int(input("Введите месяц"))
god = int(input("Введите год"))

if den > 0 and den <10 or den >10 and den <=31 and mecac >=1 and mecac <3 or mecac >3 and mecac <=12 and god >=0 and god < 2018 or god >2018:
    print("Верная дата!")
elif den == 10 and mecac == 3 and god == 2018:
    print("Дата показывает сегоднешний день!")
else:
    print("Неверная дата!")
print("пака-пака!")

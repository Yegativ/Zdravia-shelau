sum = 0
while True:
    t = input("Введите число")
    if t !="":
        t1 = int(t)
        if t1 >0 and < 1000000:
           sum += t1
           print("Сумма= ", sum)
        elif t1 >= 1000000:
            sum += t1
            print("Сумма", sum)
            break
        else:
           print("Низя так, низя, низя!!!1адын")
           continue
    else:
        print("Низя так, низя, низя!!!1адын")
        continue

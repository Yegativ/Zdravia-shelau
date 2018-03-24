def main():
    sum = 0
    count = input("Сколько купюр в кармажке")
    if count !="":
        count1 = int(count)
        money=input("Введите ценность банкноты")
        if money !="":
            money1 = int(money)
            for i in range (1,count1+1):
                    while proverka(money1) == True:
                        money=input("Введите ценность банкноты")
                        if money !="":
                            money1 = int(money)
                            sum += money1
    result(sum)
    
    
    
    
def proverka(money):
    if money ==200 or money == 500 or money == 1000 or money == 2000 or money == 5000 or money == 10000 or money == 20000:
        return True
    else:
        print("Фу фальшивомонетчик, вызываю ментов, земля тебе пухом братишка")
        return False
def result(sum):
    print(sum)
main()
    
    
    


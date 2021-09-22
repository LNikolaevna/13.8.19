number_of_tickets = int(input("Введите количество билетов:"))
while number_of_tickets <= 0:
    print("Введено неправильное значение, повторите ввод:")
    number_of_tickets = int(input("Введите количество билетов:"))
i = 1
while (i <= number_of_tickets):
    print(str(i) + "й билет")
    age = int(input("Введите возраст участника:"))
    while age <= 0:
        print("Введено неправильное значение, повторите ввод:")
        age = int(input("Введите возраст участника"))

    price = 0
    if 0 < age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    elif age >= 25 :
        price = 1390
    i = i + 1
    summa = 0 + price
print("Сумма билетов без скидки:" + str(summa))
if number_of_tickets >=3:
    summa = summa * 0.9
    print("Действующая скидка 10%. К оплате:" + str(summa))
    exit
else:
    print("К оплате:" + str(summa))
    exit
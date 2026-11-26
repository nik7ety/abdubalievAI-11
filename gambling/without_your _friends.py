import random

def two_dice_roll():
    coin = 30
    choice_with_no_choice = input("Введи сюда что угодно")
    while True:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 + dice2 == 7 or dice1 + dice2 == 11:
            coin = coin - 5
            print("Джекпот.")
            coin += 15
            print(f"Баланс: {coin}")
            try:
                gambling = int(input("Еще раз?(1 - да; 2 - нет)"))
                if gambling == 1:
                    continue
                elif gambling == 2:
                    print("До встречи.")
                    break
                else:
                    print("Не то.")
            except ValueError:
                print("Напиши цифрой.")
        elif dice1 == dice2:
            coin = coin - 5
            print("Дубль.")
            coin += 10
            print(f"Баланс: {coin}")
            try:
                gambling = int(input("Еще раз?(1 - да; 2 - нет)"))
                if gambling == 1:
                    continue
                elif gambling == 2:
                    print("До встречи.")
                    break
                else:
                    print("Не то.")
            except ValueError:
                print("Напиши цифрой.")
        elif coin == 0:
            print("Баланс исчерпан, вы проиграли.")
            break
        else:
            coin = coin - 5
            print(dice1 + dice2)
            print(f"Баланс: {coin}")
            try:
                gambling = int(input("Еще раз?(1 - да; 2 - нет)"))
                if gambling == 1:
                    continue
                elif gambling == 2:
                    print("До встречи.")
                    break
                else:
                    print("Не то.")
            except ValueError:
                print("Напиши цифрой.")


while True:
    question = input("Испытать удачу? (да/нет): ")
    if question.lower() == 'да' or question.lower() == 'yes':
        print ("Отлично.")
        two_dice_roll()
        break
    elif question.lower() == 'нет' or question.lower() == 'no':
        print("Чтож... у тебя есть время подумать.")
    else:
        print("Твой ответ как в тумане, повтори.")


#Смотрите! адеватный код! быбыбыбыбыбыббыбыбыббыббыебебебебебепббееббебебебебебеб ыыыыыыыыыыыыыыыыыыыыыыыыыыыы ээээээээээээвэ\адаэлзкуэлз уэуэуэууыуыуыуыуыуыуыыуыыуыуыуыуыуыуыуыуыуыуыуыуыуыуыуыуыуыуыыыыыыыыыыыыыыыыыыыыыыыы

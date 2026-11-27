def find_the_int():
    freakly_cifers = random.randint(1,100)
    user_trys = 0
    while True:
        try:
            user_guess = int(input("Введи число: "))
        except ValueError:
            print("ЧИСЛО, ИНФУЗОРИЯ!")
            user_trys += 1
        if user_trys > 10 or user_guess == 676767:
            give_up = input("Сдаешься?)").lower()
            if give_up == "yes" or give_up == "да":
                print(f"Игра окончена, загаданная цифра: {freakly_cifers}")
                break
            elif give_up != "yes" or give_up != "да":
                print("Ладно...")
                continue
        elif user_guess > 100:
            print("Я не загадываю такие большие числа")
        elif user_guess < freakly_cifers:
            print("У меня больше)")
            user_trys += 1
        elif user_guess > freakly_cifers:
            print("У меня меньше(")
            user_trys += 1
        elif user_guess == freakly_cifers:
            print(f"Молодец! ты угадал цифру с {user_trys} попыток!")
            break


while True:
    welcomin = input("Привет, телепат, готов сыграть в 'Yгадайку'? ").lower()
    if welcomin == "yes" or welcomin == "да" or welcomin == "88005553535":
        print("Отлично, тогда начнем.")
        find_the_int()
        break
    else:
        print("Ты не угадал моих намерений, попробуй еще)")

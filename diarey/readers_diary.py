lettersB = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
    'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
    'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]
lettersC = [ch.upper() for ch in lettersB]

n = 0
poop_list = []
while True:
    print("=== ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===")
    print("1 - Добавить книгу")
    print("2 - Показать все книги")
    print("3 - Показать последние  5 прочитанных книг")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("0 - Свалить")
    try:
            cheese = int(input("!): "))
    except ValueError:
            print("только цифры")
            n += 1

    if cheese == 1:
        while True:
            poop_across = input("Введите название книги: ").strip().lower()
            if poop_across != "" or poop_across != "                                                                                               ":
                poop_list.append(poop_across)
                n += 1
                break
            else:
                print("Вы ничего не ввели, попробуйте еще раз")
                n += 1

    elif cheese == 2:
        for sh in poop_list:
            indx = poop_list.index(sh)
            print(f"{indx+1}. {sh}")
            n += 1

    elif cheese == 3:
        try:
            print(poop_list.index(0),poop_list.index(1),poop_list.index(2),poop_list.index(3),poop_list.index(4))
        except ValueError:
            print("Произошла ошибка бебебебе")
        n += 1

    elif cheese == 4:
        pass
        n += 1

    elif cheese == 5:
        tralalelo_tralala = input("напишите название книги которую ххачитэ ноты: ")
        if tralalelo_tralala.lower() not in poop_list:
            print("пустыотыа ничигео ниет")
            n += 1
        elif tralalelo_tralala.lower() in poop_list:
            print(f"{poop_list.index(tralalelo_tralala)} --- {tralalelo_tralala}")
            n += 1

    elif cheese == 6:
        print(f"кароче ты умный и ваще крутой, по статистике ты рылся в этой проге {n} раз")

    elif cheese == 0:
        break

    else:
        print("что то не так...")

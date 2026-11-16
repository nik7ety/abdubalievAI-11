#Я ЕЩЕ НЕ ДОДЕЛАААААААААААААААААААЛ!!!!!!!!!!!!!!!!!!!!!!!!!
lettersB = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
    'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
    'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]
lettersC = [ch.upper() for ch in lettersB]

poop_list = []
while True:
    print("=== ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===")
    print("1 - Добавить книгу")
    print("2 - Показать все книги")
    print("3 - Показать последние  5 прочитанных ниг")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("0 - Свалить")
    cheese = input("!): ")
    if cheese in lettersB or cheese in lettersC:
        print("Напишите цифрой, идиот")
    elif cheese == "" or cheese == "           ":
        print("Вы должны хоть что то написать")

    elif cheese == "1":
        while True:
            poop_across = input("Введите название книги: ").strip()
            if poop_across != "" or poop_across != "                                                                                               ":
                poop_list.append(poop_across)
                break
            else:
                print("Вы ничего не ввели, попробуйте еще раз")

    elif cheese == "2":
        for sh in poop_list:
            indx = poop_list.index(sh)
            print(f"{indx+1}. {sh}")

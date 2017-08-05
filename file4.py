def ice():
    import question
    ice_cream = ["лимонное", "шоколадное", "пломбир"]
    print(" ")
    print("И какой вкус мороженого ты предпочитаешь?")
    for ctrl in ice_cream:
        print("   -", ctrl)
    choice_ice = input("")
    choice_ice = str(choice_ice.lower().strip())
    if choice_ice == "лимонное":
        question.lemon()
    elif choice_ice == "шоколадное":
        question.choc()
    elif choice_ice == "пломбир":
        question.white()


def cookies():
    import question
    cookies = ["треугольнички", "шоколадные трещинки", "брилиантовое"]
    print(" ")
    print("И какое печенье ты предпочитаешь?")
    for ctrl in cookies:
        print("   -", ctrl)
    choice_cookie = input("")
    choice_cookie = str(choice_cookie.lower().strip())
    if choice_cookie in cookies:
        if choice_cookie == "треугольнички":
            question.triangle()
        elif choice_cookie == "шоколадные трещинки":
            question.choc_cookie()
        elif choice_cookie == "брилиантовое":
            question.briliant()


def cakes():
    import question
    cakes = ["кофейно-сливочный", "пражский", "наполеон"]
    print(" ")
    print("И какой торт ты предпочитаешь?")
    for ctrl in cakes:
        print("   -", ctrl)
    choice_cake = input("")
    choice_cake = str(choice_cake.lower().strip())
    if choice_cake in cakes:
        if choice_cake == "кофейно-сливочный":
            question.coffee_cake()
        elif choice_cake == "пражский":
            question.praga()
        elif choice_cake == "наполеон":
            question.napoleon()
    else:
        print("")


def meal():
    repeat = True
    repeat1 = True
    while repeat:
        repeat = False
        meals = ["мороженое", "торт", "печеньки"]
        print("Могу предложить тебе несколько вариантов десертов.")
        print("У нас есть:")
        for ctrl in meals:
            print("   -", ctrl)
        choice_meal = input("Выбери из списка:")
        choice_meal = str(choice_meal.lower().strip())
        while repeat1:
            repeat1 = False
            if choice_meal in meals:
                if choice_meal == "мороженое":
                    ice()
                if choice_meal == "торт":
                    cakes()
                if choice_meal == "печеньки":
                    cookies()
            else:
                repeat = True
                print(" ")
                print("Извини, но у меня нет информиции о", choice_meal)
                print("Попробуй выбрать, что-нибудь другое.")
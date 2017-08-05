def lemonade():
    import question
    lemonades = ["имбирный", "с лавандой", "зеленый", "с мятой и лаймом", "просто лимонад"]
    print(" ")
    print("И какой вкус лимонада ты предпочитаешь?")
    for ctrl in lemonades:
        print("   -", ctrl)
    choice_ice = input("")
    choice_ice = str(choice_ice.lower().strip())
    if choice_ice == "имбирный":
        question.lemonade_gingery()
    elif choice_ice == "с лавандой":
        question.lemonade_lavender()
    elif (choice_ice == "зелёный") or (choice_ice == "зеленый"):
        question.lemonade_green()
    elif choice_ice == "с мятой и лаймом":
        question.lemonade_meantlime()
    elif choice_ice == "просто лимонад":
        question.lemonade()


def milkshakes():
    import question
    milk_shakes = ["шоколад", "карамель", "клубника", "ваниль"]
    print('С каким вкусом ты хочешь коктейль? Выбери из списка:')
    for ina in milk_shakes:
        print("   -", ina)
    choise_taste = input("С каким будешь вкусом?")
    choise_taste = str(choise_taste.lower().strip())
    if choise_taste in milk_shakes:
        question.milkshake()


def tea():
    import question
    teas = ['имбирный', 'с рябиной', 'шоколадный', 'яблочный с апельсином и корицей', '"здоровье"']
    print(" ")
    print("Вот какие у нас есть чаи:")
    for i in teas:
        print('   -', i)
    choise_teas = input('Какой именно чай тебе хочется сегодня приготовить? Выбери из списка:')
    if choise_teas == 'имбирный':
        question.tea_gingery()
    if choise_teas == 'с рябиной':
        question.tea_rowan()
    if choise_teas == 'шоколадный':
        question.tea_chocolate()
    if choise_teas == 'яблочный с апельсином и корицей':
        question.tea_orange_cinnamon()
    if choise_teas == '"здоровье"' or choise_teas == 'здоровье':
        question.tea_health()


def drinks():
    drinks = ["молочный коктейль", "чай", "лимонад"]
    print('Можешь выбрать из списка то, что ты хочешь приготовить сегодня.')
    print("У нас есть:")
    for x in drinks:
        print("   -", x)
    choise_drinks = input('Твой выбор: ')
    choise_drinks = str(choise_drinks.lower().strip())
    if choise_drinks in drinks:
        if choise_drinks == "молочный коктейль":
            milkshakes()
        if choise_drinks == "чай":
            tea()
        if choise_drinks == "лимонад":
            lemonade()
    else:
        print('Прости, у нас такого нет. Выбери что-нибудь другое!')
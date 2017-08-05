def tea_health():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть Половинка лайма?".lower().strip())
            if ingridients == "нет":
                a = "Половинка лайма"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть Половина стручка ванили?".lower().strip())
            if ingridients == "нет":
                b = "Половина стручка ванили"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть Горсть шиповника?".lower().strip())
            if ingridients == "нет":
                c = "Горсть шиповника"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 1 апельсин?".lower().strip())
            if ingridients == "нет":
                d = "1 апельсин"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть 1 палочка корицы?".lower().strip())
            if ingridients == "нет":
                e = "1 палочка корицы"
            elif ingridients == "да":
                e = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e]:
                print("	  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_tea_health()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть Половинка лайма?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть Половина стручка ванили?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть Горсть шиповника?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 1 апельсин?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть 1 палочка корицы?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                formula.printing_tea_health()
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_tea_health()


def tea_orange_cinnamon():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 2 столовых ложки меда?".lower().strip())
            if ingridients == "нет":
                a = "2 столовых ложки меда"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 3 чайных ложки крупнолистового черного чая?".lower().strip())
            if ingridients == "нет":
                b = "3 чайных ложки крупнолистового черного чая"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 2 яблока?".lower().strip())
            if ingridients == "нет":
                c = "2 яблока"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 1 апельсин?".lower().strip())
            if ingridients == "нет":
                d = "1 апельсин"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть 1 щепотка молотой корицы?".lower().strip())
            if ingridients == "нет":
                e = "1 щепотка молотой корицы"
            elif ingridients == "да":
                e = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_tea_orange_cinnamon()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 2 столовых ложки меда?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 3 чайных ложки крупнолистового черного чая?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 2 яблока?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 1 апельсин?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть 1 щепотка молотой корицы?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                formula.printing_tea_orange_cinnamon()
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_tea_orange_cinnamon()


def tea_chocolate():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 2 чайных ложки сухого молока?".lower().strip())
            if ingridients == "нет":
                a = "2 чайных ложки сухого молока"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 200 мл черного чая?".lower().strip())
            if ingridients == "нет":
                b = "200 мл черного чая"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 2 чайных ложки какао?".lower().strip())
            if ingridients == "нет":
                c = "2 чайных ложки какао"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть Молотая корица?".lower().strip())
            if ingridients == "нет":
                d = "Молотая корица"
            elif ingridients == "да":
                d = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_tea_chocolate()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 2 чайных ложки сухого молока?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 200 мл черного чая?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 2 чайных ложки какао?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть Молотая корица?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            formula.printing_tea_chocolate()
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_tea_chocolate()


def tea_rowan():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 3 грамма чорноплодной рябины?".lower().strip())
            if ingridients == "нет":
                a = "3 грамма чорноплодной рябины"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 1 столовая ложка черного чая?".lower().strip())
            if ingridients == "нет":
                b = "1 столовая ложка черного чая"
            elif ingridients == "да":
                b = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_tea_rowan()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 3 грамма чорноплодной рябины?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 1 столовая ложка черного чая?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    formula.printing_tea_rowan()
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_tea_rowan()


def tea_gingery():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть Половина корня имбиря?".lower().strip())
            if ingridients == "нет":
                a = "Половина корня имбиря"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть Лайм и мед?".lower().strip())
            if ingridients == "нет":
                b = "Лайм и мед"
            elif ingridients == "да":
                b = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_tea_gingery()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть Половина корня имбиря?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть Лайм и мед?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    formula.printing_tea_gingery()
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_tea_gingery()


def lemonade():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 1 кг сахара?".lower().strip())
            if ingridients == "нет":
                a = "1 кг сахара"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 3 лимона?".lower().strip())
            if ingridients == "нет":
                b = "3 лимона"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 2 литра воды?".lower().strip())
            if ingridients == "нет":
                c = "2 литра воды"
            elif ingridients == "да":
                c = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_lemonade()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 1 кг сахара?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 3 лимона?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 2 литра воды?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        formula.printing_lemonade()
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_lemonade()


def lemonade_meantlime():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть Пол пучка свежей мяты?".lower().strip())
            if ingridients == "нет":
                a = "Пол пучка свежей мяты"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 1 лайм?".lower().strip())
            if ingridients == "нет":
                b = "1 лайм"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 1 литр воды?".lower().strip())
            if ingridients == "нет":
                c = "1 литр воды"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть Сахар и лед?".lower().strip())
            if ingridients == "нет":
                d = "Сахар и лед"
            elif ingridients == "да":
                d = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_lemonade_meantlime()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть Пол пучка свежей мяты?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 1 лайм?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 1 литр воды?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть Сахар и лед?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            formula.printing_lemonade_meantlime()
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_lemonade_meantlime()


def lemonade_green():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 10 яблок?".lower().strip())
            if ingridients == "нет":
                a = "10 яблок"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 1 лимон?".lower().strip())
            if ingridients == "нет":
                b = "1 лимон"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 4 стебля сельдерея?".lower().strip())
            if ingridients == "нет":
                c = "4 стебля сельдерея"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 1 пучок кормовой капусты?".lower().strip())
            if ingridients == "нет":
                d = "1 пучок кормовой капусты"
            elif ingridients == "да":
                d = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_lemonade_green()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 10 яблок?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 1 лимон?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 4 стебля сельдерея?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 1 пучок кормовой капусты?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            formula.printing_lemonade_green()
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_lemonade_green()


def lemonade_lavender():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 2 столовых ложки сушоных листьев лаванды?".lower().strip())
            if ingridients == "нет":
                a = "2 столовых ложки сушоных листьев лаванды"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 3 лимона?".lower().strip())
            if ingridients == "нет":
                b = "3 лимона"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть Пол стакана сахара?".lower().strip())
            if ingridients == "нет":
                c = "Пол стакана сахара"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 4,5 стакана воды?".lower().strip())
            if ingridients == "нет":
                d = "4,5 стакана воды"
            elif ingridients == "да":
                d = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_lemonade_lavender()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 2 столовых ложки сушоных листьев лаванды?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 3 лимона?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть Пол стакана сахара?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 4,5 стакана воды?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            formula.printing_lemonade_lavender()
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_lemonade_lavender()


def lemonade_gingery():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 50 грамм тросникового сахара?".lower().strip())
            if ingridients == "нет":
                a = "50 грамм тросникового сахара"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 4 лимона?".lower().strip())
            if ingridients == "нет":
                b = "4 лимона"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 50 грамм имбиря?".lower().strip())
            if ingridients == "нет":
                c = "50 грамм имбиря"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 2 литра воды?".lower().strip())
            if ingridients == "нет":
                d = "2 литра воды"
            elif ingridients == "да":
                d = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_lemonade_gingery()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 50 грамм тросникового сахара?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 4 лимона?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 50 грамм имбиря?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 2 литра воды?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            formula.printing_lemonade_gingery()
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_lemonade_gingery()


def milkshake():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 100 грамм пломбира?".lower().strip())
            if ingridients == "нет":
                a = "100 грамм пломбира"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 100 мл молока?".lower().strip())
            if ingridients == "нет":
                b = "100 мл молока"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть Выбранный тобой топинг?".lower().strip())
            if ingridients == "нет":
                c = "Выбранный тобой топинг"
            elif ingridients == "да":
                c = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_milkshake()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 100 грамм пломбира?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 100 мл молока?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть Выбранный тобой топинг?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        formula.printing_milkshake()
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_milkshake()


def lemon():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 5 куриных яиц?".lower().strip())
            if ingridients == "нет":
                a = "5 куриных яиц"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 500мл 33% сливок?".lower().strip())
            if ingridients == "нет":
                b = "500мл 33% сливок"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 180гр сахара?".lower().strip())
            if ingridients == "нет":
                c = "180гр сахара"
            elif ingridients == "да":
                c = ""
            ingridients = input(
                "У тебя есть 3 ст.л. лимонной цедры (можно получить мелко натерев лимонную кожуру)?".lower().strip())
            if ingridients == "нет":
                d = "3 ст.л. лимонной цедры (можно получить мелко натерев лимонную кожуру)"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть 90мл лимонного сока?".lower().strip())
            if ingridients == "нет":
                e = "90мл лимонного сока"
            elif ingridients == "да":
                e = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.formula_limon_printing()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 5 куриных яиц?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 500мл 33% сливок?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 180гр сахара?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input(
                            "У тебя есть 3 ст.л. лимонной цедры (можно получить мелко натерев лимонную кожуру)?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть 90мл лимонного сока?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                formula.formula_limon_printing()
                            elif ingridients == "нет":
                                print("Ну что ж, тогда выбери другой рецепт.")
                        elif ingridients == "нет":
                            print("Ну что ж, тогда выбери другой рецепт.")
                    elif ingridients == "нет":
                        print("Ну что ж, тогда выбери другой рецепт.")
                elif ingridients == "нет":
                    print("Ну что ж, тогда выбери другой рецепт.")
            elif ingridients == "нет":
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.formula_limon_printing()


def choc():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
    market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
    market = str(market.lower().strip())
    if market == "да":
        print("Тогда давай решим, что тебе надо купить.")
        ingridients = input("У тебя есть Сливки 40% — 1 стакан?".lower().strip())
        if ingridients == "нет":
            a = "Сливки 40% — 1 стакан"
        elif ingridients == "да":
            a = ""
        ingridients = input("У тебя есть Сливки 18% — 240 мл?".lower().strip())
        if ingridients == "нет":
            b = "Сливки 18% — 240 мл"
        elif ingridients == "да":
            b = ""
        ingridients = input("У тебя есть Сахар — 0,5 стакана?".lower().strip())
        if ingridients == "нет":
            c = "Сахар — 0,5 стакана"
        elif ingridients == "да":
            c = ""
        ingridients = input("У тебя есть Ванильный сахар — 3\4 ч. ложки?".lower().strip())
        if ingridients == "нет":
            d = "Ванильный сахар — 3\4 ч. ложки"
        elif ingridients == "да":
            d = ""
        ingridients = input("У тебя есть Соль — небольшая щепотка?".lower().strip())
        if ingridients == "нет":
            e = "Соль — небольшая щепотка"
        elif ingridients == "да":
            e = ""
        ingridients = input(
            "У тебя есть У тебя есть Какао — 3 ст. ложки (или шоколадный сироп — 60 мл)?".lower().strip())
        if ingridients == "нет":
            f = "У тебя есть Какао — 3 ст. ложки (или шоколадный сироп — 60 мл)"
        elif ingridients == "да":
            f = ""
        print("Вот то, что тебе надо купить:")
        for x in [a, b, c, d, e, f]:
            print("  -", x)
        tratata = input("Ты уже купил всё что нужно?")
        repeat3 = True
        while repeat3:
            repeat3 = False
            if tratata == "да":
                formula.print_choco()
            else:
                print("Тогда быстро иди в магазин")
                repeat3 = True
    elif market == "нет":
        print(" ")
        print("Тогда давай разберёмся, что у тебя есть из продуктов.")
        ingridients = input("У тебя есть Сливки 40% — 1 стакан?")
        ingridients = str(ingridients.lower().strip())
        if ingridients == "да":
            ingridients = input("У тебя есть Сливки 18% — 240 мл?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть Сахар — 0,5 стакана?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть Ванильный сахар — 3\4 ч. ложки?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть Соль — небольшая щепотка?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть Какао — 3 ст. ложки (или шоколадный сироп — 60 мл)?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                formula.print_choco()
                            elif ingridients == "нет":
                                print("Ну что ж, тогда выбери другой рецепт.")
                        elif ingridients == "нет":
                            print("Ну что ж, тогда выбери другой рецепт.")
                    elif ingridients == "нет":
                        print("Ну что ж, тогда выбери другой рецепт.")
                elif ingridients == "нет":
                    print("Ну что ж, тогда выбери другой рецепт.")
            elif ingridients == "нет":
                print("Ну что ж, тогда выбери другой рецепт.")
        elif ingridients == "нет":
            print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.print_choco()


def white():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 4 желтка?".lower().strip())
            if ingridients == "нет":
                a = "4 желтка"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 90–100 г мелкокристаллического сахара?".lower().strip())
            if ingridients == "нет":
                b = "90–100 г мелкокристаллического сахара"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 1 стручок ванили?".lower().strip())
            if ingridients == "нет":
                c = "1 стручок ванили"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 250 мл молока 6%?".lower().strip())
            if ingridients == "нет":
                d = "250 мл молока 6%"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть 350 мл жирных сливок 38%?".lower().strip())
            if ingridients == "нет":
                e = "350 мл жирных сливок 38%"
            elif ingridients == "да":
                e = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.print_white()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 4 желтка?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 90–100 г мелкокристаллического сахара?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 1 стручок ванили?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 250 мл молока 6%?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть 350 мл жирных сливок 38%?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                formula.print_white()
                            elif ingridients == "нет":
                                print("Ну что ж, тогда выбери другой рецепт.")
                        elif ingridients == "нет":
                            print("Ну что ж, тогда выбери другой рецепт.")
                    elif ingridients == "нет":
                        print("Ну что ж, тогда выбери другой рецепт.")
                elif ingridients == "нет":
                    print("Ну что ж, тогда выбери другой рецепт.")
            elif ingridients == "нет":
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.print_white()


def coffee_cake():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 3 яйца?".lower().strip())
            if ingridients == "нет":
                a = "3 яйца"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 225г растительного масла?".lower().strip())
            if ingridients == "нет":
                b = "225г растительного масла"
            elif ingridients == "да":
                b = ""
            ingridients = input(
                "У тебя есть 0.5 стакана сахара + 1/3 стакана сахара + 2 чайных ложки сахара?".lower().strip())
            if ingridients == "нет":
                c = "0.5 стакана сахара + 1/3 стакана сахара + 2 чайных ложки сахара"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 10г какао?".lower().strip())
            if ingridients == "нет":
                d = "10г какао"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть 80г муки?".lower().strip())
            if ingridients == "нет":
                e = "80г муки"
            elif ingridients == "да":
                e = ""
            ingridients = input("У тебя есть 1.5 чайных ложки разрыхлителя?".lower().strip())
            if ingridients == "нет":
                f = "1.5 чайных ложки разрыхлителя"
            elif ingridients == "да":
                f = ""
            ingridients = input("У тебя есть ванилин?".lower().strip())
            if ingridients == "нет":
                g = "ванилин"
            elif ingridients == "да":
                g = ""
            ingridients = input("У тебя есть 0.5 стакана молока + 250г молока?".lower().strip())
            if ingridients == "нет":
                h = "0.5 стакана молока + 250г молока"
            elif ingridients == "да":
                h = ""
            ingridients = input("У тебя есть 1 чайная ложка муки?".lower().strip())
            if ingridients == "нет":
                i = "1 чайная ложка муки"
            elif ingridients == "да":
                i = ""
            ingridients = input("У тебя есть 1 столовая ложка растворимого кофе?".lower().strip())
            if ingridients == "нет":
                j = "1 столовая ложка растворимого кофе"
            elif ingridients == "да":
                j = ""
            ingridients = input("У тебя есть 300г 30~50% сливок?".lower().strip())
            if ingridients == "нет":
                k = "300г 30~50% сливок"
            elif ingridients == "да":
                k = ""
            ingridients = input("У тебя есть 15г желатина?".lower().strip())
            if ingridients == "нет":
                l = "15г желатина"
            elif ingridients == "да":
                l = ""
            ingridients = input("У тебя есть 2/3  стакана сахарной пудры?".lower().strip())
            if ingridients == "нет":
                m = "2/3  стакана сахарной пудры"
            elif ingridients == "да":
                m = ""
            ingridients = input("У тебя есть 50г воды?".lower().strip())
            if ingridients == "нет":
                n = "50г воды"
            elif ingridients == "да":
                n = ""
            ingridients = input("У тебя есть 2 чайных ложки коньяка?".lower().strip())
            if ingridients == "нет":
                o = "2 чайных ложки коньяка"
            elif ingridients == "да":
                o = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.print_coffee_cake()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 3 яйца?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 225г растительного масла?".lower().strip())
                if ingridients == "да":
                    ingridients = input(
                        "У тебя есть 0.5 стакана сахара + 1/3 стакана сахара + 2 чайных ложки сахара?".lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 10г какао?".lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть 80г муки?".lower().strip())
                            if ingridients == "да":
                                ingridients = input("У тебя есть 1.5 чайных ложки разрыхлителя?".lower().strip())
                                if ingridients == "да":
                                    ingridients = input("У тебя есть ванилин?".lower().strip())
                                    if ingridients == "да":
                                        ingridients = input(
                                            "У тебя есть 0.5 стакана молока + 250г молока?".lower().strip())
                                        if ingridients == "да":
                                            ingridients = input("У тебя есть 1 чайная ложка муки?".lower().strip())
                                            if ingridients == "да":
                                                ingridients = input(
                                                    "У тебя есть 1 столовая ложка растворимого кофе?".lower().strip())
                                                if ingridients == "да":
                                                    ingridients = input(
                                                        "У тебя есть 300г 30~50% сливок?".lower().strip())
                                                    if ingridients == "да":
                                                        ingridients = input("У тебя есть 15г желатина?".lower().strip())
                                                        if ingridients == "да":
                                                            ingridients = input(
                                                                "У тебя есть 2/3  стакана сахарной пудры?")
                                                            if ingridients == "да":
                                                                ingridients = input(
                                                                    "У тебя есть 50г воды?".lower().strip())
                                                                if ingridients == "да":
                                                                    ingridients = input(
                                                                        "У тебя есть 2 чайных ложки коньяка?".lower().strip())
                                                                    if ingridients == "да":
                                                                        formula.print_coffee_cake()
                                                                    else:
                                                                        print("Ну что ж, тогда выбери другой рецепт.")
                                                                else:
                                                                    print("Ну что ж, тогда выбери другой рецепт.")
                                                            else:
                                                                print("Ну что ж, тогда выбери другой рецепт.")
                                                        else:
                                                            print("Ну что ж, тогда выбери другой рецепт.")
                                                    else:
                                                        print("Ну что ж, тогда выбери другой рецепт.")
                                                else:
                                                    print("Ну что ж, тогда выбери другой рецепт.")
                                            else:
                                                print("Ну что ж, тогда выбери другой рецепт.")
                                        else:
                                            print("Ну что ж, тогда выбери другой рецепт.")
                                    else:
                                        print("Ну что ж, тогда выбери другой рецепт.")
                                else:
                                    print("Ну что ж, тогда выбери другой рецепт.")
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.print_coffee_cake()


def praga():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 2 яйца?".lower().strip())
            if ingridients == "нет":
                a = "2 яйца"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 300г сметаны?".lower().strip())
            if ingridients == "нет":
                b = "300г сметаны"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 1.5 стакана + 3 столовых ложки сахара?".lower().strip())
            if ingridients == "нет":
                c = "1.5 стакана + 3 столовых ложки сахара"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 3 чайных + 3 столовых ложки какао?".lower().strip())
            if ingridients == "нет":
                d = "3 чайных + 3 столовых ложки какао"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть 1/2 ложки соды?".lower().strip())
            if ingridients == "нет":
                e = "1/2 ложки соды"
            elif ingridients == "да":
                e = ""
            ingridients = input("У тебя есть 2 пакетика ванилина?".lower().strip())
            if ingridients == "нет":
                f = "2 пакетика ванилина"
            elif ingridients == "да":
                f = ""
            ingridients = input("У тебя есть 350г сливочного масла?".lower().strip())
            if ingridients == "нет":
                g = "350г сливочного масла"
            elif ingridients == "да":
                g = ""
            ingridients = input("У тебя есть 1 банка сгущённого молока с какао?".lower().strip())
            if ingridients == "нет":
                h = "1 банка сгущённого молока с какао"
            elif ingridients == "да":
                h = ""
            ingridients = input("У тебя есть 3/4 стакана воды?".lower().strip())
            if ingridients == "нет":
                i = "3/4 стакана воды"
            elif ingridients == "да":
                i = ""
            ingridients = input("У тебя есть 1 столовая ложка коньяка?".lower().strip())
            if ingridients == "нет":
                j = "1 столовая ложка коньяка"
            elif ingridients == "да":
                j = ""
            ingridients = input("У тебя есть 1/2 чайной ложки соли?".lower().strip())
            if ingridients == "нет":
                k = "1/2 чайной ложки соли"
            elif ingridients == "да":
                k = ""
            ingridients = input("У тебя есть 50~100г шоколада?".lower().strip())
            if ingridients == "нет":
                l = "50~100г шоколада"
            elif ingridients == "да":
                l = ""
            ingridients = input("У тебя есть 1 стакан сахарной пудры?".lower().strip())
            if ingridients == "нет":
                m = "1 стакан сахарной пудры"
            elif ingridients == "да":
                m = ""
            ingridients = input("У тебя есть 1 столовая ложка крахмала?".lower().strip())
            if ingridients == "нет":
                n = "1 столовая ложка крахмала"
            elif ingridients == "да":
                n = ""
            ingridients = input("У тебя есть 5 столовых ложек молока?".lower().strip())
            if ingridients == "нет":
                o = "5 столовых ложек молока"
            elif ingridients == "да":
                o = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.print_prague_cake()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 2 яйца?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 300г сметаны?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 1.5 стакана + 3 столовых ложки сахара?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 1.5 стакана муки?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть 3 чайных + 3 столовых ложки какао?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                ingridients = input("У тебя есть 1/2 ложки соды?")
                                ingridients = str(ingridients.lower().strip())
                                if ingridients == "да":
                                    ingridients = input("У тебя есть 2 пакетика ванилина?")
                                    ingridients = str(ingridients.lower().strip())
                                    if ingridients == "да":
                                        ingridients = input("У тебя есть 350г сливочного масла?")
                                        ingridients = str(ingridients.lower().strip())
                                        if ingridients == "да":
                                            ingridients = input("У тебя есть 1 банка сгущённого молока с какао?")
                                            ingridients = str(ingridients.lower().strip())
                                            if ingridients == "да":
                                                ingridients = input("У тебя есть 3/4 стакана воды?")
                                                ingridients = str(ingridients.lower().strip())
                                                if ingridients == "да":
                                                    ingridients = input("У тебя есть 1 столовая ложка коньяка?")
                                                    ingridients = str(ingridients.lower().strip())
                                                    if ingridients == "да":
                                                        ingridients = input("У тебя есть 1/2 чайной ложки соли?")
                                                        ingridients = str(ingridients.lower().strip())
                                                        if ingridients == "да":
                                                            ingridients = input("У тебя есть 50~100г шоколада?")
                                                            ingridients = str(ingridients.lower().strip())
                                                            if ingridients == "да":
                                                                ingridients = input(
                                                                    "У тебя есть 1 стакан сахарной пудры?")
                                                                ingridients = str(ingridients.lower().strip())
                                                                if ingridients == "да":
                                                                    ingridients = input(
                                                                        "У тебя есть 5 столовых ложек молока?")
                                                                    ingridients = str(ingridients.lower().strip())
                                                                    if ingridients == "да":
                                                                        ingridients = input(
                                                                            "У тебя есть 1 столовая ложка крахмала?")
                                                                        ingridients = str(ingridients.lower().strip())
                                                                        if ingridients == "да":
                                                                            formula.print_prague_cake()
                                                                        else:
                                                                            print(
                                                                                "Ну что ж, тогда выбери другой рецепт.")
                                                                    else:
                                                                        print("Ну что ж, тогда выбери другой рецепт.")
                                                                else:
                                                                    print("Ну что ж, тогда выбери другой рецепт.")
                                                            else:
                                                                print("Ну что ж, тогда выбери другой рецепт.")
                                                        else:
                                                            print("Ну что ж, тогда выбери другой рецепт.")
                                                    else:
                                                        print("Ну что ж, тогда выбери другой рецепт.")
                                                else:
                                                    print("Ну что ж, тогда выбери другой рецепт.")
                                            else:
                                                print("Ну что ж, тогда выбери другой рецепт.")
                                        else:
                                            print("Ну что ж, тогда выбери другой рецепт.")
                                    else:
                                        print("Ну что ж, тогда выбери другой рецепт.")
                                else:
                                    print("Ну что ж, тогда выбери другой рецепт.")
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.print_prague_cake()


def napoleon():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть 2 стакана муки?".lower().strip())
            if ingridients == "нет":
                a = "2 стакана муки"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть 200г маргарина?".lower().strip())
            if ingridients == "нет":
                b = "200г маргарина"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть 1 стакан сметаны?".lower().strip())
            if ingridients == "нет":
                c = "1 стакан сметаны"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть 1 столовая ложка водки?".lower().strip())
            if ingridients == "нет":
                d = "1 столовая ложка водки"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть 200г сливочного масла?".lower().strip())
            if ingridients == "нет":
                e = "200г сливочного масла"
            elif ingridients == "да":
                e = ""
            ingridients = input("У тебя есть 0.5 стакана молока?".lower().strip())
            if ingridients == "нет":
                f = "0.5 стакана молока"
            elif ingridients == "да":
                f = ""
            ingridients = input("У тебя есть 1 стакан сахара?".lower().strip())
            if ingridients == "нет":
                g = "1 стакан сахара"
            elif ingridients == "да":
                g = ""
            ingridients = input("У тебя есть 1 яйцо?".lower().strip())
            if ingridients == "нет":
                h = "1 яйцо"
            elif ingridients == "да":
                h = ""
            ingridients = input("У тебя есть0.5 порошка ванилина или 2~3 столовых ложки коньяка?".lower().strip())
            if ingridients == "нет":
                i = "0.5 порошка ванилина или 2~3 столовых ложки коньяка"
            elif ingridients == "да":
                i = ""
            ingridients = input("У тебя есть 0.5 литра сметаны или сливок?".lower().strip())
            if ingridients == "нет":
                j = "0.5 литра сметаны или сливок"
            elif ingridients == "да":
                j = ""
            ingridients = input("У тебя есть 1 стакан сахарной пудры?".lower().strip())
            if ingridients == "нет":
                k = "1 стакан сахарной пудры"
            elif ingridients == "да":
                k = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e, f, g, h, i, j, k]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.print_napoleon_cake()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть 2 стакана муки?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть 200г маргарина?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть 1 стакан сметаны?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть 1 столовая ложка водки?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть 200г сливочного масла?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                ingridients = input("У тебя есть 0.5 стакана молока?")
                                ingridients = str(ingridients.lower().strip())
                                if ingridients == "да":
                                    ingridients = input("У тебя есть 1 стакан сахара?")
                                    ingridients = str(ingridients.lower().strip())
                                    if ingridients == "да":
                                        ingridients = input("У тебя есть 1 яйцо?")
                                        ingridients = str(ingridients.lower().strip())
                                        if ingridients == "да":
                                            ingridients = input(
                                                "У тебя есть 0.5 порошка ванилина или 2~3 столовых ложки коньяка?")
                                            ingridients = str(ingridients.lower().strip())
                                            if ingridients == "да":
                                                ingridients = input("У тебя есть 0.5 литра сметаны или сливок?")
                                                ingridients = str(ingridients.lower().strip())
                                                if ingridients == "да":
                                                    ingridients = input("У тебя есть 1 стакан сахарной пудры?")
                                                    ingridients = str(ingridients.lower().strip())
                                                    if ingridients == "да":
                                                        formula.print_napoleon_cake()
                                                    else:
                                                        print("Ну что ж, тогда выбери другой рецепт.")
                                                else:
                                                    print("Ну что ж, тогда выбери другой рецепт.")
                                            else:
                                                print("Ну что ж, тогда выбери другой рецепт.")
                                        else:
                                            print("Ну что ж, тогда выбери другой рецепт.")
                                    else:
                                        print("Ну что ж, тогда выбери другой рецепт.")
                                else:
                                    print("Ну что ж, тогда выбери другой рецепт.")
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.print_napoleon_cake()


def choc_cookie():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть Шоколад (черный) — 170 г?".lower().strip())
            if ingridients == "нет":
                a = "Шоколад (черный) — 170 г"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть Масло сливочное — 60 г?".lower().strip())
            if ingridients == "нет":
                b = "Масло сливочное — 60 г"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть Сахар — 100 г?".lower().strip())
            if ingridients == "нет":
                c = "Сахар — 100 г"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть Яйцо куриное	— 2 шт?".lower().strip())
            if ingridients == "нет":
                d = "Яйцо куриное	— 2 шт"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть Разрыхлитель теста — 3/4 ч. л.?".lower().strip())
            if ingridients == "нет":
                e = "Разрыхлитель теста — 3/4 ч. л."
            elif ingridients == "да":
                e = ""
            ingridients = input("У тебя есть Ванилин — 1 ч. л.?".lower().strip())
            if ingridients == "нет":
                f = "Ванилин — 1 ч. л."
            elif ingridients == "да":
                f = ""
            ingridients = input("У тебя есть Сахарная пудра (для присыпки)?".lower().strip())
            if ingridients == "нет":
                g = "Сахарная пудра (для присыпки)"
            elif ingridients == "да":
                g = ""
            ingridients = input("У тебя есть Мука — 200 г?".lower().strip())
            if ingridients == "нет":
                h = "Мука — 200 г"
            elif ingridients == "да":
                h = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e, f, g, h]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_choc()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть Шоколад (черный) — 170 г?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть Масло сливочное — 60 г?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть Сахар — 100 г?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть Яйцо куриное	— 2 шт?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть Разрыхлитель теста — 3/4 ч. л.?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                ingridients = input("У тебя есть Соль — 1/4 ч. л.?")
                                ingridients = str(ingridients.lower().strip())
                                if ingridients == "да":
                                    ingridients = input("У тебя есть Ванилин — 1 ч. л.?")
                                    ingridients = str(ingridients.lower().strip())
                                    if ingridients == "да":
                                        ingridients = input("У тебя есть Сахарная пудра (для присыпки)?")
                                        ingridients = str(ingridients.lower().strip())
                                        if ingridients == "да":
                                            ingridients = input("У тебя есть Мука — 200 г?")
                                            ingridients = str(ingridients.lower().strip())
                                            if ingridients == "да":
                                                formula.printing_choc()
                                            else:
                                                print("Ну что ж, тогда выбери другой рецепт.")
                                        else:
                                            print("Ну что ж, тогда выбери другой рецепт.")
                                    else:
                                        print("Ну что ж, тогда выбери другой рецепт.")
                                else:
                                    print("Ну что ж, тогда выбери другой рецепт.")
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_choc()


def briliant():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть Масло сливочное (комнатной температуры) — 230 г?".lower().strip())
            if ingridients == "нет":
                a = "Масло сливочное (комнатной температуры) — 230 г"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть Сахарная пудра (важно! не сахар) — 105 г?".lower().strip())
            if ingridients == "нет":
                b = "Сахарная пудра (важно! не сахар) — 105 г"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть Мука пшеничная — 330 г?".lower().strip())
            if ingridients == "нет":
                c = "Мука пшеничная — 330 г"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть Ванильная эссенция — 0,5 ч. л.?".lower().strip())
            if ingridients == "нет":
                d = "Ванильная эссенция — 0,5 ч. л."
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть Соль — 0,25 ч. л.?".lower().strip())
            if ingridients == "нет":
                e = "Соль — 0,25 ч. л."
            elif ingridients == "да":
                e = ""
            ingridients = input("У тебя есть Сахар или мак (для посыпки)?".lower().strip())
            if ingridients == "нет":
                f = "Сахар или мак (для посыпки)"
            elif ingridients == "да":
                f = ""
            ingridients = input("У тебя есть Яйцо куриное — 1 шт?".lower().strip())
            if ingridients == "нет":
                g = "Яйцо куриное — 1 шт"
            elif ingridients == "да":
                g = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e, f, g]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_briliant()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть Масло сливочное (комнатной температуры) — 230 г?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть Сахарная пудра (важно! не сахар) — 105 г?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть Мука пшеничная — 330 г?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть Ванильная эссенция — 0,5 ч. л.?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть Соль — 0,25 ч. л.?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                ingridients = input("У тебя есть Сахар или мак (для посыпки)?")
                                ingridients = str(ingridients.lower().strip())
                                if ingridients == "да":
                                    ingridients = input("У тебя есть Яйцо куриное — 1 шт?")
                                    ingridients = str(ingridients.lower().strip())
                                    if ingridients == "да":
                                        formula.printing_briliant()
                                    else:
                                        print("Ну что ж, тогда выбери другой рецепт.")
                                else:
                                    print("Ну что ж, тогда выбери другой рецепт.")
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_briliant()


def triangle():
    import formula
    print(" ")
    print("Ты хочешь начать готовить сейчас или просто посмотреть рецепт?")
    forma = input('''	-рецепт
	-сейчас''')
    if forma == "сейчас":
        print(" ")
        market = input("Пойдёшь в магазин если чего-нибудь не будет хватать для приготовления?")
        market = str(market.lower().strip())
        if market == "да":
            print("Тогда давай решим, что тебе надо купить.")
            ingridients = input("У тебя есть Мука — 300 г?".lower().strip())
            if ingridients == "нет":
                a = "Мука — 300 г"
            elif ingridients == "да":
                a = ""
            ingridients = input("У тебя есть Маргарин (или масло) — 120 г?".lower().strip())
            if ingridients == "нет":
                b = "Маргарин (или масло) — 120 г"
            elif ingridients == "да":
                b = ""
            ingridients = input("У тебя есть Молоко — 120 мл?".lower().strip())
            if ingridients == "нет":
                c = "Молоко — 120 мл"
            elif ingridients == "да":
                c = ""
            ingridients = input("У тебя есть Сахар — 100 г?".lower().strip())
            if ingridients == "нет":
                d = "Сахар — 100 г"
            elif ingridients == "да":
                d = ""
            ingridients = input("У тебя есть Дрожжи (сухие) — 1 ч. л.?".lower().strip())
            if ingridients == "нет":
                e = "Дрожжи (сухие) — 1 ч. л."
            elif ingridients == "да":
                e = ""
            ingridients = input("У тебя есть Соль (щепотка)?".lower().strip())
            if ingridients == "нет":
                f = "Соль (щепотка)"
            elif ingridients == "да":
                f = ""
            print("Вот то, что тебе надо купить:")
            for x in [a, b, c, d, e, f]:
                print("  -", x)
            tratata = input("Ты уже купил всё что нужно?")
            repeat3 = True
            while repeat3:
                repeat3 = False
                if tratata == "да":
                    formula.printing_triangle()
                else:
                    print("Тогда быстро иди в магазин")
                    repeat3 = True
        elif market == "нет":
            print(" ")
            print("Тогда давай разберёмся, что у тебя есть из продуктов.")
            ingridients = input("У тебя есть Мука — 300 г?")
            ingridients = str(ingridients.lower().strip())
            if ingridients == "да":
                ingridients = input("У тебя есть Маргарин (или масло) — 120 г?")
                ingridients = str(ingridients.lower().strip())
                if ingridients == "да":
                    ingridients = input("У тебя есть Молоко — 120 мл?")
                    ingridients = str(ingridients.lower().strip())
                    if ingridients == "да":
                        ingridients = input("У тебя есть Сахар — 100 г?")
                        ingridients = str(ingridients.lower().strip())
                        if ingridients == "да":
                            ingridients = input("У тебя есть Дрожжи (сухие) — 1 ч. л.?")
                            ingridients = str(ingridients.lower().strip())
                            if ingridients == "да":
                                ingridients = input("У тебя есть Соль (щепотка)?")
                                ingridients = str(ingridients.lower().strip())
                                if ingridients == "да":
                                    formula.printing_triangle()
                                else:
                                    print("Ну что ж, тогда выбери другой рецепт.")
                            else:
                                print("Ну что ж, тогда выбери другой рецепт.")
                        else:
                            print("Ну что ж, тогда выбери другой рецепт.")
                    else:
                        print("Ну что ж, тогда выбери другой рецепт.")
                else:
                    print("Ну что ж, тогда выбери другой рецепт.")
            else:
                print("Ну что ж, тогда выбери другой рецепт.")
    elif forma == "рецепт":
        formula.printing_triangle()
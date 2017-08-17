# -*- coding: utf-8 -*-
from tkinter import *
'''Файл с функцией для создания своего собственного рецепта'''
def create_recipe(event):
    def save(event):
        '''Функция которая принимает и сохраняет данные с текстовых полей для ингредиентов и способа приготовления блюда'''
        global title
        title = entry_1.get()
        file = open(fileway + title + '.txt', 'x')    # аргумент х позволяет создать новый файл и записать туда полученый текст

        text_ingredients = text_1.get(1.0, END)
        text_cooking = text_2.get(1.0,END)
        file.write(title)
        file.write('\nИнгредиенты\n')
        file.write(text_ingredients)
        file.write('\nСпособ приготовления\n')
        file.write(text_cooking)
        file.close()

    def category(event):
        '''Функция которая в зависимости от выбраной радиокнопки определяет категорию, а тойсть путь сохранения файла'''
        a = var.get()
        global fileway
        if a == 0:
            fileway = 'Рецепты/Салаты/'
        elif a == 1:
            fileway = 'Рецепты/Первое блюдо/'
        elif a == 2:
            fileway = 'Рецепты/Основное блюдо/'
        elif a == 3:
            fileway = 'Рецепты/Гарниры/'
        elif a == 4:
            fileway = 'Рецепты/Десерты/'
        elif a == 5:
            fileway = 'Рецепты/Напитки/'

    def close(event):   # функция которая закрывает окно
        root.destroy()

    root = Toplevel()
    root.geometry('800x800+200+0')
    root.title('EasyMeal')

    frame_2 = Frame(root, width = 1000, height = 300, bg = '#3dbde0')
    frame_2.place(x = 0, y = 740)

    label_1 = Label(root, text = 'Название рецепта:', font = 'Calibri 13 bold italic')
    entry_1 = Entry(root, width = 50)
    label_1.pack()
    entry_1.pack()

    #label_2 = Label(root, text = 'Сюда введи сам рецепт')

    frame_1 = Frame(root, width = 500, height = 20)
    frame_1.pack()

    frame = Frame(root, width = 10000, height =500)
    frame.pack()

    label_3 = Label(root, text = 'Ингредиенты:', font = 'Calibri 13 bold italic')
    text_1 = Text(root, width = 40, height = 12, wrap = WORD)
    #ingredients = text_1.get(1.0, END)
    #text_1.tag_add(ingredients, '1.0', END)
    #text_1.insert(1.0, ingredients)
    #text_1.mark_set('Ингредиенты:', 2.0)
    #text_1.mark_gravity('Ингредиенты:', LEFT)
    label_3.place(x= 175, y = 55)
    text_1.place(x = 70, y = 90)

    label_4 = Label(root, text = 'Категория:', font = 'Calibri 13 bold italic')
    var = IntVar()
    var.set(0)
    category_1 = Radiobutton(root, text = 'Салаты', variable = var, value = 0, font = 'Calibri 13 italic')
    category_2 = Radiobutton(root, text = 'Первые блюда', variable = var, value = 1, font = 'Calibri 13 italic')
    category_3 = Radiobutton(root, text = 'Основные блюда', variable = var, value = 2, font = 'Calibri 13 italic')
    category_4 = Radiobutton(root, text = 'Гарниры', variable = var, value = 3, font = 'Calibri 13 italic')
    category_5 = Radiobutton(root, text = 'Десерты', variable = var, value = 4, font = 'Calibri 13 italic')
    category_6 = Radiobutton(root, text = 'Напитки', variable = var, value = 5, font = 'Calibri 13 italic')

    label_4.place(x = 530, y = 55)
    category_1.place(x = 570, y = 80)
    category_2.place(x = 570, y = 105)
    category_3.place(x = 570, y = 130)
    category_4.place(x = 570, y = 155)
    category_5.place(x = 570, y = 180)
    category_6.place(x = 570, y = 205)

    label_5 = Label(root, text = 'Способ приготовления:', font = 'Calibri 13 bold italic')
    text_2 = Text(root, width = 70, height = 20, wrap = WORD)
    #scr = Scrollbar(root, command=text_2.yview)
    #text_2.configure(yscrollcommand=scr.set)
    #scr.pack()

    text_2.mark_set('Способ приготовления:', 2.0)
    text_2.mark_gravity('Способ приготовления:', RIGHT)
    label_5.place(x = 260, y = 300)
    text_2.place(x = 40, y = 330)

    button = Button(root, text = 'Сохранить рецепт', bg = '#3dbde0', font = 'Calibri 12 bold italic')
    button.place(x = 630, y = 650)

    button_1 = Button(root, text = 'OK', bg = '#3dbde0', font = 'Calibri 12 bold ')
    button_1.place(x = 600, y = 240)
    button_1.bind("<Button-1>", category)

    button.bind("<Button-1>", save)
    button.bind("<Double-Button-1>", close)

    root.mainloop()
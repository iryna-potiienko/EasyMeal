# -*- coding: utf-8 -*-
import write_recipes
from os import listdir
from os.path import isfile
from os.path import join as joinpath
#import ImageTkInter   # Добавить гиперлынк (кнопка заказать товары)
                                # Вставить логотип
from tkinter import *       # Проблемы с расширением

root = Tk()
root.title('EasyMeal')
root.geometry('500x300')
root['bg'] = '#3dbde0'
#image = Image.open("lenna.jpg")
#photo = ImageTk.PhotoImage(image)
#im = Image.open('фон.jpg')
#ph_im = ImageTk.PhotoImage(im)
#bd = Label(root, image=bg_image)
#bd.pack()

def sorting(event):
    '''Функция которая открывает дочернее окно с рецептом и выборкой ингредиентов'''
    def exit(event):
        root.quit()
    def buy_products(event):
        a = text.get(1.0, END)
        import webbrowser
        webbrowser.open("http://fozzyshop.com.ua/?gclid=Cj0KEQjwt8rMBRDOqoKWjJfd_LABEiQA2F2biNjCv--MPLRGy1nptmCIxjSKk0_ainr1oZNGxWgdOwAaAiev8P8HAQ")
    global list, a, sos, b
    c = event.widget['text']
    root = Toplevel()
    #root.iconbitmap('logo end.png')
    root.title('EasyMeal')
    root.geometry('1400x800+0+0')
    fram = Frame(root, width = 1700, height = 50, bg = 'black')
    fram.pack()
    fram_1 = Frame(root, width = 100, height = 1000)
    fram_1.pack(side = LEFT)
    frame = Frame(root, height = 1000, width = 20)
    frame.pack(side = LEFT)
    frame_1 = Frame(frame, height=500, width=20)
    frame_1.pack(side = LEFT)
    frame_2 = Frame(root, height=500, width=1500, bg = '#3dbde0')
    frame_2.place(x = 0, y = 750)
    label = Label(frame_1, text='Кликните на ингредиенты которих у вас нету:', font='Calibri 14 bold italic')
    # label.place(x = 50, y = 20)
    label.pack()

    file = open(filename + c + '.txt')
    #a = file.readline(1.0)
    #file.delete(1.0, 2.0)
    #for i, list in enumerate(file):
     #   if i >= 2:              # чтение файла начиная со второй строчки
    a = file.readlines(12)
    b = file.readlines(1)
    list = file.readline()
    list = list.rstrip('\n')

    while list != '':   # цикл для определения какие продукты есть для приготовления, а каких нету
                    if list == a or list == b:
                        lab = Label(root)
                    if list[0:2:1] == 'Для':
                        lab1 = Label()
                    check = Button(frame_1, text=list, width = 60, bg = '#3dbde0', font = 'Calibri 13 italic')
                    check.pack(side = TOP)
                    list = file.readline()
                    list = list.rstrip('\n')


                    def change(event):   # при нажатии на кнопку она станет красной и продукт появится в текстовом поле внизу
                        global a
                        event.widget['bg'] = 'red'
                        print(event.widget['text'])
                        text.insert(END, event.widget['text'])
                        text.insert(END, '\n')

                    def returning(event):   # при двойном нажатии на кнопку функция отменит функцию change()
                        event.widget['bg'] = '#3dbde0'
                        text.replace(event.widget['text'], "")
                        #text.delete()

                    check.bind('<Button-1>', change)
                    check.bind('<Double-Button-1>', returning)
    file = open(filename + c + '.txt')
    file = file.read()
    label_title = Label(root, text = c, font = 'Calibri 18 bold', fg = 'white', bg = 'black')
    label_title.place(x = 600, y = 5)
    text_recipe = Text(root, wrap = WORD, width = 60, height = 25)
    text_recipe.insert(1.0, file)
    button_ok = Button(root, text='Выйти', bg = '#3dbde0', font = 'Calibri 14 bold')
    button_ok.bind('<Button-1>', exit)
    button_ok.place(x = 1325, y = 5)
    lab = Label(root, text = 'А вот что надо докупить:', font = 'Calibri 14 bold italic')
    lab.place(x = 800, y = 475)
    text = Text(root, width = 55, height = 13)
    text.place(x = 800, y = 520)
    text_recipe.place(x = 800, y = 60)
    button_search = Button(root, text = 'Заказать недостающие продукты', bg = '#3dbde0', font = 'Calibri 14 bold')
    button_search.bind('<Button-1>', buy_products)
    button_search.place(x = 1025, y= 5)

def file_title(event):
    '''Функция которая показывает список текстовых файлов в папке - список рецептов выбранной категории'''
    global filename
    root = Toplevel()
    root.title('EasyMeal')
    root.geometry('500x540')
    #frame1 = Frame(root, width = 700, height = 0)
    #frame1.pack()
    frame2 = Frame(root, width = 500, height = 300)
    frame3 = Frame(root, width = 500, height = 100, bg = '#3dbde0')
    frame3.place(x = 0, y = 500)
    label = Label(frame2, text = 'Выберите блюдо:', font = 'Calibri 20 bold italic')
    label.pack()
    mypath = 'Рецепты/' + event.widget['text']
    for i in listdir(mypath):
        if isfile(joinpath(mypath,i)):
            i = i[0:-4]
            filename = mypath + '/'
            but = Button(frame2, text = i, width=32, height = 1, bg = '#3dbde0', font = 'Calibri 14 italic')
            but.bind('<Button-1>', sorting)
            but.pack()
            frame = Frame(root, width = 620, height = 2)
            frame.pack()
    frame2.pack()

def new_window(event):
    '''Функция которая открывает окно с рецептами'''
    def closing(event):
        window.destroy()
    window = Toplevel(root)
    root.title('EasyMeal')
    window.geometry('620x450')
    window['bg'] = '#3dbde0'
    frame = Frame(window, width = 620, height = 350)
    frame.pack()
    lab1 = Label(window, font = 'Calibri 20 bold italic', text=''' Хорошо, мы будем готовить! 
    Что мы хотим приготовить сегодня?''')
    but3 = Button(window, text='Салаты', width=15, height = 2, bg = '#3dbde0', font = 'Calibri 15 bold italic')
    but4 = Button(window, text='Первое блюдо', width=15, height = 2, bg = '#3dbde0', font = 'Calibri 15 bold italic')
    but5 = Button(window, text='Основное блюдо', width=15, height = 2, bg = '#3dbde0', font = 'Calibri 15 bold italic')
    but6 = Button(window, text='Гарниры', width=15, height = 2, bg = '#3dbde0', font = 'Calibri 15 bold italic')
    but7 = Button(window, text='Десерты', width=15, height = 2, bg = '#3dbde0', font = 'Calibri 15 bold italic')
    but8 = Button(window, text='Напитки', width=15, height = 2, bg = '#3dbde0', font = 'Calibri 15 bold italic')

    but3.bind('<Button-1>', file_title)
    but4.bind('<Button-1>', file_title)
    but5.bind('<Button-1>', file_title)
    but6.bind('<Button-1>', file_title)
    but7.bind('<Button-1>', file_title)
    but8.bind('<Button-1>', file_title)

    #but3.bind('<Button-1>', closing)
    lab1.place(x = 75, y = 40)
    but3.place(x = 30, y = 220)
    but4.place(x = 30, y = 120)
    but5.place(x = 230, y = 120)
    but6.place(x = 230, y = 220)
    but7.place(x = 430, y = 220)
    but8.place(x = 430, y = 120)

frame1 = Frame(root, width = 500, height = 230)
frame1.pack()

lab = Label(root,text='Привет, что делаем сегодня?', font = 'Calibri 20 bold italic')
but1 = Button(root,text='готовим',width=15, bg = '#3dbde0', font = 'Calibri 15 bold italic')
but2 = Button(root,text='создаем',width=15, bg = '#3dbde0', font = 'Calibri 15 bold italic')

but1.bind('<Button->',new_window)
but2.bind('<Button-1>', write_recipes.create_recipe)

lab.place(x = 80, y = 70)
but1.place(x = 40, y = 140)
but2.place(x = 300, y = 140)

root.mainloop()

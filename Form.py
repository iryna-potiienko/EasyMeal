import write_recipes

from os import listdir
from os.path import isfile
from os.path import join as joinpath
from tkinter import *

root = Tk()
salads = ''

def sorting(event):
    global list, a, sos
    root = Toplevel()
    frame = Frame(root, height = 1000, width = 20)
    frame.pack()
    frame_1 = Frame(frame, height=500, width=20)
    frame_1.pack(side = LEFT)
    frame_2 = Frame(frame, height=500, width=20)
    frame_2.pack(side = LEFT)

    file = open(filename + '.txt')
    for i, list in enumerate(file):
        if i >= 1:
            list = file.readline()
            list = list.rstrip('\n')
            while list:
                    var = StringVar()
                    check = Checkbutton(frame_1, text=list, variable=var, onvalue=list, offvalue=' ')
                    check.pack()
                    a = var.get()
                    sos = list
                    list = file.readline()
                    list = list.rstrip('\n')
                    if list == 'Способ приготовления':
                         break

                    def result(event):
                         lis = Listbox(root, height=3)
                         a = var.get()
                         l = [a]
                         #lis.delete(0, 2)
                         for a in list:
                            lis.insert(END, a)
                         lis.pack()

    file = open(filename + '.txt')
    file = file.read()
    label_recipe = Label(frame_2, text = file)
    button_ok = Button(frame_1, text='OK')
    button_ok.bind('<Button-1>', result)
    button_ok.pack()
    label_recipe.grid(row = 0, column = 0)

def file_title_s(event):
    global filename
    root = Toplevel()
    mypath = 'Салаты'
    for i in listdir(mypath):
        if isfile(joinpath(mypath,i)):
            i = i[0:-4]
            but = Button(root, text = i)
            but.bind('<Button-1>', sorting)
            but.pack()
            filename = i

def file_title_f(event):
    global filename
    root = Toplevel()
    mypath = "Первое блюдо"
    for i in listdir(mypath):
        if isfile(joinpath(mypath,i)):
            i = i[0:-4]
            but = Button(root, text = i)
            but.bind('<Button-1>', sorting)
            but.pack()
            filename = i
def file_title_o(event):
    global filename
    root = Toplevel()
    mypath = "Основное блюдо"
    for i in listdir(mypath):
        if isfile(joinpath(mypath,i)):
            i = i[0:-4]
            but = Button(root, text = i)
            but.bind('<Button-1>', sorting)
            but.pack()
            filename = i
def file_title_h(event):
    global filename
    root = Toplevel()
    mypath = "Гарниры"
    for i in listdir(mypath):
        if isfile(joinpath(mypath,i)):
            i = i[0:-4]
            but = Button(root, text = i)
            but.bind('<Button-1>', sorting)
            but.pack()
            filename = i
def file_title_n(event):
    global filename
    root = Toplevel()
    mypath = "Напитки"
    for i in listdir(mypath):
        if isfile(joinpath(mypath,i)):
            i = i[0:-4]
            but = Button(root, text = i)
            but.bind('<Button-1>', sorting)
            but.pack()
            filename = i
def file_title_d(event):
    global filename
    root = Toplevel()
    mypath = "Десерты"
    for i in listdir(mypath):
        if isfile(joinpath(mypath, i)):
            i = i[0:-4]
            but = Button(root, text=i)
            but.bind('<Button-1>', sorting)
            but.pack()
            filename = i


def new_window(event):
    def closing(event):
        window.destroy()
    window = Toplevel(root)
    lab1 = Label(window, text='Что вы хотите приготовить сегодня?')
    but3 = Button(window, text='Салаты', width=35)
    but4 = Button(window, text='Первое блюдо', width=35)
    but5 = Button(window, text='Основное блюдо', width=35)
    but6 = Button(window, text='Гарниры', width=35)
    but7 = Button(window, text='Десерты', width=35)
    but8 = Button(window, text='Напитки', width=35)

    but3.bind('<Button-1>', file_title_s)
    but4.bind('<Button-1>', file_title_f)
    but5.bind('<Button-1>', file_title_o)
    but6.bind('<Button-1>', file_title_h)
    but7.bind('<Button-1>', file_title_d)
    but8.bind('<Button-1>', file_title_n)

    #but3.bind('<Button-1>', closing)
    lab1.pack()
    but3.pack()
    but4.pack()
    but5.pack()
    but6.pack()
    but7.pack()
    but8.pack()


lab = Label(root,text='Привет, что делаем сегодня?')
but1 = Button(root,text='готовим',width=35)
but2 = Button(root,text='создаем',width=35)

but1.bind('<Button->',new_window)
but2.bind('<Button-1>', write_recipes.create_recipe)

lab.grid(column = 1, row = 0)
but1.grid(column = 1, row = 1)
but2.grid(column = 2, row = 1)

root.mainloop()

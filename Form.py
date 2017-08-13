import write_recipes
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from tkinter import *

root = Tk()

def sorting(event):
    global list, a, sos, b
    c = event.widget['text']
    root = Toplevel()
    frame = Frame(root, height = 1000, width = 20)
    frame.pack()
    frame_1 = Frame(frame, height=500, width=20)
    frame_1.pack(side = LEFT)
    frame_2 = Frame(frame, height=500, width=20)
    frame_2.pack(side = LEFT)

    file = open(filename + c + '.txt')
    for i, list in enumerate(file):
        if i >= 2:
            #list = file.readline()
            list = list.rstrip('\n')
            while list :
                    if list == 'Способ приготовления:':
                        break
                    elif list == 'Приятного аппетита!':
                        break
                    if len(list) > 50:
                        break
                    check = Button(frame_1, text=list)
                    check.pack()
                    list = file.readline()
                    list = list.rstrip('\n')

                    def change(event):
                        global a
                        event.widget['bg'] = 'red'
                        print(event.widget['text'])
                        text.insert(END, event.widget['text'])
                        text.insert(END, '\n')

                    def returning(event):
                        event.widget['bg'] = 'blue'
                        text.replace(event.widget['text'], "")
                        #text.delete()

                    check.bind('<Button-1>', change)
                    check.bind('<Double-Button-1>', returning)
    file = open(filename + c + '.txt')
    file = file.read()
    label_recipe = Label(frame_2, text = file)
    #button_ok = Button(frame_1, text='OK')
    #button_ok.bind('<Button-1>', buying)
    #button_ok.pack()
    text = Text(frame_1)
    text.pack()
    label_recipe.grid(row = 0, column = 0)

def file_title(event):
    global filename
    root = Toplevel()
    mypath = 'Рецепты/' + event.widget['text']
    for i in listdir(mypath):
        if isfile(joinpath(mypath,i)):
            i = i[0:-4]
            filename = mypath + '/'
            but = Button(root, text = i)
            but.bind('<Button-1>', sorting)
            but.pack()

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

    but3.bind('<Button-1>', file_title)
    but4.bind('<Button-1>', file_title)
    but5.bind('<Button-1>', file_title)
    but6.bind('<Button-1>', file_title)
    but7.bind('<Button-1>', file_title)
    but8.bind('<Button-1>', file_title)

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

import write_recipes
import product_try
from tkinter import *
root = Tk()

def new_window(event):
    def opening(event):
        product_try.list()

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

    but3.bind('<Button-1>', opening)
    but3.bind('<Double-Button-1>', closing)
    lab1.pack()
    but3.pack()
    but4.pack()
    but5.pack()
    but6.pack()
    but7.pack()
    but8.pack()

def create(event):
    write_recipes.create_recipe()



lab = Label(root,text='Привет, что делаем сегодня?')
but1 = Button(root,text='готовим',width=35)
but2 = Button(root,text='создаем',width=35)
but1.bind('<Button->',new_window)

but2.bind('<Button-1>', create)

lab.grid(column = 1, row = 0)
but1.grid(column = 1, row = 1)
but2.grid(column = 2, row = 1)

root.mainloop()

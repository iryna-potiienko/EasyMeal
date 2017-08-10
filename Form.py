from tkinter import *
root = Tk()

lab = Label(root,text='Привет, что делаем сегодня?')
but1 = Button(root,text='готовим',width=35)
but2 = Button(root,text='создаем',width=35)

lab1 = Label(root,text='Что вы хотите приготовить сегодня?')
but3 = Button(root,text='Салаты',width=35)
but4 = Button(root,text='Первое блюдо(супы)',width=35)
but5 = Button(root,text='Основное блюдо(мясо, рыба и т.д.)',width=35)
but6 = Button(root,text='Гарниры',width=35)
but7 = Button(root,text='Десерты',width=35)
but8 = Button(root,text='Напитки',width=35)


lab.pack()
but1.pack()
but2.pack()
lab1.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()
but8.pack()

root.mainloop()

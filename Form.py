import write_recipes
from os import listdir
from os.path import isfile
from os.path import join as joinpath
#from PIL import Image, ImageTk
from tkinter import *

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
    global list, a, sos, b
    c = event.widget['text']
    root = Toplevel()
    root.geometry('1200x800')
    frame = Frame(root, height = 1000, width = 20)
    frame.pack()
    frame_1 = Frame(frame, height=500, width=20)
    frame_1.pack(side = LEFT)
    frame_2 = Frame(frame, height=500, width=20)
    frame_2.pack(side = LEFT)

    file = open(filename + c + '.txt')
    for i, list in enumerate(file):
        if i >= 2:              # чтение файла начиная со второй строчки
            #list = file.readline()
            list = list.rstrip('\n')
            while list :   # цикл для определения какие продукты есть для приготовления, а каких нету
                    if list == 'Способ приготовления:':
                        break
                    elif list == 'Приятного аппетита!' or list == 'Приятного апетита!' or list == 'Приятного аппетита':
                        break
                    if len(list) > 50:
                        break
                    check = Button(frame_1, text=list, width = 40, bg = '#3dbde0', font = 'Calibri 14 italic')
                    check.pack()
                    list = file.readline()
                    list = list.rstrip('\n')

                    def change(event):   # при нажатии на кнопку она станет красной и продукт появится в текстовом поле внизу
                        global a
                        event.widget['bg'] = 'red'
                        print(event.widget['text'])
                        text.insert(END, event.widget['text'])
                        text.insert(END, '\n')

                    def returning(event):   # при двойном нажатии на кнопку она отменит функцию change()
                        event.widget['bg'] = '#3dbde0'
                        text.replace(event.widget['text'], "")
                        #text.delete()

                    check.bind('<Button-1>', change)
                    check.bind('<Double-Button-1>', returning)
    file = open(filename + c + '.txt')
    file = file.read()
    text_recipe = Text(frame_2, wrap = WORD)
    text_recipe.insert(1.0, file)
    button_ok = Button(root, text='Выйти', bg = '#3dbde0', font = 'Calibri 14 bold')
    button_ok.bind('<Button-1>', exit)
    button_ok.place(x = 1100, y = 750)
    text = Text(frame_1, width = 55, height = 13)
    text.pack()
    text_recipe.grid(row = 0, column = 0)

def file_title(event):
    '''Функция которая показывает список текстовых файлов в папке - список рецептов выбранной категории'''
    global filename
    root = Toplevel()
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
    def closing(event):
        window.destroy()
    window = Toplevel(root)
    window.geometry('620x450')
    window['bg'] = '#3dbde0'
    frame = Frame(window, width = 620, height = 350)
    frame.pack()
    lab1 = Label(window, text='Что вы хотите приготовить сегодня?', font = 'Calibri 20 bold italic')
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
    lab1.place(x = 80, y = 50)
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

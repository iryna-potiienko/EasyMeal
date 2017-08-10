from tkinter import *

def save(event):
    title = entry_1.get()
    file = open(title + '.txt', 'x')

    text_ingredients = text_1.get(1.0, END)
    text_cooking = text_2.get(1.0,END)
    file.write(title)
    file.write('\n')
    file.write(text_ingredients)
    file.write('\nСпособ приготовления\n')
    file.write(text_cooking)
    file.close()

def close(event):
    root.destroy()


root = Tk()
root.title('Create recipe')

label_1 = Label(root, text = 'Название рецепта:')
entry_1 = Entry(root, width = 50)
label_1.pack()
entry_1.pack()

label_2 = Label(root, text = 'Сюда введи сам рецепт')

frame_1 = Frame(root, width = 500, height = 20)
frame_1.pack()

frame = Frame(root, width = 10000, height =500)
frame.pack()

label_3 = Label(frame_1, text = 'Ингредиенты:')
text_1 = Text(frame, width = 40, height = 20, wrap = WORD)
ingredients = text_1.get(1.0, END)
text_1.tag_add(ingredients, '1.0', END)
text_1.insert(1.0, ingredients)
label_3.pack(side = LEFT)
text_1.pack(side = LEFT)

label_4 = Label(frame, text = 'Категория:')
var = IntVar()
var.set(0)
category_1 = Radiobutton(frame, text = 'Салаты', variable = var, value = 0)
category_2 = Radiobutton(frame, text = 'Первые блюда', variable = var, value = 1)
category_3 = Radiobutton(frame, text = 'Основные блюда', variable = var, value = 2)
category_4 = Radiobutton(frame, text = 'Гарниры', variable = var, value = 3)
category_5 = Radiobutton(frame, text = 'Десерты', variable = var, value = 4)
category_6 = Radiobutton(frame, text = 'Напитки', variable = var, value = 5)

label_4.pack()
category_1.pack()
category_2.pack()
category_3.pack()
category_4.pack()
category_5.pack()
category_6.pack()

label_5 = Label(root, text = 'Способ приготовления:')
text_2 = Text(root, width = 80, height = 20, wrap = WORD)
label_5.pack()
text_2.pack()

button = Button(root, text = 'Сохранить рецепт')
button.pack(side = RIGHT)

button.bind("<Button-1>", save)
#button.bind("<Button-1>", close)   #два действия вместе не хотят работать

root.mainloop()
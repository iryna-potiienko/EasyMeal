from tkinter import *

def save(event):
    title = entry_1.get()
    file = open(title + '.txt', 'x')

    text = text_1.get(1.0, END)
    file.write(text)
    file.close()

def close(event):
    root.destroy()

root=Tk()
root.title('Create recipe')

label_1 = Label(root, text = 'Как ты назовешь свой рецепт?')
entry_1 = Entry(root, width = 50)
label_1.pack()
entry_1.pack()

label_2 = Label(root, text = 'Сюда введи сам рецепт:')
text_1 = Text(root, width = 80, height = 30, wrap = WORD)
label_2.pack()
text_1.pack()

button = Button(root, text = 'Сохранить рецепт')
button.pack(side = RIGHT)

button.bind("<Button-1>", save)
button.bind("<Button-1>", close)

root.mainloop()
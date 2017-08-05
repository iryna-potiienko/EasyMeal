import file4
import file3
import random
ps=["Привет!","Ку-ку!","Hi!","Здраствуйте!","Здаров!","Драсте!","Салют!"]
i=random.randint(0,len(ps)-1)
print (ps[i])
print ('''Что ты хочешь приготовить сегодня? Давай выберём вместе. Я предлагаю тебе выбрать или десерт, или напиток)''')
choice=input("")
choice=str(choice.lower().strip())
if choice=="десерт":
	print(" ")
	file4.meal()
if choice=="напиток":
	print (" ")
	file3.drinks()
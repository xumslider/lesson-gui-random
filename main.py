import random
from tkinter import *
from pyexpat.errors import messages


class application():
    def __init__(self):
        # создание атрибута окна
        self.root = Tk()
        # создание атрибута  титульной надписи
        self.root.title('random')
        # атрибут минимального размера окна
        self.root.minsize(500, 400)
        # создание атрибута кнопки рассчета
        self.create_random_box()

        self.create_result_label()

        # метод mainloop циклит приложение
        self.root.mainloop()

     # создание функции кнопки "Рассчитать"
    def create_random_box(self):
        # пустая строка для разделения блоков
        self.random_box = Label()
        # создание кнопки с текстом
        self.random_btn = Button(text="Рандом")
        # метод bind создает связь между нажатием кнопки и функцией
        self.random_btn.bind('<Button>', self.get_random)
        # pack - менеджер размещения на экран
        self.random_box.pack()
        self.random_btn.pack()

    def create_result_label(self):
        empty_label = Label()
        empty_label.pack()
        self.random_label = Label()
        self.random_label.pack()

    def get_random(self, event):
        club_mem = ['Артем', 'Марина', 'Иван', 'Алексей']
        message = random.choice(club_mem)
        self.random_label.config(text=message)


application()

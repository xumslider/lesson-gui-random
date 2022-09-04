import random
from tkinter import *


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
        # метод mainloop циклит приложение
        self.root.mainloop()

    def create_random_box(self):  # создание функции кнопки "Рассчитать"
        # пустая строка для разделения блоков
        self.random_box = Label()
        # создание кнопки с текстом
        self.random_btn = Button(text="Рандом")
        # метод bind создает связь между нажатием кнопки и функцией
        self.random_btn.bind('<Button>', self.get_random)
        # pack - менеджер размещения на экран
        self.random_box.pack()
        self.random_btn.pack()

    def get_random(self, event):
        club_mem = ['Артем', 'Марина', 'Иван', 'Алексей']
        messages = random.choice(club_mem)
        empty_label = Label()
        empty_label.pack()
        random_label = Label(text=messages)
        random_label.pack()


application()

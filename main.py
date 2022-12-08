from tkinter import *
from tkinter import ttk
from logiccalc import LogicCalc

# Интерфейс через tkinter


class Interface(Tk):
    '''   Простенький интерфейс. Создается главное окно.
    Сверху накладывается фрейм с сеткой.
    Относительно сетки размещались кнопки   '''
    def __init__(self):
        super().__init__()
        self.window()

    def window(self):
        # Создание главного окна и настройка его параметров
        self.title("Calc for Kaif")
        icon = PhotoImage(file="icon.png")
        self.iconphoto(False, icon)
        self.resizable(False, False)
        self.main_greed()
        self.entry_box()
        self.buttons()
        self.mainloop()

    def main_greed(self):
        # Создание главного фрейма и сетки на нем
        self.mainframe = ttk.Frame(self, padding="5 5 5 5")
        self.mainframe.grid(column=0, row=0, sticky='nwes')
        self.columnconfigure(0, weight=3)
        self.rowconfigure(0, weight=4)

    def entry_box(self):
        # Поле заполнения
        global feet
        feet = StringVar()
        global feet_entry
        feet_entry = ttk.Entry(self.mainframe, textvariable=feet)
        feet_entry.grid(row=0, column=0, padx=5, pady=5, ipadx=20, ipady=20, columnspan=4, sticky=N+W+S+E)
        feet_entry.insert(0, '0')

    # Метод отчистки поля ввода для кнопки 'Clear'

    def clear(self):
        feet_entry.delete(0, END)
        feet_entry.insert(0, '0')

    # Метод счета выражения для кнопки '='

    def calculate(self):
        num, op, open_oper, close_oper = 0, 0, 0, 0
        i = LogicCalc()
        mass = i.unpack(feet.get())
        for el in mass:
            if type(el) == float:
                num += 1
            elif el in '+/*':
                op += 1
            elif el == '(':
                open_oper += 1
            elif el == ')':
                close_oper += 1
        if num != (op + 1) or open_oper != close_oper:
            feet_entry.delete(0, END)
            feet_entry.insert(0, 'Введите корректное выражение')
        elif '=' in feet.get():
            self.clear()
        elif feet.get() != '0':
            if type(i.turn(mass)) == str:
                feet_entry.delete(0, END)
                feet_entry.insert(0, i.turn(mass))
            else:
                feet_entry.insert(END, '=' + str(round(i.turn(mass))))

    # Метод заполнения окна для остальны функциональных кнопок

    def fill(self, w):
        if feet.get() == '0' or feet.get() == 'Введите корректное выражение':
            feet_entry.delete(0, END)

        feet_entry.insert(END, w)

    # Кнопки чисел и знаков математических операций

    def buttons(self):
        l_but = 10
        w_but = 6

        mass_num_button = (
            ('1', '2', '3'),
            ('4', '5', '6', '+'),
            ('7', '8', '9', '-'),
            ('(', ')', '/', '*'),
        )
        for i in range(len(mass_num_button)):
            for j in range(len(mass_num_button[i])):
                num = ttk.Button(self.mainframe, text=mass_num_button[i][j], width=w_but,
                                 command=lambda x=mass_num_button[i][j]: self.fill(x))
                num.grid(row=i + 1, column=j, padx=5, pady=5, ipady=l_but, ipadx=w_but, sticky=N + S + W + E)

        num = ttk.Button(self.mainframe, text='=', width=w_but, command=self.calculate)
        num.grid(row=1, column=3, padx=5, pady=5, ipady=l_but, ipadx=w_but, sticky=N + S + W + E)

        num = ttk.Button(self.mainframe, text='Clear', width=w_but, command=self.clear)
        num.grid(row=5, column=0, padx=5, pady=5, ipady=l_but - 5, ipadx=w_but, sticky=N + S + W + E, columnspan=2)

        num = ttk.Button(self.mainframe, text='Credits', command=lambda x='Credits': print(x), width=w_but)
        num.grid(row=5, column=2, padx=5, pady=5, ipady=l_but - 5, ipadx=w_but, sticky=N + S + W + E, columnspan=2)


i = Interface()

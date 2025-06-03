import tkinter as tk
from random import randint

start, end = 1, 100
count = 5


class Window:

    def __init__(self, parent):
        self.number = self.random_number()
        self.counter = count

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        container = tk.Frame(parent)
        container.grid(column=0, row=0, sticky='new')
        container.grid_columnconfigure(0, weight=3)

        header = tk.Label(parent, text='Number Guessing Game')
        header['font'] = ('times 16 bold')
        header['relief'] = 'groove'
        header.grid(column=0, row=0, sticky='new', pady=4, ipady=4)

        instructions = tk.Label(parent)
        instructions['text'] = f'Choose a number between {start} and {end}'
        instructions['bg'] = 'lightyellow'
        instructions['relief'] = 'groove'
        instructions.grid(column=0, row=1, sticky='new', pady=4)

        self.msgbox = tk.Label(parent, anchor='w')
        self.msgbox['relief'] = 'groove'
        self.msgbox['text'] = f'Tries Left: {self.counter}'
        self.msgbox.grid(column=0, row=2, sticky='new', pady=8)

        self.entry = tk.Entry(parent)
        self.entry.grid(column=0, row=3, sticky='new', pady=8)

        btn_frame = tk.Frame(parent)
        btn_frame.grid(column=0, row=4, sticky='new')
        for i in range(2):
            btn_frame.grid_columnconfigure(i, weight=3, uniform='btns')

        self.btn = tk.Button(btn_frame)
        self.btn['text'] = 'Submit'
        self.btn['command'] = lambda: self.check(self.entry.get())
        self.btn.grid(column=0, row=0, sticky='new')

        self.reset_btn = tk.Button(btn_frame)
        self.reset_btn['text'] = 'Reset'
        self.reset_btn['state'] = 'disabled'
        self.reset_btn.grid(column=1, row=0, sticky='new')

        msg_container = tk.Frame(parent)
        msg_container['relief'] = 'groove'
        msg_container['highlightbackground'] = 'lightgray'
        msg_container['highlightcolor'] = 'lightgray'
        msg_container['highlightthickness'] = 1
        msg_container.grid(column=0, row=5, sticky='new', pady=4)
        msg_container.grid_columnconfigure(0, weight=0)
        msg_container.grid_columnconfigure(1, weight=3)

        self.label = tk.Label(msg_container, text='MSG:', anchor='w')
        self.label.grid(column=0, row=0, sticky='new')

        self.msg_label = tk.Label(msg_container, anchor='w')
        self.msg_label.grid(column=1, row=0, sticky='new')
        self.entry.focus()
        self.entry.bind('<Return>', lambda num: self.check(self.entry.get()))

    def random_number(self):

        number = randint(start, end)
        return number

    def check(self, guess):

        try:
            guess = int(guess)
            self.counter = self.counter - 1
            self.msgbox['text'] = f'Tries Left: {self.counter}'

            self.entry.delete(0, tk.END)
            if guess > end or guess < start:
                if self.counter > count:
                    self.counter = count
                else:
                    self.counter = self.counter + 1

                self.msg_label['text'] = f'Please choose a number between {start} and {end}'
                self.msg_label['fg'] = 'red'
                self.msgbox['text'] = f'Tries Left: {self.counter}'

            elif guess > self.number:
                self.msg_label['text'] = f'{guess} is too high.'
                self.msg_label['fg'] = 'red'
            elif guess < self.number:
                self.msg_label['text'] = f'{guess} is too low.'
                self.msg_label['fg'] = 'darkorange'
            else:
                self.msg_label['text'] = f'You win! {guess} is correct.'
                self.msg_label['fg'] = 'green'
                self.btn['state'] = 'disabled'
                self.reset_btn['state'] = 'normal'
                self.reset_btn['command'] = self.reset

            if self.counter == 0:
                self.msg_label['text'] = 'You have no tries left.'
                self.msg_label['fg'] = 'tomato'
                self.btn['state'] = 'disabled'
                self.reset_btn['state'] = 'normal'
                self.reset_btn['command'] = lambda: self.reset()

        except ValueError:
            self.msg_label['text'] = 'Error! Please enter only whole numbers.'
            self.msg_label['fg'] = 'red'
            self.entry.delete(0, tk.END)

    def reset(self):

        self.counter = count
        self.btn['state'] = 'normal'
        self.reset_btn['state'] = 'disabled'
        self.msg_label['text'] = ''
        self.msg_label['fg'] = 'black'
        self.msgbox['text'] = f'Tries Left: {count}'
        self.number = self.random_number()


def main():
    root = tk.Tk()
    root['padx'] = 8
    root['pady'] = 5
    root.geometry('400x210+250+250')
    root.resizable(False, False)
    Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
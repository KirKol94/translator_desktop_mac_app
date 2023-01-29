from googletrans import Translator
import os
import tkinter as tk


def get_translation(string):
    t = Translator()
    out_lang = t.detect(string)
    is_english = 'lang=en' in str(out_lang)
    trans = t.translate(string, dest=f"{'ru' if is_english else 'en'}")
    return trans.text


def to_voice(string='hello'):
    os.system(f"say {get_translation(string)}")


def create_win():
    win = tk.Tk()
    win.title('translator')
    win.geometry('500x75+1000+500')
    win.resizable(False, False)

    def handle_translate(self):
        to_voice(field.get())
        field.focus()
        field.delete(0, 'end')

    # элементы
    label = tk.Label(win, text='Русский <---> English')
    field = tk.Entry(win, width=50)

    win.bind("<Return>", handle_translate)

    # отображение
    label.pack()
    field.pack(pady=10)
    field.focus()

    win.mainloop()


if __name__ == '__main__':
    create_win()

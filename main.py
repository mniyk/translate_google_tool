import pyperclip
import tkinter as tk
from googletrans import Translator


class Application(tk.Frame):
    def __init__(self, master: tk.Tk = None):
        super().__init__(master)

        # master
        self.master = master
        self.master_settings()

        # radio
        self.radio_value = tk.IntVar()
        self.create_translate_type_radiobutton()

        # text
        self.before_text = None
        self.after_text = None
        self.create_translate_text()

        # button
        self.create_translate_button()

    def master_settings(self):
        self.master.title('Translate Google Tool')

    def create_translate_type_radiobutton(self):
        self.radio_value.set(0)

        padding = 5

        tk.Radiobutton(
            self.master, value=0, variable=self.radio_value, text='日本語 → 英語', width=15
        ).grid(row=0, column=0, padx=padding, pady=padding)

        tk.Radiobutton(
            self.master, value=1, variable=self.radio_value, text='英語 → 日本語', width=15
        ).grid(row=0, column=1, padx=padding, pady=padding)

    def create_translate_text(self):
        width = 30
        height = 10
        padding = 5

        tk.Label(text='翻訳前').grid(row=1, padx=padding, pady=padding, sticky=tk.W)
        tk.Button(
            text='クリア', command=self.clear_text
        ).grid(row=1, column=1, padx=padding, pady=padding, sticky=tk.E)
        self.before_text = tk.Text(self.master, width=width, height=height)
        self.before_text.grid(row=2, columnspan=2, padx=padding, pady=padding, sticky=tk.W+tk.E)

        tk.Label(text='翻訳後').grid(row=4, padx=padding, pady=padding, sticky=tk.W)
        self.after_text = tk.Text(self.master, width=width, height=height)
        self.after_text.configure(state='disabled')
        self.after_text.grid(row=5, columnspan=2, padx=padding, pady=padding, sticky=tk.W+tk.E)

    def create_translate_button(self):
        padding = 5

        tk.Button(
            self.master, text='翻訳', command=self.execute_translate
        ).grid(row=3, columnspan=2, padx=padding, pady=padding, sticky=tk.W+tk.E)

    def execute_translate(self):
        trans = Translator()

        translate_type = self.radio_value.get()

        text = self.before_text.get('1.0', 'end')

        if translate_type == 0:
            result = trans.translate(text, src='ja', dest='en')
        else:
            result = trans.translate(text, src='en', dest='ja')

        pyperclip.copy(result.text)

        self.after_text.configure(state='normal')
        self.after_text.delete('1.0', 'end')
        self.after_text.insert('1.0', result.text)
        self.after_text.configure(state='disabled')

    def clear_text(self):
        self.before_text.delete('1.0', 'end')

        self.after_text.configure(state='normal')
        self.after_text.delete('1.0', 'end')
        self.after_text.configure(state='disabled')


def main():
    master = tk.Tk()

    app = Application(master=master)

    app.mainloop()


if __name__ == '__main__':
    main()

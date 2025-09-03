# DateEntry.py   page 125

import tkinter as tk
from  tkinter import  ttk
from datetime import datetime




class DataEntry(ttk.Entry):
    """An Entry for ISO-style dates ( Year-month-day )"""  # Page126
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(
            validate='all',
            validatecommand=(
                self.register(self._validate),
                '%S', '%i', '%V', '%d'
            ),
            invalidcommand=(self.register(self._on_invalid), '%V')
            )
        self.error = tk.StringVar()


    def _toggle_error(self, error='' ):
        self.error.set(error)
        self.config(foreground='red' if error else 'black')

    def _validate(self, char, index, event, action):
        # reset errr state
        self._toggle_error()
        valid=True    # Page 126
        #ISO dates only need digits and  hyphens
        if event == 'key':
            if action == '0':
                valid = True
            elif index in ('0', '1', '2', '3', '5', '6', '8', '9'):
                valid = char.isdigit()
            elif index in ('4', '7'):
                valid = char == '-'
            else:
                valid = False
        elif event =='focusout':
            try:
                datetime.strptime(self.get(), '%Y-%m-%d')
            except ValueError:
                valid = False
        return valid


    def _on_invalid(self, event):
        if event != 'key':
            self._toggle_error('Not a valid date')  # Page 128




if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('640x480+200+100')  # set the root window size

    entry = DataEntry(root)
    entry.pack()
    ttk.Label(
        textvariable=entry.error, foreground='red'
    ).pack()

    # Add this s we can unfocus the DateEntry  Page 128
    ttk.Entry(root).pack()
    root.mainloop()






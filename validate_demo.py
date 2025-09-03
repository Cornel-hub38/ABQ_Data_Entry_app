# validate demo.py

import tkinter as tk
from tkinter.ttk import Label

root = tk.Tk()

label = Label(root, text='Trial run')
root.title('Interesting')   #set the title
root.geometry('640x480+200+100')#set the root window size


entry = tk.Entry(root)
entry.grid()

def always_good():    #  Page 120  Moore A - Python GUI programming with tkinter
    return True


validate_ref = root.register(always_good)

entry.configure(
    validate='all',
    validatecommand=(validate_ref,)
    )

entry2 = tk.Entry(root)
entry2.grid(pady=10)

def no_t_for_me(proposed):
    return 't' not in proposed

validate2_ref = root.register(no_t_for_me)
entry2.configure(
    validate='all',
    validatecommand=(validate2_ref, '%P')
)


entry3 = tk.Entry(root)
entry3.grid()
entry3_error = tk.Label(root,  fg='red')
entry3_error.grid()

def only_five_chars(proposed):
    return len(proposed) < 6

def only_five_chars_error(proposed):
    entry3_error.configure(
        text=f'{proposed} is too long, only five chars allowed.'
    )

validate3_ref = root.register(only_five_chars)
invalidate_ref = root.register(only_five_chars_error)

entry3.configure(
    validate='all',
    validatecommand=(validate3_ref, '%P'),
    invalidcommand=(invalidate_ref, '%P')
)


#  start at page 124 of   Moore A - Python GUI programming with tkinter



root.mainloop()


import tkinter as tk   #  Friday September 12 2025 @0926     page 92
import json


class JSONVar(tk.StringVar):
    """A Tk variable that can hold dicts and lists"""
    def __init__(self, *args, **kwargs):
        kwargs['value'] = json.dumps(kwargs.get('value'))
        super().__init__(*args, **kwargs)


    def set(self, value, *args, **kwargs):
        string = json.dumps(value)
        super().set(string, *args, **kwargs)

    def get(self, *args, **kwargs):      #Page 93
        string = super().get(*args, **kwargs)
        return json.loads(string)


root = tk.Tk()
var1 = JSONVar(root)
var1.set([1, 2,3])
var2  = JSONVar(root, value={'a': 10, 'b': 15})

print("Var1: ", var1.get()[1])    # should print 2

print("Var2: ", var2.get()['b'])   # should print 15



#  Creating compound widgets     page 94

class LabelInput(tk.Frame):
    """A label and input combined together"""
    def __int__(
            self, parent, label, inp_cls,
             inp_args, *args, **kwargs
    ):
        super().__int__(parent, *args, **kwargs)

        self.label = tk.Label(self, text=label, anchor='w')
        self.input = inp_cls(self, **inp_args)








# data _entry_app.py   Page 136

import tkinter as tk  # Saturday 6th September 2025 @1014 on starting on page 100
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv

from pywin.framework.dlgappcore import AppDialog


variables = dict()    # Sunday 7th September 2025 @1540     Page 65
records_saved = 0

root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)

ttk.Label(    #  Page 66
    root, text="ABQ Data Entry Application",
    font=("TkDefaultFont", 16)
    ).grid()


drf = ttk.Frame(root)      #  Page 66
drf.grid(padx=10, sticky=(tk.E + tk.W))
drf.columnconfigure(0, weight=1)

r_info = ttk.LabelFrame(drf, text='Record Information')   #   Page 67
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)


variables['Date'] = tk.StringVar()
ttk.Label(r_info, text='Date').grid(row=0, column=0)
ttk.Entry(
    r_info, textvariable=variables['Date']
).grid(row=1, column=0, sticky=(tk.W + tk.E))



time_values = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = tk.StringVar()
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(
    r_info, textvariable=variables['Time'], values=time_values
).grid(row=1, column=1, sticky=(tk.W + tk.E))              #Page 68

variables['Technician'] = tk.StringVar()        # Sunday 7th September 2025 @1606     Page 68
ttk.Label(r_info, text='Technician').grid(row=0, column=2)      #  Monday September 8th 2025 @1115   Page 68
ttk.Entry(
    r_info, textvariable=variables['Technician']
).grid(row=1, column=2, sticky=(tk.W + tk.E))

variables['Lab'] = tk.StringVar()
ttk.Label(r_info, text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
        labframe, value=lab, text=lab, variable=variables['Lab']
    ).pack(side=tk.LEFT, expand=True)
    labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))

variables['Plot'] = tk.IntVar()
ttk.Label(r_info, text='Plot').grid(row=2, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['Plot'],
    values=list(range(1, 21))
).grid(row=3, column=1, sticky=(tk.W + tk.E))

variables['Seed Sample'] = tk.StringVar()
ttk.Label(r_info, text='Seed Sample').grid(row=2, column=2)         #   Page 69
ttk.Entry(
    r_info,
    textvariable=variables['Seed Sample']
).grid(row=3, column=2, sticky=(tk.W + tk.E))


# The Envirnment Data ectin    Page 69
e_info = ttk.LabelFrame(drf, text='Environment Data')
e_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    e_info.columnconfigure(i, weight=1)

variables['Humidity'] = tk.DoubleVar()
ttk.Label(e_info, text="Humidity (g/m3)").grid(row=0, column=0)
ttk.Spinbox(
    e_info, textvariable=variables['Humidity'],
    from_=0.5, to=52.0, increment=0.01,
).grid(row=1, column=0, sticky=(tk.W + tk.E))


variables['Light'] = tk.DoubleVar()
ttk.Label(e_info, text='Light (klx)').grid(row=0, column=1)
ttk.Spinbox(
    e_info, textvariable=variables['Light'],
    from_=0, to=100, increment=0.01
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables["Temperature"] = tk.DoubleVar()
ttk.Label(e_info, text="Temperature (oC)").grid(row=0, column=2)
ttk.Spinbox(
    e_info, textvariable=variables["Temperature"],
    from_=4, to=40, increment=.01
).grid(row=1, column=2, sticky=(tk.W + tk.E))     #  end of Page 69


variables['Equipment Fault'] = tk.BooleanVar(value=False)         #   Page 70
ttk.Checkbutton(
    e_info, variable=variables['Equipment Fault'],
    text='Equipment Fault'
).grid(row=2, column=0, sticky=tk.W, pady=5)

p_info = ttk.LabelFrame(drf, text="Plant Data")
p_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    p_info.columnconfigure(i, weight=1)

variables['Plants'] = tk.IntVar()
ttk.Label(p_info, text="Plants").grid(row=0, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Plants'],
    from_=0, to=20, increment=1
).grid(row=1, column=0, sticky=(tk.W + tk.E))

variables['Blossoms'] = tk.IntVar()
ttk.Label(p_info, text="Blossoms").grid(row=0, column=1)
ttk.Spinbox(
    p_info, textvariable=variables["Blossoms"],
    from_=0, to=1000, increment=1
).grid(row=1, column=1, sticky=(tk.W +tk.E))
variables['Fruit'] = tk.IntVar()          #  Page 71
ttk.Label(p_info, text="Fruit").grid(row=0, column=2)
ttk.Spinbox(
    p_info, textvariable=variables['Fruit'],
    from_=0, to=1000, increment=1
).grid(row=1, column=2, sticky=(tk.W + tk.E))

variables["Min Height"] = tk.DoubleVar()
ttk.Label(p_info, text="Min Height  (cm)").grid(row=2, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Min Height'],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=0, sticky=(tk.W + tk.W))

variables['Max Height'] = tk.DoubleVar()
ttk.Label(p_info, text="Max Height (cm)").grid(row=2, column=1)
ttk.Spinbox(
    p_info, textvariable=variables["Max Height"],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=1, sticky=(tk.W + tk.E))


variables['Med Height'] = tk.DoubleVar()            #              end of Page 71
ttk.Label(p_info, text="Median Height  (cm)").grid(row=2, column=2)
ttk.Spinbox(
    p_info, textvariable=variables["Med Height"],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=2, sticky=(tk.W + tk.E))         #    Monday 8th September 2025 @1349   Page 71

ttk.Label(drf, text="Note").grid()   #  Tuesday 9th September 2025 @1757   Page 72
notes_inp = tk.Text(drf, width=75, height=10)
notes_inp.grid(sticky=(tk.W + tk.E))


#  Add some buttons
buttons = tk.Frame(drf)
buttons.grid(sticky=tk.E + tk.W)
save_button = ttk.Button(buttons, text="Save")
save_button.pack(side=tk.RIGHT)

reset_button = ttk.Button(buttons, text="Reset")
reset_button.pack(side=tk.RIGHT)

status_variable = tk.StringVar()
ttk.Label(
    root, textvariable=status_variable
).grid(sticky=tk.W + tk.E, row=99, padx=10)











class BoundText(tk.Text):
    """ A text widget with a bound variable"""
    def __init__(self, *args, textvariable=None, **kwargs):  #  Passing in a variable on Page 101
        super().__init__(*args, **kwargs)
        self._variable = textvariable

        if self._variable:
            self.inert('1.0', self._variable.get())
        if self._variable:  # synchronising the widget to the variable  n Page 101
            self.insert('1.0', self._variable.get())
            self._variable.trace_add('write', self._set_content)
        if self._variable:    # synchronising the variable to the widget: Page 102
            self.insert('1.0', self._variable.get())
            self._variable.trace_add('write', self._set_content)
            self.bind('<<Modified>>', self._set_var)

    def  _set_var(self, *_):    # Page 102
        """Set the variable to the text content"""
        if self.edit_modified():    # Page 103
            content = self.get('1.0', 'end-1chars')
            self._variable.set(content)
            self.edit_modified(False)



    def _set_content(self, *_):   # Page 102
        """set the text contents to the variable.    create teh callback"""
        self.delete('1.0', tk.END)
        self.insert('1.0', self._variable.get())

class LabelInput(tk.Frame):   #  creating a more advanced  LabelInput()    Page 103
    """A widget containing a label and input together"""
    def __init__(
            self, parent, label, var, input_class=ttk.Entry,
            input_args=None, label_args=None, **kwargs
    ):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = var
        self.variable.label_widget = self

        if input_class in (ttk.Checkbutton, ttk.Button): #page 104
            input_args['text'] = label
        else:
            self.label =ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))


        if input_class in (
            ttk.Checkbutton, ttk.Button, ttk.Radiobutton
        ):        # Page 104
            input_args['variable'] = self.variable
        else:
            input_args['textvariable'] = self.variable

        if input_class == ttk.Radiobutton:     # start/end at Saturday 6th September 2025 @1110 Page 105
            self.input = tk.Frame(self)   #  Moore A. Python GUI programming with tkinter - 2021
            for v in input_args.pop('values', []):
                button = ttk.Radiobutton(
                    self.input, value=v, text=v, **input_args
                )
                button.pack(
                    side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill='x'
                )
        else:
            self.input = input_class(self, **input_args)

            self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
            self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.E + tk.W), **kwargs):   # Saturday 6th Septembber 2025 @1719    Page 106
        """Override grid to add default sticky values"""
        super().grid(sticky, **kwargs)


class DataRecordForm(ttk.Frame):         # Creating a form class   Page 106
    """The form input for our widgets"""

    def _add_frame(self, label, cols=3):
        """Add a LabelFrame to the form"""

        frame = ttk.LabelFrame(self, text=label)    # Page 107
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame   # Page 108

        r_info = self._add_frame("Record Information")   # Page 108

        LabelInput(
            r_info, "Date",var=self._vars['Date']
        ).grid(row=0, column=0)
        LabelInput(
            r_info, "Time", input_class=ttk.Combobox,
            var=self._vars['Time'],
            input_args={"values": ["8:00", "12:00", "16:00", "20:00"]}
            ).grid(row=0, column=1)
        LabelInput(
            r_info, "Technician", var=self._vars['Technician']
        ).grid(row=0, column=2)    # Page 108

        LabelInput(
            r_info, "Lab", input_class=ttk.Radiobutton,
            var=self._['Lab'],
            input_args={"values": ["A", "B", "C"]}
        ).grid(row=1, column=0)
        LabelInput(
            r_info, "Plot", input_class=ttk.Combobox,
            var=self._vars["Plot"],
            input_args={"values": list(range(1, 21))}
        ).grid(row=1, column=1)
        LabelInput(
            r_info, "Seed Sample", var=self._vars["Seed Sample"]
        ).grid(row=1, column=2)    #  end of page 108

        e_info = self._add_frame("Environment Data")    #  Page 109

        LabelInput(
            e_info, "Humidity (g/m3)",
            input_class=ttk.Spinbox, var=sef._vars["Humidity"],
            input_args={"from_": 0.5, "to": 52.0, "increment": .01}
        ).grid(row=0, column=0)
        LabelInput(
            e_info, "Light (klx)", input_class=ttk.Spinbox,
            var=self._vars["Light"],
            input_args={"from_": 0, "to": 100,  "increment": .01}
        ).grid(row=0, column=1)
        LabelInput(
            e_info, "Temperature (C)",
            input_class=ttk.Spinbox, var=self._vars["Temperature"],
            input_args={"from_": 4, "to": 40, "increment": .01}
        ).grid(row=0, column=2)
        LabelInput(
            e_info, "Equipment Fault",
            input_class=ttk.Checkbutton,
            var=self._vars["Equipment Fault"]
        ).grid(row=1, column=0, columnspan=3)     #  Page 109     Sunday September 7th, @ 0756


        p_info = self._add_frame("Plant data")     #  Page 109

        LabelInput(
            p_info, "Plants", input_class=ttk.Spinbox,
            var=self._vars['Plants'],
            input_args={"from_": 0, "to": 20}
        ).grid(row=0, column=0)
        LabelInput(
            p_info, "Blossoms", input_class=ttk.Spinbox,
            var=self._vars['Blossoms'],    #    Page 109      Sunday 7th September @0931
            input_args={"from_": 0, "to": 1000}
        ).grid(row=0, column=1)     #   Sunday September 7th @ 0933      Page 110
        LabelInput(
            p_info, "Fruit", input_class=ttk.Spinbox,
            var=self._vars["Fruit"],
            input_args={"from_": 0, "to": 1000}
        ).grid(row=0, column=2)
        LabelInput(
            p_info, "Min Height (cm)",
            input_class=ttk.Spinbox, var=self._vars['Min Height'],
            input_args={"from_": 0, "to": 1000, "increment": .01}
        ).grid(row=1, column=0)
        LabelInput(
            p_info, "Max Height (cm)",
            input_class=ttk.Spinbox, var=self._vars["Max Height"],
            input_args={"from_": 0, "to": 1000, "increment": .01}
        ).grid(row=1, column=1)
        LabelInput(
            p_info, "Median Height (cm)",    #   Page 110
            input_class=ttk.Spinbox, var=self._vars['Med Height'],
            input_args={"from_": 0, "to": 1000, "increment": .01}
        ).grid(row=1, column=2)  #  Page 110
        LabelInput(      # Lets add our Notes section      Page 110
            self, "Notes",
            input_class=BoundText, var=self._vars["Notes"],
            input_args={"width": 75, "height": 10}
        ).grid(sticky=tk.W, row=3, column=0)

        #  Now its time for the buttons
        buttons = tk.Frame(self)
        buttons.grid(sticky=tk.W + tk.E, row=4)
        self.savebutton = ttk.Button(
            buttons, text="Save", command=self.master._on_save)
        self.savebutton.pack(side=tk.RIGHT)

        self.resetbutton = ttk.Button(
            buttons, text="Reset", command=self.reset)
        self.resetbutton.pack(side=tk.RIGHT)    #    end f page 110




    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._vars  = {    # Page 107
            'Date': tk.StringVar(),
            'Time': tk.StringVar(),
            'Technician': tk.StringVar(),
            'Lab': tk.StringVar(),
            'Plot': tk.IntVar(),
            'Seed Sample': tk.StringVar(),
            'Humidity': tk.DoubleVar(),
            'Light': tk.DoubleVar(),
            'Temperature': tk.DoubleVar(),
            'Equipment Fault': tk.BooleanVar(),
            'Plants': tk.IntVar(),
            'Blossoms': tk.IntVar(),
            'Fruit': tk.IntVar(),
            'Min Height':tk.DoubleVar(),
            'Max Height': tk.DoubleVar(),
            'Med Height': tk.DoubleVar(),
            'Notes': tk.StringVar()
        }   #  Saturday 6th September 2025 @1745   # page 107

r_info = ttk.LabelFrame(drf, text='Record Information')
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)








class ValidatedMixin:
    """Adds a validation functionality to an input widget"""

    def __init__(self, *args, error_var=None, **kwargs):
        self.error = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)


        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)

        self.configure(
            validate = 'all',
            validatecommand=(vcmd, '%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(invcmd, '%P', '%s', '%S', '%V', '%i', '%d')
        )  # Page 133

    def _toggle_errr(self, on=False):
        self.configure(foreground=('red' if on else 'black'))   #page 133


    def _validate(self, proposed, current, char, event, index, action):
        self.error.set('')
        self._toggle_errr()
        valid = True
        # if the widget is disabled, don't validate
        state = str(self.configure('state')[-1])
        if state == tkinter.DISABLED:
            return valid

        if event == 'focusout':
            valid = self._focusout_validate(event=event)
        elif event == 'key':   # Page 133
            valid = self._key_validate(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )
            return valid   # Page 134

    def _focusout_validate(self, **kwargs):
        return True

    def _key_validate(self, **kwarg):
        return True          # Page 134


    def _invalid(self, proposed, current, char, event, index, action):   # Page 135
        if event == 'focusout':
            self._focusout_invalid(event=event)
        elif event == 'key':
            self._key_invalid(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )


    def _focusout_invalid(self, **kwargs):   # Page 135
        """Handle invalid data on a focus event."""
        self._toggle_errr(True)


    def _key_invalid(self, **kwargs):
        """Handle invalid data on a key event.
         By default we want to do nothing"""
        pass

    def trigger_focusout_validation(self):# Page 135
        valid = self._validate('', '', '', 'focusout', '', '')
        if not valid:
            self._focusout_invalid(event='focuout')
        return valid




#################################################

class RequiredEntry(ValidatedMixin, ttk.Entry):   # Page 136
    """An entry that require a value"""
    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid

class DateEntry(ValidatedMixin, ttk.Entry):  # Page 137  1052 on 4th September 2025
    """An Entry that only accepts ISO Date strings"""

    def _key_validate(self, action, index, char, **kwarg):
        valid = True

        if action == '0':  # This is a delete action
            valid = True
        elif index in ('0', '1', '2', '3', '5', '6', '8', '9'):
            valid = char.isdigit()
        elif index in ('4', '7'):
            valid = char == '-'
        else:
            valid = False
        return  valid

    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            self.error.set('A value is required')
            valid = False
        try:
            datetime.strptime(self.get(), '%Y-%m-%d')
        except ValueError:
            self.error.set('Invalid date')
            valid = False
        return valid

class ValidatedCombobox(ValidatedMixin, ttk.Combobox):   #  P138 on  Thursday 4th September 2025 @1117
    """A combbox that only takes values from its string lit"""

    def _key_validate(self, proposed, action, **kwargs):
        valid = True
        if action == '0':
            self.set('')
            return True

        values = self.cget('values')
        # Do a case-insensitive match against the entered text
        matching = [
            x for x in values     #  P139 on  Thursday 4th September 2025 @1130
            if x.lower().startswith(proposed.lower())
        ]
        if len(matching) == '0':
            valid = False
        elif len(matching) == '1':
            self.set(matching[0])
            self.icursor(tk.END)
            valid = False
        return  valid

 #  End/Strat on P139 on  Friday 5th September 2025 @08:56
    def _focusout_validate(self, **kwargs):
        valid = True
        if not self.get():
            valid = False
            self.errr.set('A value is required')
            return valid

# A range-limited spinbox widget --- Page 140

from decimal import Decimal, InvalidOperation

class ValidatedSpinbox(ValidatedMixin, ttk.Spinbox):
    def __init__(
            self, *args, from_='-Infinity', to='infinity', **kwargs
    ):

        super().__init__(*args, from_=from_, to=to, **kwargs)   # Page 141
        increment = Decimal(str(kwargs.get('increment', '1.0')))
        self.precision = increment.normalize().as_tuple().exponent


    def _key_validate(   #  Reducing Uer Error with Validation and Automation - Page 142
            self, char, index, current, proposed, action, **kwargs
    ):
        if action == '0':
            return True
        valid = True
        min_val = self.cget('from')
        max_val = self.cget('to')
        no_negative = min_val >= 0
        no_decimal = self.precision >= 0

        if any([
            (char not in '-1234567890'),
            (char == '-' and (no_negative or index != '0')),
            (char == '.' and (no_decimal or '.' in current))
            ]):
            return  False

# Page 143

        if proposed in '-':   # Page 143
            return True

        proposed = Decimal(proposed)
        proposed_precision = proposed.as_tuple().exponent

        if any([
            (proposed > max_val),
            (proposed_precision < self.precision)
        ]):
            return False
        return valid

    def _focusout_validate(self, **kwargs):
        valid = True
        value = self.get()
        min_val = self.cget('from')
        max_val = self.cget('to')

        try:
            d_value = Decimal(value)
        except InvalidOperation:
            self.error.set(f'Invalid number string: {value}')
            return False

        if d_value < min_val:
            self.error.set(f'Value is too low (min {min_val})')   # Page 144
            valid = False
        if d_value > max_val:
            self.error.set(f'Value is too high (max {max_val})')
            valid = False
        return valid


#  validating Radiobutton widgets  - Page 144

class ValidatedRadioGroup(ttk.Frame):
    """A Validated radio button group"""

    def __int__(
            self, *args, variable=None, error_var=None,
             values=None, button_args=None, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.variable = variable or tk .StringVar()     # Page 145
        self.error = error_var or tk.StringVar()
        self.values = values or list()
        self.button_args = button_args or dict()

        for v in self.values:
            button = ttk.Radiobutton(
                self, value=v, text=v,
                variable=self.variable, **self.button_args
            )
            button.pack(
                side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill='x'
            )
        self.bind('<FocusOut>', self.trigger_focusout_validation)
    def trigger_focusout_validation(self, *_):      # Page 146   Friday 5th September 2025 @1030 - Page 94
        self.error.set('')
        if not self.variable.get():
            self.error.set('A value is required')


            # Saturday 6th September 2025 @0952    on Page 146


    def on_reset(self):   #   Tuesday September 09th 2025 @1813      Page 73
        """called when reset button is clicked, or after save"""

        for variable in variables.values():
            if isinstance(variable, tk.BooleanVar):
                variable.set(False)
            else:
                variable.set('')
        notes_inp.delete('1.0', tk.END)

    reset_button.configure(command=on_reset)


def on_save(self):     #   Page 74
        """Handle save button clicks"""

        global records_saved

        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = f"abq_data_record_{datestring}.csv"
        newfile = not Path(filename).exists()   #  Page 75


#  Now it time to get the data from the form
    data = dict()
    fault = variables["Equipment Fault"].get()
    for key, variable in variables.items():
        if fault and key in ('Light', 'Humidity', 'Temperature'):
            data[key] = ''
        else:
            try:
                data[key] = variable.get()
            except tk.TclError:
                status_variable.set(
                    f'Error in field: {key}. Data was not saved!'
                )
                return
        # get the Text widget contents separately
        data["Notes"] = notes_inp.get('1.0', tk.END)









if __name__ == "__main__":   #  Sunday 7th September 2025 @1024    Page 114
    app = LabelInput()
    app.mainloop()








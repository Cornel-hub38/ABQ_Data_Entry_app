# data _entry_app.py   Page 136

from tkinter import tk   # Saturday 6th September 2025 @1014 on starting on page 100
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv


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

















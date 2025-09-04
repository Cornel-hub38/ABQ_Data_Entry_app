# data _entry_app.py   Page 136


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

class DateEntry(ValidatedMixin, ttk.Entry)# Page 137  1052 on 4th September 2025
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

class ValiddatedCombobox(ValidatedMixin, ttk.Combobox):   #  P138 on  Thursday 4th September 2025 @1117
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

 #  End/Strat on P139 on  Friday 5th September 2025 @0


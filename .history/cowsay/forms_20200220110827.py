from forms import ModelForm


class cowform(forms.ModelForm):
    class Meta:
        model = cowform
        fields = [
            'first_name',
            'last_name',
            'username'
        ]

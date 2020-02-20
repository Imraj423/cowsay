from forms import ModelForm


class cowform(forms.ModelForm):
    class Meta:
        model = Cow
        fields = [
            'first_name',
            'last_name',
            'username'
        ]

from django.forms import ModelForm


class cowform(ModelForm):
    class Meta:
        model = Cow
        fields = [
            'first_name',
            'last_name',
            'username'
        ]

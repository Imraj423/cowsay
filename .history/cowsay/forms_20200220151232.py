from django.forms import ModelForm
from .models import Cow


class cowform(ModelForm):
    class Meta:
        model = Cow
        fields = [
            'text_input',
            'cow_type'
        ]
        



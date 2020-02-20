from django.forms import ModelForm
from .models import Cow


class cowform(ModelForm):
    class Meta:
        model = Cow
        fields = __all__

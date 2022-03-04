from django.forms import ModelForm
from ClassifierApp.models import Entry

# Django форма для заполнения сгенерированная
class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['image']

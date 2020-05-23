from django import forms
from .models import Repository
import datetime

class RepoForm(forms.ModelForm):
    created_on = forms.DateField(
        label="When was this repository created?",
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year+1))
    )

    def __init__(self, *args, **kwargs):
        super(RepoForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Repository
        fields = ("__all__")
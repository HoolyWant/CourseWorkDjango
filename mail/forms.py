from django import forms

from mail.models import MessagesForDistribution, Client, MailDistributionSettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessagesForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MessagesForDistribution
        exclude = ('user', )


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user', )


class MaillingForm(forms.ModelForm):
    class Meta:
        model = MailDistributionSettings
        exclude = ('user', )

        widgets = {
            'date_start': forms.TimeInput(attrs={'type': 'time'}),
            'date_finish': forms.TimeInput(attrs={'type': 'time'}),
        }

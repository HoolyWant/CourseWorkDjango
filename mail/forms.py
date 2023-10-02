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
        fields = '__all__'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MaillingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailDistributionSettings
        fields = '__all__'

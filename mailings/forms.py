from django import forms

from mailings.models import Mailings, Message


class MailingsForm(forms.ModelForm):
    class Meta:
        model = Mailings
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data in ['хуй', 'пизда',
                            'хуевый', 'пидар', 'пидарас',
                            'охуели', 'сука', 'суки', 'пидарасы', 'пидары']:
            raise forms.ValidationError("Недопустимое название продукта")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'comment']
        labels = {
            'name': 'Nombre',
            'comment': 'Comentario'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre',
                    'id': 'name',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su comentario',
                    'id': 'comment',
                }
            )
        }


class RoomModelForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = "__all__"


# Readonly filed or disable so that it can't be editable.

class ItemForm(forms.ModelForm):
    readonly = ('sku',)
    verbose_name_plural = 'Itemformxxxxxx'
    class Meta:
        model = models.Item
        fields = "__all__"

    def __init__(self, *args,**kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for x in self.readonly:
            self.fields[x].widget.attrs['disable'] =True

    def clean(self):
        data = super(ItemForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data

    def clean_sku(self):
        if self.instance:
            return self.instance.sku
        else:
            return self.fields['sku']

class ManufacturerModelForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ManufacturerModelForm, self).clean()
        name = cleaned_data.get('name')
        if models.Manufacturer.objects.filter(name=name).exists():
            raise forms.ValidationError('Category already exists')
    class Meta:
        model = models.Manufacturer
        fields ="__all__"

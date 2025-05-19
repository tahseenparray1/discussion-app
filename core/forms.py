from django.forms import ModelForm
from . import models
class CreateComment(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
class CreateLink(ModelForm):
    class Meta:
        model = models.Link
        fields = ['title','url']
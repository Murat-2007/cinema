from django import forms
from django.forms import widgets
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        numbers =(
            ('1','1 Yildiz'),
            ('2','2 Yildiz'),
            ('3','3 Yildiz'),
            ('4','4 Yildiz'),
            ('5','5 Yildiz'),
        )
        model = Comment
        #fields = ['full_name', 'e_mail', 'text', 'rating']
        exclude = ['movie','date_added',]
        labels = {
            "full_name": "Ad - Soyad",
            "e_mail": "Eposta",
            "text": "Yorum",
            "rating": "Puan"
        }
        widgets = {
            "full_name": widgets.TextInput(attrs={"class":"form-control"}),
            "e_mail": widgets.EmailInput(attrs={"class":"form-control"}),
            "text": widgets.Textarea(attrs={"class":"form-control"}),
            "rating": widgets.Select(attrs={"class":"form-control custom-select"}, choices=numbers),
        }
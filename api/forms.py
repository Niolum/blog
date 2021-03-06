from django import forms
from .models import Comment, Post, Category


class AddPostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(label="Категории", 
                                                queryset=Category.objects.all(), 
                                                widget=forms.SelectMultiple, 
                                                to_field_name='name')

    class Meta:
        model = Post
        fields = ("title", "text", "categories")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ("name",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }
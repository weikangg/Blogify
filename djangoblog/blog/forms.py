from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"] # exclude the post field, since we don't want to let the user set it.
        labels = {
            "user_name": "Your Name",
            "email": "Your email",
            "text": "Your comment"
        }
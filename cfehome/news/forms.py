from django import forms
from .models import News,Comment


class NewsForm(forms.ModelForm):
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    content     = forms.CharField(
                        required=False,
                        label='', 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "NEWS CONTENT",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 160
                                }
                            )
                        )
    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'image',
        ]
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid title")
        return title

class CommentForm(forms.ModelForm):

    #def __init__(self, *args, **kwargs):
    #   self.author = kwargs.pop('author', None)
    #    self.post = kwargs.pop('post', None)
    #    super().__init__(*args, **kwargs)

    #    comment = super().save(commit=False)
    #    comment.author = self.author
    #    comment.post = self.post
    #    comment.save()

    class Meta:
        model = Comment
        fields = ["body"]
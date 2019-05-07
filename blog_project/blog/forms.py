from django import forms

from .models import Post, Comment, Przedszkolak


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class KidForm(forms.ModelForm):

    class Meta:
        model = Przedszkolak
        fields = ('Imię', 'Nazwisko', 'nazwa_skrócona', 'rodzic', 'grupa',)

        #widgets = {
            #'Imię': forms.TextInput(attrs={'class': 'textinputclass'}),
        #    'Nazwisko': forms.TextInput(attrs={'class': 'textinputclass'}),
        #'nazwa_skrócona': forms.TextInput(attrs={'class': 'textinputclass'}),
        #}

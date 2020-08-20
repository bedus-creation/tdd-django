from django import forms
from front.models.posts import Posts


class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'slug', 'body']

    title = forms.CharField(label='Thread Title', min_length='3',
                            max_length=100,  widget=forms.TextInput(attrs={'class': "w-full mt-2 mb-6 px-2 py-2 border rounded-lg text-gray-700 focus:outline-none focus:border-green-500"}))

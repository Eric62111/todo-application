
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter task description',
                'rows': 4
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '')

        if not title.strip():
            raise forms.ValidationError(
                'Task title cannot be empty or contain only spaces.'
            )

        if len(title) > 150:
            raise forms.ValidationError(
                'Task title cannot exceed 150 characters.'
            )

        return title.strip()

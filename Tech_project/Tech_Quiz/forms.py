from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super(QuizForm, self).__init__(*args, **kwargs)
        
        if questions:
            for question in questions:
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.text,
                    choices=[(option.id, option.text) for option in question.options.all()],
                    widget=forms.RadioSelect,
                    required=False
                )
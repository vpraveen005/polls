# from django import forms
# from django.core.exceptions import ValidationError
#
# class QuesionForm(forms.Form):
#     question_text = forms.CharField(max_length=200)
#     class Meta:
#         fields = ['question_text']
#
#     # def clean(self):
#
#
#     def clean_question_text(self):
#         question = self.cleaned_data['question_text']
#         if not question.strip().endswith('?'):
#             raise ValidationError('Question should ends with "?"')
#         else:
#             return question

from django import forms
from django.core.exceptions import ValidationError
from .models import Email


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)

    class Meta:
        fields = '__all__'

    def clean_question_text(self):
        question = self.cleaned_data["question_text"]
        if not question.strip().endswith("?"):
            raise ValidationError("Question should ends with '?'")
        return question

# class MailForm(forms.Form):
#     mail_from_text = forms.CharField(max_length=100)
#     mail_to_text = forms.CharField(max_length=100)
#     subject_text = forms.CharField(max_length=100)
#
#     class Meta:
#         fields = '__all__'
#
#     def clean_mail_from_text(self):
#         mail_from_text = self.cleaned_data['mail_from_text']
#         if not mail_from_text.endswith('com'):
#             raise ValidationError('Mail should end with ".com"')
#         return mail_from_text
#
#     def clean_mail_to_text(self):
#         mail_to_text = self.cleaned_data['mail_to_text']
#         if not mail_to_text.endswith('com'):
#             raise ValidationError('Mail should end with ".com"')
#         return mail_to_text
#
#     def clean_subject_text(self):
#         subject_text = self.cleaned_data['subject_text']
#         return subject_text


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
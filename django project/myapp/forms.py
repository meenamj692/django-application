from django import forms
from myapp.models import Topic, Student

class TopicForm(forms.ModelForm):
    subject = forms.CharField(label='Subject',max_length=100, required=False)
    intro_course = forms.BooleanField(label='This should be an introductory level course', required=False)
    avg_age = forms.IntegerField(label='What is Your Age')
    class Meta:
        model=Topic
        fields='__all__'
        widgets={
            'time':forms.RadioSelect(attrs={'class':'radio'}),

        }

class InterestForm(forms.Form):
    CHOICES=(
        (0,'no'),
        (1,'yes')
    )
    interested= forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
    age = forms.IntegerField(initial=20, label='Age of Use')
    comments = forms.Textarea(attrs={'required':'false'})
    comments.id_for_label('Additional Conditions')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'username','email','password','address','city','age','profile_pic')

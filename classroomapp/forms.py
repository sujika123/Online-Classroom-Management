from django import forms
from django.contrib.auth.forms import UserCreationForm
import datetime

from classroomapp.models import Login, courseadd, teacherlogin, studentadd, notificationadd, stdleaveshedule, \
    tchrleaveshedule, addnotes, taddAsgnmnttopic, SaddAssignments, Attendance, StdntComplaint, TchrComplaint, Question, \
    Mark


class DateInput(forms.DateInput):
    input_type="date"

class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2= forms.CharField(widget=forms.PasswordInput, label='confirm password')
    class Meta:
        model=Login
        fields=('username','password1','password2',)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class userloginform(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model=teacherlogin
        fields=('name','age','address','subject','phone','tid','gender','image')

class courseddform(forms.ModelForm):
   # date=forms.DateField(widget=DateInput)
    class Meta:
        model=courseadd
        fields=('dept','subject','teacher','description')

class studentloginform(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model=studentadd
        fields=('name','dob','age','address','semester','dept','phone','sid','gender','photo')

class notificationform(forms.ModelForm):

    class Meta:
        model=notificationadd
        fields=('name','description')

class stdleavesheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:

        model=stdleaveshedule
        fields=('title','date','content')

class tchrleavesheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:

        model=tchrleaveshedule
        fields=('title','date','content')


class StdntComplaintForm(forms.ModelForm):
    # date = forms.DateField(widget=DateInput)

    class Meta:
        model = StdntComplaint
        fields = ('subject', 'complaint')


class TchrComplaintForm(forms.ModelForm):
    # date = forms.DateField(widget=DateInput)

    class Meta:
        model = TchrComplaint
        fields = ('subject', 'complaint')



class notesddform(forms.ModelForm):
    class Meta:
        model=addnotes
        fields=('subject','title','description','file')


class taddAsgnmnttopicform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=taddAsgnmnttopic
        fields=('subject','title','date')


class sAssignmentddform(forms.ModelForm):

    class Meta:
        model=SaddAssignments
        fields=('subject','title','file')

att_choice = (
    ('present', 'present'),
    ('absent', 'absent')
)

class AddAttendanceForm(forms.ModelForm):
    student=forms.ModelChoiceField(queryset=studentadd.objects.all())
    attendance=forms.ChoiceField(choices=att_choice,widget=forms.RadioSelect)
    class Meta:
        model=Attendance
        fields=('student','attendance')

ANSWER_CHOICES=(
    ('option1','option1'),
    ('option2','option2'),
    ('option3','option3'),
    ('option4','option4'),
)

class QuestionForm(forms.ModelForm):
    # Ans = forms.ChoiceField(choices=ANSWER_CHOICES, widget=forms.CheckboxSelectMultiple)
    Ans = forms.ChoiceField(choices=ANSWER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Question
        fields = ('question', 'Ans', 'option_1','option_2','option_3','option_4')


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('student','name','mark')



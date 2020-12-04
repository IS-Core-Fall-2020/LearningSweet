from django import forms
# from django.forms import ModelForm
# from myapp.models import Article
from django.contrib.auth.models import User
from loginpage.models import Group, Assignment
from datetime import datetime, timedelta



##https://docs.djangoproject.com/en/3.1/topics/forms/


    
class UserGroupForm(forms.ModelForm) :
    group_name = forms.CharField(max_length=30, label='Group Name')
    group_description = forms.CharField(max_length=100, label='Group Description')
    # user = forms.ModelMultipleChoiceField(queryset=User.objects.all().order_by('first_name'), widget=forms.CheckboxSelectMultiple(), required=False)
    user = forms.ModelMultipleChoiceField(queryset=User.objects.all().order_by('username'))

    class Meta:
        model = Group
        fields = ('group_name', 'group_description', 'user')



class AssignmentForm(forms.ModelForm) :
    assign_name = forms.CharField(max_length=30, label='Assignment Name')
    assign_description = forms.CharField(max_length=250, label='Assignment Description')
    assign_completion = forms.CheckboxInput()
    assign_duedate = forms.DateField(label='Due Date', widget=forms.SelectDateWidget)
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = Assignment
        fields = ('assign_name', 'assign_description', 'assign_completion', 'assign_duedate', 'group')

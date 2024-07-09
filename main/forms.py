from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ToDoItem

class SignUpForm(UserCreationForm):
    email = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "uk-input", "placeholder": "Email"}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "uk-input", "placeholder": "First Name"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "uk-input", "placeholder": "Last Name"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'uk-input'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="uk-input text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'uk-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'uk-input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted small"><small>Enter the same password as before, for verification.</small></span>'




class TaskForm(forms.ModelForm):

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Adjust format according to your needs
    )
    class Meta:
        model= ToDoItem
        fields=["title","description","due_date","completed","priority","categories"]

    def __init__(self,*args,**kwargs):
        super(TaskForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class']="uk-input"
        self.fields['title'].widget.attrs['placeholder']="Enter your task Title !"
        self.fields['title'].lable=""


        self.fields['description'].widget.attrs['class']="uk-textarea"
        self.fields['description'].widget.attrs['placeholder']="Enter task description !"
        self.fields['description'].lable=""


        self.fields['due_date'].widget.attrs['class']="uk-input"
        self.fields['due_date'].widget.attrs['type']="date"
        self.fields['due_date'].widget.attrs['placeholder']="Enter task date !"
        self.fields['due_date'].lable=""
        


        self.fields['completed'].widget.attrs['class']="uk-radio"
        
        self.fields['completed'].lable=""



        self.fields['priority'].widget.attrs['class']="uk-select"
        
        self.fields['priority'].lable=""


        self.fields['categories'].widget.attrs['class']="uk-select"
        
        self.fields['categories'].lable=""





class UpdateTask(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Adjust format according to your needs
    )
    class Meta:
        model= ToDoItem
        fields=["title","description","due_date","completed","priority","categories"]

    def __init__(self,*args,**kwargs):
        super(UpdateTask,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class']="uk-input"
        self.fields['title'].widget.attrs['placeholder']="Enter your task Title !"
        self.fields['title'].lable=""


        self.fields['description'].widget.attrs['class']="uk-textarea"
        self.fields['description'].widget.attrs['placeholder']="Enter task description !"
        self.fields['description'].lable=""


        self.fields['due_date'].widget.attrs['class']="uk-input"
        self.fields['due_date'].widget.attrs['type']="date"
        self.fields['due_date'].widget.attrs['placeholder']="Enter task date !"
        self.fields['due_date'].lable=""
        


        self.fields['completed'].widget.attrs['class']="uk-radio"
        
        self.fields['completed'].lable=""



        self.fields['priority'].widget.attrs['class']="uk-select"
        
        self.fields['priority'].lable=""


        self.fields['categories'].widget.attrs['class']="uk-select"
        
        self.fields['categories'].lable=""




class FilterForm(forms.Form):
    priority = forms.ChoiceField(choices=[('', 'All Priorities'), ('L', 'Low'), ('M', 'Medium'), ('H', 'High')], required=False)
    completed = forms.ChoiceField(choices=[('', 'All'), ('true', 'Completed'), ('false', 'Not Completed')], required=False)

    def __init__(self,*args,**kwargs):
        super(FilterForm,self).__init__(*args,**kwargs)
        self.fields['priority'].widget.attrs['class']="uk-select"
        self.fields['completed'].widget.attrs['class']="uk-select"




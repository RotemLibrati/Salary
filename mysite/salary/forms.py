from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    user_name = forms.CharField(initial='')
    password = forms.CharField(widget=forms.PasswordInput(), initial='')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address', 'age', 'payment')
        
        
class CompleteUserForm(UserCreationForm):  # create user - django
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  )

        def save(self, commit=True):
            user = super(CompleteUserForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
            return user

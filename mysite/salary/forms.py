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


class ChangePaymentForm(forms.Form):
    payment = forms.IntegerField()


class AddShifts(forms.Form):
    DAYS = (('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('07', '07'), ('08', '08'),
            ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
            ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'),
            ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'),
            ('30', '30'), ('31', '31'))
    MONTH = (('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('07', '07'), ('08', '08'),
             ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'))
    YEAR = (('20', '20'), ('21', '21'))
    day = forms.IntegerField(widget=forms.Select(choices=DAYS))
    month = forms.IntegerField(widget=forms.Select(choices=MONTH))
    year = forms.IntegerField(widget=forms.Select(choices=YEAR))
    start = forms.CharField(max_length=6)
    over = forms.CharField(max_length=6)
    PERCENT100 =  (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')
                   , ('9', '9'))
    PERCENT125 = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    PERCENT150 = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')
                   , ('9', '9'), ('9', '9'))
    PERCENT175 = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    PERCENT200 = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    percent100 = forms.IntegerField(widget=forms.Select(choices=PERCENT100))
    percent125 = forms.IntegerField(widget=forms.Select(choices=PERCENT125))
    percent150 = forms.IntegerField(widget=forms.Select(choices=PERCENT150))
    percent175 = forms.IntegerField(widget=forms.Select(choices=PERCENT175))
    percent200 = forms.IntegerField(widget=forms.Select(choices=PERCENT200))
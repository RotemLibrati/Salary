from datetime import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import AnonymousUser
from django.db.models.signals import post_save
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import CompleteUserForm, ProfileForm, LoginForm, ChangePaymentForm, AddShifts
from .models import UserProfile, User, Shifts

def index(request):
    context = {}
    if request.user is not None:
        context['user'] = request.user
    return render(request, 'salary/index.html', context)



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['user_name'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('salary:index'))
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'salary/login.html', context) #מועבר לדף זה לאחר לחיצה על התחברות בעמוד הקודם



def new_user(request):
    if request.method == 'POST':
        user_form = CompleteUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = get_object_or_404(User, username=user_form.cleaned_data['username'])
            return HttpResponseRedirect(reverse('salary:new-profile', args=[str(user.username)])) # לחיצה על כפתור submit תעביר אותי לקישור
    else: # מכניס אותי לדף עם הקישור למטה כי הוא עדיין לא זיהה form
        user_form = CompleteUserForm()
        context = {'user_form': user_form}
        return render(request, 'salary/new-user.html', context)
    
    
def new_profile(request, username):
    def attach_user(sender, **kwargs):
        userprofile = kwargs['instance']
        userprofile.user = user
        post_save.disconnect(attach_user, sender=UserProfile)
        userprofile.save()

    if request.method == 'POST':
        user = User.objects.get(username=username)
        form = ProfileForm(request.POST)
        if form.is_valid():
            post_save.connect(attach_user, sender=UserProfile)
            form.save()
            return render(request, 'salary/index.html')
    else:
        user = User.objects.get(username=username)
        form = ProfileForm()
    context = {'user': user, 'form': form}
    return render(request, 'salary/new-profile.html', context)


def logout(request):
    request.session.flush()
    if hasattr(request, 'user'):
        request.user = AnonymousUser()
    return HttpResponseRedirect(reverse('salary:index'))

def change_payment(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePaymentForm(request.POST)
        if form.is_valid():
            payment = form.cleaned_data['payment']
            user_profile = UserProfile.objects.get(user=user)
            user_profile.payment = payment
            user_profile.save()
            return HttpResponseRedirect(reverse('salary:index'))
    else:
        form = ChangePaymentForm()
    context = {'form': form}
    return render(request, 'salary/change-payment.html', context)

def add_shifts(request):
    user = request.user
    if request.method == 'POST':
        form = AddShifts(request.POST)
        if form.is_valid():
            day = form.cleaned_data.get('day')
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            start = form.cleaned_data.get('start')
            over = form.cleaned_data.get('over')
            percent100 = form.cleaned_data.get('percent100')
            percent125 = form.cleaned_data.get('percent125')
            percent150 = form.cleaned_data.get('percent150')
            percent175 = form.cleaned_data.get('percent175')
            percent200 = form.cleaned_data.get('percent200')
            up1 = UserProfile.objects.get(user=request.user)
            date = '{0}/{1}/{2}'.format(month, day, year)
            date_object = datetime.strptime(date, '%m/%d/%y')
            time = datetime.strptime(start, '%H:%M').time()
            time_over = datetime.strptime(over, '%H:%M').time()
            shift = Shifts(date=date_object, start=time, over=time_over, user=up1)
            shift.total = abs(datetime.strptime(str(time_over), '%H:%M:%S') - datetime.strptime(str(time), '%H:%M:%S'))
            shift.total = shift.total.seconds/60/60
            shift.save()
            return HttpResponseRedirect(reverse('salary:index'))
    else:
        form = AddShifts()
    context = {'form': form}
    return render(request, 'salary/add-shifts.html', context)

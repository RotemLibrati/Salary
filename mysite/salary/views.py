from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mysite.salary.forms import CompleteUserForm, LoginForm, ProfileForm
from mysite.salary.models import UserProfile

def index(request):
    return HttpResponse("Hello")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['user_name'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('salary:profile'))
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
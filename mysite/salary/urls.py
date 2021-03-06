from django.urls import path
from . import views as views

app_name = 'salary'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('new-user/', views.new_user, name='new-user'),
    path('<str:username>/new-profile/', views.new_profile, name='new-profile'),
    path('logout/', views.logout, name='logout'),
    path('change-payment/', views.change_payment, name='change-payment'),
    path('add-shifts/', views.add_shifts, name='add-shifts'),
    path('not-success/', views.not_success, name='not-success'),
    path('my-shifts/', views.my_shifts, name='my-shifts'),
    path('choose-month/', views.choose_month, name='choose-month'),
    path('remove-shifts/', views.remove_shifts, name='remove-shifts'),
]
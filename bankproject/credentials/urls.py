from django.urls import path
from.import views
app_name='credentials'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('welcome',views.welcome,name='welcome'),
    path('enrol', views.enrol, name='enrol'),
    path('form', views.form, name='form'),
    path('logout', views.logout, name='logout'),
    path('mypage', views.mypage, name='mypage'),
    path('fun', views.fun, name='fun')

]
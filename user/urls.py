from django.urls import path
from .views import login_view , home ,list , appsetting, school , update_appsetting, update_school , logout, desactivate_user , update_user,activate_user
from django.contrib.auth.views import LogoutView

app_name = 'user'
urlpatterns = [
    path('list/',list ,name='list'),
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('',appsetting,name='appsetting'),
    path('school/',school,name='school'),
    path('afficher_appsetting/',update_appsetting,name='afficher_appsetting'),
    path('afficher_school/',update_school,name='afficher_school'),
    path('desactivate/,<int:user_id>',desactivate_user,name='desactivate'),
    path('update/<int:id>',update_user , name='update_user'),
    path('activate/<int:id>',activate_user,name='activate')

]
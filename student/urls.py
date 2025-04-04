from django.urls import path
from student.views import add,list,update,delete , absence , delete_absence, absence_list , cards , search

app_name='student'
urlpatterns = [
  path('add/',add,name='add'),  
  path('list/',list,name='list'),
  path('update/<int:id>',update,name='update'),
  path('delete/<int:id>',delete,name='delete'),
  #absence
  path('absence/<int:id>',absence,name='absence'),
  path('delete_absence/<int:id>',delete_absence,name='delete_absence'),
  path('list_absence/',absence_list,name='list_absence'),
  #cards
  path('cards/<int:id>',cards,name='cards'),
  path('search/',search, name='search')

]
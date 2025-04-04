from django.urls import path
from rapport.views import rapport
app_name = 'rapport'
urlpatterns = [
  path('rapport/',rapport,name='rapport')
]
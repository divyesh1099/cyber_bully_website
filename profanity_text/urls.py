from django.urls import path
from . import views
app_name = 'profanity_text'
# url patterns
urlpatterns = [
    path("", views.index, name = 'index'),
    path("cuss",views.save_cusswords,name='cuss'),
    
]
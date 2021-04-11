from django.urls import path
from . import views
app_name = 'profanity_text_api'
# url patterns
urlpatterns = [
    path("", views.index, name = 'index'),
]
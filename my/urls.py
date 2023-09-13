from django.urls import path
from .views import main,person

urlpatterns = [
    path('', main,name='main'),
    path('persons/',person, name='persons'),
]
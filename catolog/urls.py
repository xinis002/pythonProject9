from django.urls import path, include
from catolog.apps import CatologConfig
from catolog.views import home, contacts

app_name = CatologConfig.name


urlpatterns = [
    path('', home, name='home' ),
    path('contacs/', contacts, name='contacts')
]

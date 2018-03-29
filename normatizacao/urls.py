from django.conf.urls import url
from . import views

app_name = 'normatizacao'

urlpatterns = [
    url(r'^', views.NormatizadorList.as_view(), name='normatizacao'),
]

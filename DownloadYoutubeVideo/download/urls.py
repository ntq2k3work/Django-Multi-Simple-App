from django.urls import path
from download import views
urlpatterns = [
    path('',views.index,name='download.index'),
    path('Download', views.Download, name='Download')
]

from xml.dom.minidom import Document
from django.urls import path
from . import views

urlpatterns = [
    path('<filenamew>', views.FilesView.as_view())
    ]
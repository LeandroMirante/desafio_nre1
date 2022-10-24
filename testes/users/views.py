from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.conf import settings
import os
from django.template.loader import render_to_string
from django.views.generic import ListView
from .models import Customer

def pdf_view(request,filenamew):
    #filepath = settings.MEDIA_ROOT + filename
    response_data = render_to_string("users/files.html")
    return HttpResponse(response_data)

class FilesView(ListView):
    template_name= "users/files.html"
    model = Customer
    context_object_name = "customer"




# C\\Users\\leand\\OneDrive\\Documentos\\Django Course\\custom_user_model\\testes\\files

# from django.http import FileResponse, Http404

# def pdf_view(request, filenamew):
#     try:
#         return FileResponse(open('Introducao_a_Mecanica_dos_Fluidos_Fox_Mc.pdf','rb'),content_type='application/pdf')
#     except:
#         raise Http404()
import csv

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser

from .serializers import ContactUploadSerializer
from .forms import ContactUploadForm
from .models import Contact

class FileUploadView(APIView):
    serializer_class = ContactUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def put(self, request, format=None):
        file_obj = request.data['file']
        print file_obj
        reader = csv.reader(file_obj)
        for row in reader:
            contact = Contact.objects.create_contact(row)
            # We could do checks here and return contacts that didn't get saved
        return Response(status=204)

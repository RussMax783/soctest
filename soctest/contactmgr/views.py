import csv

from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .forms import ContactUploadForm
from .models import Contact
from .serializers import ContactUploadSerializer, ContactSerializer


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


class RetrieveDestroyContact(generics.RetrieveDestroyAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.all()

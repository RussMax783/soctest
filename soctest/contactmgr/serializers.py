from rest_framework import serializers

from .models import Contact


class ContactUploadSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact


from .models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets


class ContactViewset(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset  = Contact.objects.all()
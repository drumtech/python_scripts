from django.shortcuts import render
from rest_framework import generics
from .serializer import ServerSerializer
from .serializer_my import ServerSerializer_my
from .serializer_additional import AddInfoSerializer
from .models import Server
from .models import AdditionalInformation

class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class StateViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer_my

class AddInfoViewSet(generics.ListAPIView):

    queryset = AdditionalInformation.objects.all()
    serializer_class = AddInfoSerializer

class AddInfoAddView(generics.CreateAPIView):

    queryset = AdditionalInformation.objects.all()
    serializer_class = AddInfoSerializer

class AddInfoDetailSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = AdditionalInformation.objects.all()
    serializer_class = AddInfoSerializer

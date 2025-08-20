from django.shortcuts import render
from rest_framework import generics
from .models import Tinta
from .serializer import TintaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TintaListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tinta.objects.all()
    serializer_class = TintaSerializer

class TintaDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    queryset = Tinta.objects.all()
    serializer_class = TintaSerializer
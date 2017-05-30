from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from places.serializers import CountrySerializer, StateSerializer
from places.models import Country, State
from rest_framework.mixins import ListModelMixin
# Create your views here.

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
# class StateListView(APIView):
    
#     def post(self, request, format=None):
#         country_code = request.data['country']
#         country = Country.objects.get(code=country_code)
#         states = State.objects.filter(country=country)
#         the_states = [StateSerializer(x) for x in states]
#         return Response(the_states)


class StateListView(generics.GenericAPIView, ListModelMixin):
    
    serializer_class= StateSerializer

    def post(self, request, *args, **kwargs):
        country_code = request.data['country']
        country = Country.objects.get(code=country_code)
        self.queryset = State.objects.filter(country=country)
        return self.list(request, *args, **kwargs)
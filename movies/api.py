from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Actor
from .serializers import (                                  Viewset - Это абстракция drf позволяет нам описывать методы
    ActorListSerializer,
    ActorDetailSerializer,
)


class ActorViewSet(viewsets.ViewSet):
    def list(self, request):              #выводим список
        queryset = Actor.objects.all()
        serializer = ActorListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):             #метод retrieve принимает Pk
        queryset = Actor.objects.all()                  #ищем данный обьект по Id,если будет такой обьект мы вернем
        actor = get_object_or_404(queryset, pk=pk)
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)

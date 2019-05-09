from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Key, Translation
from app.serializers import KeySerializer, TranslationSerializer


class KeyViewSet(viewsets.GenericViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer

    def list(self, request, *args, **kwargs):
        return Response({
            'keys': self.serializer_class(self.queryset.all(), many=True).data,
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'key': serializer.data,
        })

    def retrieve(self, request, *args, **kwargs):
        return Response({
            'key': self.serializer_class(self.get_object()).data,
        })

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            instance=self.get_object(),
            data=request.data,
            partial=False,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'key': serializer.data,
        })


class TranslationListView(generics.GenericAPIView):
    serializer_class = TranslationSerializer
    # lookup_field = 'locale'

    def get_queryset(self):
        key_id = self.kwargs.get('key_id')
        return Translation.objects.filter(key_id=key_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response({
            'translations': self.serializer_class(queryset.all(), many=True).data,
        })


class TranslrationDetailView(generics.GenericAPIView):
    serializer_class = TranslationSerializer

    def get_queryset(self):
        key_id = self.kwargs.get('key_id')
        locale = self.kwargs.get('locale')
        return Translation.objects.filter(key_id=key_id, locale=locale)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({
            'translation': self.serializer_class(obj).data,
        })

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            key=Key.objects.get(id=self.kwargs.get('key_id')),
            locale=self.kwargs.get('locale'),
        )
        return Response({
            'translation': serializer.data,
        })

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            instance=self.get_object(),
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'translation': serializer.data,
        })

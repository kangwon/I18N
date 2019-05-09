from rest_framework import viewsets
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


class TranslationViewSet(viewsets.ModelViewSet):
    lookup_field = 'locale'
    serializer_class = TranslationSerializer

    def get_queryset(self):
        key_id = self.kwargs.get('key_id')
        return Translation.objects.filter(key_id=key_id)

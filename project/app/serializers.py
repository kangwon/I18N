from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.models import Key, Translation


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('id', 'name')

    name = serializers.RegexField(
        '^[.a-z]+$',
        validators=[UniqueValidator(
            queryset=Key.objects.all(),
            message='key with this name already exists.',
        )]
    )


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('id', 'value', 'keyId', 'locale',)
        read_only_fields = ('locale', 'keyId',)

    keyId = serializers.PrimaryKeyRelatedField(source='key', read_only=True)

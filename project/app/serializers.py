from rest_framework import serializers

from app.models import Key, Translation


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('id', 'name')


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('id', 'value', 'keyId', 'locale',)
        read_only_fields = ('locale', 'keyId',)

    keyId = serializers.PrimaryKeyRelatedField(source='key', read_only=True)

from rest_framework import serializers

from app.models import Key, Translation


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('id', 'name')


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('id', 'value')
        readonlys = ('key_id', 'locale',)

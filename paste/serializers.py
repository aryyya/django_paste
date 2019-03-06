from .models import Paste, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

from rest_framework import serializers

class PasteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Paste
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.ModelSerializer):
    pastes = serializers.PrimaryKeyRelatedField(many=True, queryset=Paste.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'pastes')

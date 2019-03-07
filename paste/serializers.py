from .models import Paste, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

from rest_framework import serializers

class PasteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='paste-highlight', format='html')

    class Meta:
        model = Paste
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    pastes = serializers.HyperlinkedRelatedField(many=True, view_name='paste-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'pastes')

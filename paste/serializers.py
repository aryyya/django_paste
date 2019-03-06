from .models import Paste, LANGUAGE_CHOICES, STYLE_CHOICES

from rest_framework import serializers

class PasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

from rest_framework import serializers
from .models import ClothingItem
from sorl.thumbnail import get_thumbnail

class ClothingItemSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = ClothingItem
        fields = ['id', 'name', 'thumbnail', 'color', 'description']

    def get_thumbnail(self, obj):
        """
        This will generate and cache a thumbnail
        :param obj:
        :return: a url for a thumbnail image
        """
        if obj.image:
            # Generate a thumbnail of the desired size (e.g., 100x100)
            thumbnail = get_thumbnail(obj.image, '100x100', crop='center', quality=99)
            return self.context['request'].build_absolute_uri(thumbnail.url)
        return None
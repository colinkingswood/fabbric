import io
import base64

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from prototype.images import change_color
from prototype.models import ClothingItem
from prototype.serializers import ClothingItemSerializer


class ClothingItemViewSet(viewsets.ModelViewSet):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer

    @action(detail=True, methods=['post'])
    def customize_color(self, request, pk=None):
        """
        This is a custom endpoint on the Clothing Item Viewset, it will take a hexcolor and a clothing item
        and adjust the image by applying the color

        :param request:
        :param pk:
        :return: An HTTP response, with the image as Base64 encoded png
        """
        clothing_item = self.get_object()

        # Get the color from the request
        color = request.data.get('color')

        # customize the image with the color
        image_path = clothing_item.image.path
        custom_image = change_color(image_path, color)

        # convert the image to base64 and return it in the response
        buffer = io.BytesIO()
        custom_image.save(buffer, format='PNG')
        image_png = buffer.getvalue()
        image_base64 = base64.b64encode(image_png)
        image_data = 'data:image/png;base64,' + image_base64.decode('utf-8')

        return HttpResponse(image_data)



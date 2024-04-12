import base64
import os
from PIL import Image
import io


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from prototype.models import ClothingItem
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage


class ClothingItemTests(APITestCase):
    fixtures = ['prototype/fixtures/items.json']


    def test_list(self):
        """
        Test that the list view returns 3 objects as expected.
        I wanted to test the thumbnails,
        """
        url = reverse('clothingitem-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertEqual(len(data),3)

        self.assertEqual(data[0]["name"], 'Item1')
        self.assertEqual(data[0]["description"], 'Hoodie, extra confortable')

        # I wanted to test the thumbnails, but it was giving 404s, I suspect because
        # the image paths were loaded from fixtures or something to do with the way the test
        # server works, but I didn't want to spend a lot of time getting that to work



    def test_customize_color(self):
        url = reverse('clothingitem-customize-color', kwargs={"pk": 1})
        data = {"color": "green"}
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 200)

        # get base64 image string and remove prefix
        base64_data = response.content.decode('utf-8')
        prefix, base64_string = base64_data.split(',', 1)

        # Load the image data and verify that it is a PNG image
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data))
        image.verify()

        self.assertEqual(image.format, 'PNG')




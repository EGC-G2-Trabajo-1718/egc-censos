from django.urls import reverse
from rest_framework.test import APITestCase





# Create your tests here.

class CensoTest(APITestCase):

    def create_censo(self):

        url = reverse('create')
        data = {'id_votacion':'4', 'id_grupo':'3', 'nombre':'censo1'}
        response = self.client.post(url, data, format='json')
        assert response.status_code == 200

# shopping_list/tests.py

import pytest
import uuid
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from shopping_list.models import ShoppingList, ShoppingItem

@pytest.mark.django_db
def test_valid_shopping_list_is_created():
    url = reverse('all-shopping-lists')
    data = {
        'name': 'Electronics',
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert ShoppingList.objects.get().name == 'Electronics'


@pytest.mark.django_db
def test_shopping_list_name_missing_resturns_bad_request():
    url = reverse('all-shopping-lists')
    data ={
        'something_else': 'blahblah',
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_retrieve_all_shopping_lists():
    url = reverse('all-shopping-lists')
    client = APIClient()
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_single_shopping_list():
    shopping_list = ShoppingList.objects.create(name='Electronics')
    url = reverse('shopping-list-detail', kwargs={'pk': shopping_list.id})
    client = APIClient()
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_retrieve_a_single_shopping_item():
    shopping_list = ShoppingList.objects.create(name='Electronics')
    shopping_item = ShoppingItem.objects.create(id=uuid.uuid4(), name='Laptop', purchased=False, shopping_list=shopping_list)
    url = reverse('shopping-item-detail', kwargs={'pk': shopping_list.id, 'item_pk': shopping_item.id})
    client = APIClient()
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
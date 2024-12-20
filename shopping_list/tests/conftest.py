# shopping_list/tests/conftest.py

import pytest

from django.contrib.auth.models import User
from shopping_list.models import ShoppingList, ShoppingItem

from rest_framework.test import APIClient

@pytest.fixture(scope='session')
def create_shopping_item():
    def _create_shopping_item(name, user, shopping_list=None, purchased=False):

        if shopping_list is None:
            shopping_list = ShoppingList.objects.create(name='My shopping list')
            shopping_list.members.add(user)
            

        shopping_item = ShoppingItem.objects.create(name=name, purchased=purchased, shopping_list=shopping_list)

        return shopping_item
    
    return _create_shopping_item

@pytest.fixture(scope='session')
def create_user():    
    def _create_user():
        return User.objects.create_user('buensofvida', 'buensofvida@gmail.com', 'something')
    
    return _create_user

@pytest.fixture(scope='session')
def create_authenticated_client():
    def _create_authenticated_client(user):
        client = APIClient()
        client.force_login(user)

        return client
    
    return _create_authenticated_client


@pytest.fixture(scope='session')
def create_shopping_list():
    def _create_shopping_list(name, user):
        shopping_list = ShoppingList.objects.create(name=name)
        shopping_list.members.add(user)

        return shopping_list
    
    return _create_shopping_list
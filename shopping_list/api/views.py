# shopping_list/api/views.py

from rest_framework import generics

from shopping_list.api.permissions import (
    ShoppingListMembersOnly,
    ShoppingItemShoppingListMembersOnly,
    AllShoppingItemShoppingListMembersOnly,
)
from shopping_list.models import ShoppingList, ShoppingItem
from shopping_list.api.serializers import ShoppingListSerializer, ShoppingItemSerializer

class ListAddShoppingList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def perform_create(self, serializer):
        shopping_list = serializer.save()
        shopping_list.members.add(self.request.user)
        return shopping_list
    
    def get_queryset(self):
        return ShoppingList.objects.filter(members=self.request.user)

class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    permission_classes = [ShoppingListMembersOnly]

class AddShoppingItem(generics.CreateAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

    permission_classes = [AllShoppingItemShoppingListMembersOnly]

class ShoppingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer
    permission_classes = [ShoppingItemShoppingListMembersOnly]
    lookup_url_kwarg = 'item_pk'


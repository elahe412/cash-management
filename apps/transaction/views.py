from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.transaction.models import Category, Transaction
from apps.transaction.serializers import TransactionSerializer, CategorySerializer
from common.exceptions import PermissionException


class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filterset_fields = ['category', 'created_at', 'kind', 'created_at__lte', 'created_at__gte']
    search_fields = ['description']
    ordering_fields = ['created_at', 'amount']

    def get_queryset(self):
        if self.request.user.id:
            return super().get_queryset().filter(user=self.request.user, is_deleted=False)
        raise PermissionException()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if self.request.user == instance.user:
            serializer.save()
        else:
            raise PermissionException()

    def perform_destroy(self, instance):
        instance = self.get_object()
        if self.request.user == instance.user:
            instance.delete()
        else:
            raise PermissionException()

from django.contrib import admin

from apps.transaction.models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'is_deleted', 'deleted_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['is_deleted']
    list_display_links = ['name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'is_deleted', 'deleted_at', 'updated_at', 'category', 'kind', 'amount',
                    'description']
    search_fields = ['category', 'description', 'kind']
    list_filter = ['is_deleted', 'category']

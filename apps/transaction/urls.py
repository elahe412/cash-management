from rest_framework.routers import DefaultRouter

from apps.transaction.views import TransactionView, CategoryView

app_name = "apps.transaction"
urlpatterns = []
router = DefaultRouter()

router.register('transaction', TransactionView, basename='transaction')
router.register('category', CategoryView, basename='category')

urlpatterns += router.urls

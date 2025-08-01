from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.havasbook.views import (
    BannerView,
    CategoryView,
    BookView,
    CartitemView,
    CartView,
    LocationView,
    OrderView, 
    OrderitemView,
    BooksSearchView,
    PreorderView,
    DeliveryView, toggle_is_discount, mark_ready, 
)
# from core.apps.havasbook.views.send import mark_ready_view


router = DefaultRouter()
router.register(r"banner", BannerView, basename='banner')
router.register(r"category", CategoryView, basename='category')
router.register(r"books", BookView, basename='books')
router.register(r"cart", CartView, basename='cart')
router.register(r"cart-item", CartitemView, basename='cart-item')
router.register(r"location", LocationView, basename='location')
router.register(r"order", OrderView, basename='order')
router.register(r"order-item", OrderitemView, basename='order-item')
router.register(r"preorder", PreorderView, basename="preorder")
router.register(r"delivery", DeliveryView, basename='delivery')

# search
router.register(r"search", BooksSearchView, basename="search")




urlpatterns = [
    path("", include(router.urls)),
    path('toggle-discount/<int:pk>/', toggle_is_discount, name='toggle_is_discount'),
    
    path('order/<int:order_id>/mark-ready/', mark_ready, name='mark_ready'),
    # path("mark-ready/<int:pk>/", mark_ready_view, name="mark-ready")


]

from django.urls import path
from .views import*

urlpatterns = [
    path('custmer/', manage_custmer),
    path('custmer/<int:id>/', manage_custmer),

    path('order/', manage_order),
    path('order/<int:id>/', manage_order),

    path('product/', manage_product),
    path('product/<int:id>/', manage_product),

    path('sale/', manage_sale),
    path('sale/<int>/', manage_sale),

]


from django.urls import path

from product.views import HomePage, SubcategoryView, ProductListView, ProductDetailView, ProductResultsView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('category/<int:category_id>', SubcategoryView.as_view(), name='category'),
    path('subcategory/<int:subcategory_id>', ProductListView.as_view(), name='subcategory'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('search', ProductResultsView.as_view(), name='search')
]

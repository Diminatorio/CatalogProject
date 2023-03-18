from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import CategoryModel, SubcategoryModel, ProductModel, ProductPhotoModel


class HomePage(ListView):
    template_name = 'home_page.html'
    model = CategoryModel


class SubcategoryView(ListView):
    template_name = 'subcategory.html'
    model = SubcategoryModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        subcategory_list = SubcategoryModel.objects.all().filter(category_id=category_id)
        category = CategoryModel.objects.get(id=category_id).category_name
        context['subcategory_list'] = subcategory_list
        context['category_name'] = category
        return context


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = ProductModel
    paginate_by = 9

    def get_context_data(self, **kwargs):
        sort = self.request.GET.get('sort')
        context = super().get_context_data(**kwargs)
        subcategory_id = self.kwargs.get('subcategory_id')
        product_list = ProductModel.objects.all().filter(subcategory_id=subcategory_id).order_by('id')
        if sort:
            product_list = product_list.order_by(sort)
        subcategory = SubcategoryModel.objects.get(id=subcategory_id).subcategory_name
        paginator = Paginator(product_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['product_list'] = page_obj.object_list
        context['subcategory_name'] = subcategory
        return context


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = ProductModel
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        product = context['product']
        context['photos'] = product.photos.all()
        context['product_name'] = product.product_name
        return context


class ProductResultsView(ListView):
    template_name = 'search_list.html'
    model = ProductModel
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        sort = self.request.GET.get('sort')
        if query:
            queryset = ProductModel.objects.all().filter(product_name__icontains=query).order_by('id')
            if sort:
                queryset = queryset.order_by(sort)
        return queryset

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        context = super().get_context_data(**kwargs)
        context['search_result'] = query
        return context


def https404(request, exception):
    return render(request, '404.html', {})

from django.shortcuts import render
from products.models import Product
from django.views.generic.list import ListView
from django.db.models import Q
class SearchProductView(ListView):
    queryset = Product.objects.all()
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
        '''
            __icontains = field contains this
            __iexact = field is exactly this
        '''
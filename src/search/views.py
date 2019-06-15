from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        get_request = request.GET
        search_query = get_request.get('q', 'shirt')
        if search_query is not None:
            return Product.objects.search(search_query)
        return Product.objects.featured()

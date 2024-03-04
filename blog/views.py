from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        self.object.number_of_views += 1
        self.object.save()

        return context_data

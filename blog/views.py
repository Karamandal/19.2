from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Blog


class BlogPostListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    queryset = Blog.objects.filter(is_published=True)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.slug = slugify(blog.title)
        blog.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.slug = slugify(blog.title)
        blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:list')

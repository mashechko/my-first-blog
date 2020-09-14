from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import Post, News, Category
from .forms import PostForm
from .parsing import parsing_tut_by, parsing_onliner


# Главная страница
class MainPage(View):
    def get(self, request):
        return render(request, 'blog/mainpage.html')


# Новости
class NewsList(View):
    def get(self, request):
        parsing_tut_by()
        parsing_onliner()
        object_list = News.objects.all().order_by('-date')
        paginator = Paginator(object_list, 10)
        page = request.GET.get('page')
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        return render(request,
                      'blog/news.html',
                      {'page': page,
                       'news': news})


# Блог
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostByCategories(View):
    def get(self, request, category_id):
        posts = Post.objects.filter(category_id=category_id)
        categories = Category.objects.all()
        category = Category.objects.get(pk=category_id)
        return render(request, 'blog/category.html', {'posts': posts, 'categories': categories, 'category': category})


class CategoryList(ListView):
    model = Category
    template_name = 'base_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class PostDetail(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})


# О нас
class About(View):
    def get(self, request):
        return render(request, 'blog/about.html')


# Поиск
class SearchPost(ListView):
    model = Post
    template_name = 'blog/search_post.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query))
        return post_list


class SearchNews(ListView):
    model = News
    template_name = 'blog/search_news.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        news_list = News.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query))
        return news_list


class PostNew(CreateView):
    form_class = PostForm
    template_name = 'blog/new_post.html'

 
